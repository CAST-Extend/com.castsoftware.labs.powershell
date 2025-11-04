# -*- coding: utf-8 -*-
"""
PowerShell Analyzer Level
Compatible with CAST 8.3 (Python 3.4)
"""

import cast_upgrade_1_6_23
import cast.analysers.ua
from cast.analysers import log, CustomObject, Bookmark, create_link
from cast.application import open_source_file
import os
import re


class PowerShellAnalyzerLevel(cast.analysers.ua.Extension):

    def __init__(self):
        # File used to pass data from analyzer level to application level
        self.exchange_file = None

    def start_analysis(self):
        log.info('[PowerShell] ===== Starting PowerShell analysis =====')

        # Create intermediate file for communication with Application Level
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

        # Create root program/module object
        program = CustomObject()
        if filename.endswith('.psm1'):
            program.set_type('PowerShellModule')
        else:
            program.set_type('PowerShellProgram')

        program.set_name(filename)
        program.set_fullname(filepath)
        program.set_parent(file)  # project as parent (DataPower pattern)
        program.save()

        # Parse PowerShell content
        line_count = 0
        current_class = None
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    line_count += 1
                    stripped = line.strip()

                    if not stripped or stripped.startswith('#'):
                        continue

                    # Detect class
                    m_class = re.match(r'^class\s+([A-Za-z_]\w*)', stripped)
                    if m_class:
                        class_name = m_class.group(1)
                        class_obj = CustomObject()
                        class_obj.set_type('PowerShellClass')
                        class_obj.set_name(class_name)
                        class_obj.set_fullname(filename + '.' + class_name)
                        class_obj.set_parent(program)
                        class_obj.save()
                        current_class = class_obj
                        continue

                    # Detect function
                    m_func = re.match(r'^function\s+([A-Za-z_]\w*)', stripped)
                    if m_func:
                        func_name = m_func.group(1)
                        func_obj = CustomObject()
                        func_obj.set_type('PowerShellFunction' if not current_class else 'PowerShellMethod')
                        func_obj.set_name(func_name)
                        func_obj.set_fullname(filename + '.' + func_name)
                        func_obj.set_parent(current_class or program)
                        func_obj.save()

                        # Example of writing to exchange file
                        self.exchange_file.write(func_name + ';' + filepath + '\n')
                        continue

                    # Reset class context when '}' encountered
                    if stripped == '}':
                        current_class = None

        except Exception as e:
            log.warning('[PowerShell] Error while reading file ' + filepath + ' : ' + str(e))

        log.info('[PowerShell] File processed with ' + str(line_count) + ' lines.')

    def end_analysis(self):
        log.info('[PowerShell] ===== End of PowerShell analysis =====')
        if self.exchange_file:
            self.exchange_file.close()
