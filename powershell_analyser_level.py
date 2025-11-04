import cast_upgrade_1_6_23
import cast.analysers.ua
from cast.analysers import log, CustomObject
import os
import subprocess
import json
from collections import defaultdict


class PowerShellAnalyzerLevel(cast.analysers.ua.Extension):

    def __init__(self):
        self.exchange_file = None

    def start_analysis(self):
        log.info('[PowerShell] ===== Starting PowerShell analysis =====')
        self.exchange_file = self.get_intermediate_file('com.castsoftware.labs.powershell.txt')
        log.info('[PowerShell] Created exchange file com.castsoftware.labs.powershell.txt')

    def start_file(self, file):
        """
        Called for every file selected in the analysis.
        """
        filepath = file.get_path()
        filename = os.path.basename(filepath).lower()

        if not (filename.endswith('.ps1') or filename.endswith('.psm1')):
            log.info('[PowerShell] Skipping file: ' + filepath)
            return

        log.info('[PowerShell] Processing file: ' + filepath)

        created_objects = defaultdict(list)

        # Create root program/module object
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

        # Parse file using PowerShell AST with custom serialization script
        try:
            # PowerShell script that extracts only what we need from AST
            ps_script = """
$ast = [System.Management.Automation.Language.Parser]::ParseFile('{0}',[ref]$null,[ref]$null)

function Extract-AstInfo {{
    param($Node, $Depth = 0)

    if ($Depth -gt 20) {{ return $null }}
    if ($null -eq $Node) {{ return $null }}

    $result = @{{}}
    $result['Type'] = $Node.GetType().Name

    # Extract Name if exists
    if ($Node.PSObject.Properties.Name -contains 'Name') {{
        $result['Name'] = $Node.Name
    }}

    # For TypeDefinitionAst (classes)
    if ($Node -is [System.Management.Automation.Language.TypeDefinitionAst]) {{
        $result['Members'] = @()
        foreach ($member in $Node.Members) {{
            $memberInfo = @{{
                'Type' = $member.GetType().Name
                'Name' = $member.Name
            }}
            $result['Members'] += $memberInfo
        }}
    }}

    # For FunctionDefinitionAst
    if ($Node -is [System.Management.Automation.Language.FunctionDefinitionAst]) {{
        $result['Name'] = $Node.Name
    }}

    # Process child nodes
    $childProperties = @('Body', 'ScriptBlock', 'BeginBlock', 'ProcessBlock', 'EndBlock', 'Statements')
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
$extracted | ConvertTo-Json -Depth 20 -Compress
""".format(filepath.replace("'", "''").replace('\\', '\\\\'))

            # Try pwsh first (PowerShell Core), fall back to powershell.exe (Windows PowerShell)
            ps_executables = ["pwsh", "powershell.exe"]
            result_stdout = None
            result_stderr = None

            for ps_executable in ps_executables:
                try:
                    process = subprocess.Popen(
                        [ps_executable, "-NoProfile", "-Command", ps_script],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    stdout_data, stderr_data = process.communicate()
                    result_stdout = stdout_data.decode("utf-8", errors="ignore")
                    result_stderr = stderr_data.decode("utf-8", errors="ignore")

                    if process.returncode != 0:
                        log.warning("[PowerShell] {} exited with code {}: {}".format(
                            ps_executable, process.returncode, result_stderr))
                        if ps_executable == ps_executables[-1]:
                            # Last executable failed, return
                            return
                        continue
                    break

                except (OSError, FileNotFoundError) as e:
                    if ps_executable == ps_executables[-1]:
                        # Last executable not found
                        log.warning("[PowerShell] No PowerShell executable found (tried: {}): {}".format(
                            ', '.join(ps_executables), e))
                        return
                    # Try next executable
                    continue

            if not result_stdout:
                log.warning("[PowerShell] No AST returned for file: " + filepath)
                return

            ast = json.loads(result_stdout)

        except json.JSONDecodeError as e:
            log.warning("[PowerShell] Failed to parse JSON from PowerShell AST for {} : {}".format(filepath, e))
            return
        except Exception as e:
            log.warning("[PowerShell] Failed to parse PowerShell AST for {} : {}".format(filepath, e))
            return

        # Recursive AST exploration
        self.explore_ast(ast, program, created_objects, filename, filepath)

        # Summary logs
        log.info('[PowerShell] === Object creation summary for file: {} ==='.format(filename))
        total = 0
        for obj_type, names in created_objects.items():
            total += len(names)
            log.info('[PowerShell] {} ({}): {}'.format(obj_type, len(names), ', '.join(names)))
        log.info('[PowerShell] Total objects created: {}'.format(total))

    def explore_ast(self, node, program, created_objects, filename, filepath):
        """
        Recursively explore AST nodes and create CAST objects.
        """
        if isinstance(node, dict):
            node_type = node.get("Type")
            node_name = node.get("Name")

            # PowerShell class
            if node_type == "TypeDefinitionAst":
                class_obj = CustomObject()
                class_obj.set_type("PowerShellClass")
                class_obj.set_name(node_name)
                class_obj.set_fullname(filename + '.' + node_name)
                class_obj.set_parent(program)
                class_obj.save()
                created_objects["PowerShellClass"].append(node_name)

                # Explore its members (methods, properties)
                for member in node.get("Members", []):
                    if isinstance(member, dict) and member.get("Type") == "FunctionMemberAst":
                        method_name = member.get("Name")
                        if method_name and method_name.lower() == node_name.lower():
                            continue
                        if method_name:
                            method_obj = CustomObject()
                            method_obj.set_type("PowerShellMethod")
                            method_obj.set_name(method_name)
                            method_obj.set_fullname(filename + '.' + node_name + '.' + method_name)
                            method_obj.set_parent(class_obj)
                            method_obj.save()
                            created_objects["PowerShellMethod"].append(method_name)
                            self.exchange_file.write(method_name + ';' + filepath + '\n')

            # Global function
            elif node_type == "FunctionDefinitionAst":
                if node_name:
                    func_obj = CustomObject()
                    func_obj.set_type("PowerShellFunction")
                    func_obj.set_name(node_name)
                    func_obj.set_fullname(filename + '.' + node_name)
                    func_obj.set_parent(program)
                    func_obj.save()
                    created_objects["PowerShellFunction"].append(node_name)
                    self.exchange_file.write(node_name + ';' + filepath + '\n')

            # Recurse deeper
            for k, v in node.items():
                if isinstance(v, (list, dict)):
                    self.explore_ast(v, program, created_objects, filename, filepath)

        elif isinstance(node, list):
            for item in node:
                self.explore_ast(item, program, created_objects, filename, filepath)

    def end_analysis(self):
        log.info('[PowerShell] ===== End of PowerShell analysis =====')
        if self.exchange_file:
            self.exchange_file.close()