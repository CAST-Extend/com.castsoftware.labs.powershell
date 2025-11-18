import cast_upgrade_1_6_23
import cast.analysers.ua
from cast.analysers import log, CustomObject, create_link, Bookmark
import os
import subprocess
import json
from collections import defaultdict


class PowerShellAnalyzerLevel(cast.analysers.ua.Extension):

    def __init__(self):
        self.exchange_file = None
        self.current_function_stack = []
        self.all_functions = {}  # {fullname: CustomObject}
        self.pending_calls = []  # List of calls to create after complete analysis
        self.current_file = None  # Current file being processed
        self.file_objects = {}  # {filepath: File object} for bookmark creation

    def start_analysis(self):
        log.info('[PowerShell] ===== Starting PowerShell analysis =====')
        self.exchange_file = self.get_intermediate_file('com.castsoftware.labs.powershell.txt')
        log.info('[PowerShell] Created exchange file')

    def start_file(self, file):
        filepath = file.get_path()
        filename = os.path.basename(filepath).lower()

        if not (filename.endswith('.ps1') or filename.endswith('.psm1')):
            log.info('[PowerShell] Skipping file: ' + filepath)
            return

        self.current_file = filename  # Keep track of current file
        self.file_objects[filepath] = file  # Store File object for bookmark creation later
        created_objects = defaultdict(list)

        program = CustomObject()
        if filename.endswith('.psm1'):
            program_type = 'PowerShellModule'
        else:
            program_type = 'PowerShellProgram'

        program.set_type(program_type)
        program.set_name(filename)
        program.set_fullname(filepath)
        program.set_parent(file)
        program.save()
        created_objects[program_type].append(filename)

        try:
            ps_script = """
            $ast = [System.Management.Automation.Language.Parser]::ParseFile('{0}',[ref]$null,[ref]$null)

            function Extract-AstInfo {{
                param($Node, $Depth = 0)

                if ($Depth -gt 30) {{ return $null }}
                if ($null -eq $Node) {{ return $null }}

                $result = @{{}}
                $result['Type'] = $Node.GetType().Name

                # Extract position information
                if ($Node.PSObject.Properties.Name -contains 'Extent') {{
                    $result['Extent'] = @{{
                        'StartLineNumber' = $Node.Extent.StartLineNumber
                        'EndLineNumber' = $Node.Extent.EndLineNumber
                        'StartColumnNumber' = $Node.Extent.StartColumnNumber
                        'EndColumnNumber' = $Node.Extent.EndColumnNumber
                        'Text' = $Node.Extent.Text
                    }}
                }}

                if ($Node.PSObject.Properties.Name -contains 'Name') {{
                    $result['Name'] = $Node.Name
                }}

                # TYPE DEFINITION (CLASS)
                if ($Node -is [System.Management.Automation.Language.TypeDefinitionAst]) {{
                    $result['Members'] = @()
                    foreach ($member in $Node.Members) {{
                        $memberInfo = @{{
                            'Type' = $member.GetType().Name
                            'Name' = $member.Name
                        }}

                        # Extract Method Body
                        if ($member -is [System.Management.Automation.Language.FunctionMemberAst]) {{
                            if ($member.Body) {{
                                $memberInfo['Body'] = Extract-AstInfo -Node $member.Body -Depth ($Depth + 1)
                            }}
                        }}

                        $result['Members'] += $memberInfo
                    }}
                }}

                # FUNCTION DEFINITION
                if ($Node -is [System.Management.Automation.Language.FunctionDefinitionAst]) {{
                    $result['Name'] = $Node.Name
                    if ($Node.Body) {{
                        $result['Body'] = Extract-AstInfo -Node $Node.Body -Depth ($Depth + 1)
                    }}
                }}

                # COMMAND (potential function call)
                if ($Node -is [System.Management.Automation.Language.CommandAst]) {{
                    $result['CommandElements'] = @()
                    foreach ($elem in $Node.CommandElements) {{
                        $entry = @{{ 'Type' = $elem.GetType().Name }}

                        if ($elem -is [System.Management.Automation.Language.StringConstantExpressionAst]) {{
                            $entry['Value'] = $elem.Value
                        }} elseif ($elem -is [System.Management.Automation.Language.CommandParameterAst]) {{
                            if ($elem.Argument) {{
                                $entry['Argument'] = $elem.Argument.Extent.Text
                            }}
                        }} elseif ($elem.PSObject.Properties.Name -contains 'Value') {{
                            $entry['Value'] = $elem.Value
                        }} elseif ($elem.PSObject.Properties.Name -contains 'VariablePath') {{
                            $entry['Value'] = $elem.VariablePath.UserPath
                        }}

                        if ($elem.PSObject.Properties.Name -contains 'Extent') {{
                            $entry['Extent'] = @{{
                                'Text' = $elem.Extent.Text
                                'StartLineNumber' = $elem.Extent.StartLineNumber
                            }}
                        }}

                        $result['CommandElements'] += $entry
                    }}
                }}

                # INVOKE MEMBER EXPRESSION ($this.Method() or $object.Method())
                if ($Node -is [System.Management.Automation.Language.InvokeMemberExpressionAst]) {{
                    $result['Member'] = $Node.Member.Value

                    if ($Node.Expression) {{
                        $expr = @{{
                            'Type' = $Node.Expression.GetType().Name
                        }}

                        # Extract Extent → CRUCIAL pour récupérer "$this"
                        if ($Node.Expression.Extent) {{
                            $expr['Extent'] = @{{
                                'Text' = $Node.Expression.Extent.Text
                                'StartLine' = $Node.Expression.Extent.StartLineNumber
                                'EndLine' = $Node.Expression.Extent.EndLineNumber
                                'StartCol' = $Node.Expression.Extent.StartColumnNumber
                                'EndCol' = $Node.Expression.Extent.EndColumnNumber
                            }}
                        }}

                        # VariablePath si disponible
                        if ($Node.Expression.PSObject.Properties.Name -contains 'VariablePath') {{
                            $expr['VariablePath'] = $Node.Expression.VariablePath.UserPath
                        }}

                        $result['Expression'] = $expr
                    }}
                }}

                # Properties to explore recursively
                $childProperties = @(
                    'Body',
                    'ScriptBlock',
                    'BeginBlock',
                    'ProcessBlock',
                    'EndBlock',
                    'Statements',
                    'Statement',
                    'Pipeline',
                    'PipelineElements',
                    'Command',
                    'Expression',
                    'Left',
                    'Right',
                    'Children'
                )

                foreach ($prop in $childProperties) {{
                    if ($Node.PSObject.Properties.Name -contains $prop) {{
                        $childNode = $Node.$prop
                        if ($null -ne $childNode) {{
                            if ($childNode -is [System.Collections.IEnumerable] -and $childNode -isnot [string]) {{
                                $result[$prop] = @()
                                foreach ($item in $childNode) {{
                                    $extracted = Extract-AstInfo -Node $item -Depth ($Depth + 1)
                                    if ($null -ne $extracted) {{
                                        $result[$prop] += $extracted
                                    }}
                                }}
                            }} else {{
                                $extracted = Extract-AstInfo -Node $childNode -Depth ($Depth + 1)
                                if ($null -ne $extracted) {{
                                    $result[$prop] = $extracted
                                }}
                            }}
                        }}
                    }}
                }}

                return $result
            }}

            $extracted = Extract-AstInfo -Node $ast
            $extracted | ConvertTo-Json -Depth 30 -Compress
            """.format(filepath.replace("'", "''").replace('\\', '\\\\'))

            ps_executables = ["pwsh", "powershell.exe"]
            result_stdout = None

            for ps_executable in ps_executables:
                try:
                    process = subprocess.Popen(
                        [ps_executable, "-NoProfile", "-Command", ps_script],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    stdout_data, stderr_data = process.communicate()
                    result_stdout = stdout_data.decode("utf-8", errors="ignore")
                    if process.returncode == 0:
                        break
                except Exception:
                    continue

            if not result_stdout:
                log.warning("[PowerShell] No output from PowerShell parser")
                return

            ast = json.loads(result_stdout)

        except Exception as e:
            log.warning("[PowerShell] Failed to parse AST for {}: {}".format(filepath, e))
            return

        self.explore_ast(ast, program, created_objects, filename, filepath)

        log.info('[PowerShell] === Object creation summary for file: {} ==='.format(filename))
        total = 0
        for obj_type, names in created_objects.items():
            total += len(names)
            log.info('[PowerShell] {} ({}): {}'.format(obj_type, len(names), ', '.join(names)))
        log.info('[PowerShell] Total objects created: {}'.format(total))

    def explore_ast(self, node, program, created_objects, filename, filepath):
        if isinstance(node, dict):
            node_type = node.get("Type")
            node_name = node.get("Name")
            extent = node.get("Extent", {})
            line_number = extent.get("StartLineNumber", -1)

            # -------- CLASS + METHOD --------
            if node_type == "TypeDefinitionAst":
                class_obj = CustomObject()
                class_obj.set_type("PowerShellClass")
                class_obj.set_name(node_name)
                class_obj.set_fullname(filename + '.' + node_name)
                class_obj.set_parent(program)
                class_obj.save()
                created_objects["PowerShellClass"].append(node_name)

                for member in node.get("Members", []):
                    if isinstance(member, dict) and member.get("Type") == "FunctionMemberAst":
                        method_name = member.get("Name")
                        # Don't treat constructor as a normal method
                        if method_name and method_name.lower() != node_name.lower():
                            method_obj = CustomObject()
                            method_obj.set_type("PowerShellMethod")
                            method_obj.set_name(method_name)
                            method_fullname = filename + '.' + node_name + '.' + method_name
                            method_obj.set_fullname(method_fullname)
                            method_obj.set_parent(class_obj)
                            method_obj.save()
                            created_objects["PowerShellMethod"].append(method_name)

                            # Register method in global dictionary
                            self.all_functions[method_fullname] = method_obj

                            # Explore method body to detect calls
                            log.info("[PowerShell] Exploring method body: {}".format(method_fullname))
                            self.current_function_stack.append({
                                'fullname': method_fullname,
                                'class': node_name  # Keep track of the class
                            })

                            # Explore method Body recursively
                            method_body = member.get("Body")
                            if method_body:
                                self.explore_ast(method_body, program, created_objects, filename, filepath)

                            self.current_function_stack.pop()

                # Don't explore members recursively after processing them
                return

            # -------- FUNCTION --------
            elif node_type == "FunctionDefinitionAst":
                if node_name:
                    fullname = filename + '.' + node_name

                    func_obj = CustomObject()
                    func_obj.set_type("PowerShellFunction")
                    func_obj.set_name(node_name)
                    func_obj.set_fullname(fullname)
                    func_obj.set_parent(program)
                    func_obj.save()
                    created_objects["PowerShellFunction"].append(node_name)

                    # Register function in global dictionary
                    self.all_functions[fullname] = func_obj

                    # Push caller onto stack
                    self.current_function_stack.append({
                        'fullname': fullname,
                        'class': None
                    })

                    # Traverse function body to detect calls
                    for k, v in node.items():
                        if isinstance(v, (list, dict)):
                            self.explore_ast(v, program, created_objects, filename, filepath)

                    # Pop caller
                    self.current_function_stack.pop()

                    return

            # -------- INVOKE MEMBER EXPRESSION ($this.Method() or $object.Method()) --------
            elif node_type == "InvokeMemberExpressionAst":
                method_name = node.get("Member")
                expression_info = node.get("Expression", {})

                expr_text = expression_info.get("Extent", {}).get("Text", "").strip()
                is_this_call = expr_text.startswith("$this")

                log.info("[PowerShell DEBUG] Found InvokeMemberExpressionAst: Member={}, ExprText={}".format(
                    method_name, expr_text))

                if method_name and is_this_call and self.current_function_stack:
                    caller_info = self.current_function_stack[-1]
                    caller_fullname = caller_info['fullname']
                    caller_class = caller_info.get('class')

                    if caller_class:
                        callee_fullname = filename + '.' + caller_class + '.' + method_name

                        call_info = {
                            'caller': caller_fullname,
                            'callee': method_name,
                            'callee_fullname': callee_fullname,
                            'filepath': filepath,
                            'line': line_number,
                            'type': 'method_call'
                        }
                        self.pending_calls.append(call_info)

                        log.info("[PowerShell] Detected $this method call: {} -> {} (line {})".format(
                            caller_fullname, callee_fullname, line_number
                        ))


            # -------- CALL DETECTION (CommandAst) --------
            elif node_type == "CommandAst":
                elems = node.get("CommandElements", [])

                if isinstance(elems, list) and len(elems) > 0:
                    first_elem = elems[0]
                    callee_name = first_elem.get("Value")

                    # If no Value, try to extract from Extent/Text
                    if not callee_name:
                        elem_extent = first_elem.get("Extent", {})
                        extent_text = elem_extent.get("Text", "").strip()
                        if extent_text:
                            # Clean text (remove &, quotes, etc.)
                            callee_name = extent_text.strip("&").strip().strip("'\"")
                            log.info("[PowerShell DEBUG] Extracted from Extent.Text: {}".format(callee_name))

                    if callee_name:
                        # Determine caller
                        if self.current_function_stack:
                            caller_info = self.current_function_stack[-1]
                            caller_fullname = caller_info['fullname']
                        else:
                            caller_fullname = "GLOBAL"

                        # Register call for later processing
                        call_info = {
                            'caller': caller_fullname,
                            'callee': callee_name,
                            'filepath': filepath,
                            'line': line_number,
                            'type': 'function_call',
                            'source_file': filename  # Keep track of source file
                        }
                        self.pending_calls.append(call_info)

                        log.info("[PowerShell] Detected call: {} -> {} (line {})".format(
                            caller_fullname, callee_name, line_number
                        ))

            # Traverse children recursively
            for k, v in node.items():
                if isinstance(v, (list, dict)) and k != "Members":  # Don't reprocess Members
                    self.explore_ast(v, program, created_objects, filename, filepath)

        elif isinstance(node, list):
            for item in node:
                self.explore_ast(item, program, created_objects, filename, filepath)

    def end_analysis(self):
        log.info('[PowerShell] ===== Resolving and creating call links =====')

        # Create index for fast resolution: {short_name: [fullname1, fullname2, ...]}
        functions_by_name = defaultdict(list)
        for fullname in self.all_functions.keys():
            short_name = fullname.split('.')[-1]
            functions_by_name[short_name].append(fullname)

        # Statistics
        intra_file_links = 0
        inter_file_links = 0
        unresolved_calls = 0
        native_cmdlets = 0
        method_calls = 0

        for call in self.pending_calls:
            caller_fullname = call['caller']
            callee_name = call['callee']
            call_type = call.get('type', 'function_call')

            # Find caller object
            caller_obj = None
            if caller_fullname != "GLOBAL":
                caller_obj = self.all_functions.get(caller_fullname)

            if not caller_obj:
                unresolved_calls += 1
                continue

            callee_obj = None

            # CASE 1: $this.Method() call - we already know the fullname
            if call_type == 'method_call':
                callee_fullname = call.get('callee_fullname')
                if callee_fullname and callee_fullname in self.all_functions:
                    callee_obj = self.all_functions[callee_fullname]
                    method_calls += 1

                    # Determine if method call is intra or inter-file
                    caller_file = caller_fullname.split('.')[0]
                    callee_file = callee_fullname.split('.')[0]
                    if caller_file == callee_file:
                        intra_file_links += 1
                    else:
                        inter_file_links += 1

                    log.info("[PowerShell] Resolved $this method call: {} -> {}".format(
                        caller_fullname, callee_fullname))

            # CASE 2: Function call - smart resolution
            else:
                # Extract file name from caller fullname
                caller_file = caller_fullname.split('.')[0]

                # PRIORITY 1: Look in same file as caller (intra-file)
                potential_intra_file = caller_file + '.' + callee_name
                if potential_intra_file in self.all_functions:
                    callee_obj = self.all_functions[potential_intra_file]
                    intra_file_links += 1
                    log.info("[PowerShell] Intra-file call (PRIORITY): {} -> {}".format(
                        caller_fullname, potential_intra_file))
                else:
                    # PRIORITY 2: If function doesn't exist locally, search elsewhere
                    candidates = functions_by_name.get(callee_name, [])

                    if len(candidates) == 1:
                        # Only one function with this name exists
                        callee_fullname = candidates[0]
                        callee_obj = self.all_functions[callee_fullname]

                        # Check if it's actually intra or inter-file
                        callee_file = callee_fullname.split('.')[0]
                        if caller_file == callee_file:
                            intra_file_links += 1
                            log.info("[PowerShell] Intra-file call (unique match): {} -> {}".format(
                                caller_fullname, callee_fullname))
                        else:
                            inter_file_links += 1
                            log.info("[PowerShell] Inter-file call (unique match): {} -> {}".format(
                                caller_fullname, callee_fullname))

                    elif len(candidates) > 1:
                        # Multiple functions with same name
                        log.warning("[PowerShell] Ambiguous call: {} exists in multiple files: {}".format(
                            callee_name, candidates))

                        # Look in same file first
                        same_file_candidate = None
                        for candidate in candidates:
                            candidate_file = candidate.split('.')[0]
                            if candidate_file == caller_file:
                                same_file_candidate = candidate
                                break

                        if same_file_candidate:
                            # Found function in same file
                            callee_obj = self.all_functions[same_file_candidate]
                            intra_file_links += 1
                            log.info("[PowerShell] Intra-file call (ambiguous resolved to same file): {} -> {}".format(
                                caller_fullname, same_file_candidate))
                        else:
                            # No function in same file, take first one
                            callee_fullname = candidates[0]
                            callee_obj = self.all_functions[callee_fullname]
                            inter_file_links += 1
                            log.info("[PowerShell] Inter-file call (ambiguous, first match): {} -> {}".format(
                                caller_fullname, callee_fullname))

            # If callee found, write to exchange file AND create link
            if callee_obj:
                callee_fullname = callee_obj.fullname if callee_obj.fullname else callee_obj.name

                # First write to exchange file
                line_to_write = "CALL;{};{};{};{}\n".format(
                    caller_fullname,
                    callee_fullname,
                    call['filepath'],
                    call['line']
                )
                self.exchange_file.write(line_to_write)

                # Then try to create link
                try:
                    file_obj = self.file_objects.get(call['filepath'])
                    if file_obj:
                        bookmark = Bookmark(file_obj, call['line'], -1, -1, -1)
                        create_link('callLink', caller_obj, callee_obj, bookmark)
                        log.info("[PowerShell] Created link from {} to {}".format(caller_fullname, callee_fullname))
                    else:
                        log.warning("[PowerShell] File object not found for: {}".format(call['filepath']))
                except Exception as e:
                    log.warning("[PowerShell] Failed to create link but exchange file written: {}".format(e))
            else:
                # Probably a native PowerShell cmdlet
                native_cmdlets += 1

        log.info('[PowerShell] Call links summary:')
        log.info('[PowerShell]   - Intra-file links (same file): {}'.format(intra_file_links))
        log.info('[PowerShell]   - Inter-file links (cross file): {}'.format(inter_file_links))
        log.info('[PowerShell]   - Method calls ($this): {}'.format(method_calls))
        log.info('[PowerShell]   - Native cmdlets (ignored): {}'.format(native_cmdlets))
        log.info('[PowerShell]   - Unresolved calls (from GLOBAL): {}'.format(unresolved_calls))
        log.info('[PowerShell]   - Total calls detected: {}'.format(len(self.pending_calls)))

        log.info('[PowerShell] ===== End of PowerShell analysis =====')
        if self.exchange_file:
            self.exchange_file.close()