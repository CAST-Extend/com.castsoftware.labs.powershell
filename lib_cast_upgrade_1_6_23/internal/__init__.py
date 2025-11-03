application = None

def get_current_application():
    global application
    return application

def set_current_application(current):
    global application
    application = current


def is_debug_log():
    """
    True when debug log is activated
    """
    # get intermediate folder (LISA)
    import logging
    import sys
    
    intermediate_folder = None
    
    # when launched by CMS : we have the option
    try:
        arguments = sys.argv
        intermediate_option = arguments.index('--intermediate')
        if intermediate_option > 0:
            intermediate_folder = arguments[intermediate_option+1]   
    
    except:
        # many things may have happen : for example we are running from anarun.
        pass
    
    # probably in test mode...
    if not intermediate_folder:
        return True
    
    try:
        import glob, os
        import xml.etree.ElementTree as ET
        
        have_settings = False
        
        # scan the JobSettings.xml files
        # each one is generated when doing an analysis (either full or partial)
        for settings in glob.glob(os.path.join(intermediate_folder, '*', 'JobSettings.xml')):
            
            have_settings = True
            
            tree = ET.parse(settings)
            root = tree.getroot()
        
            for node in root.iter('includeDebug'):
                
                if node.text.strip() == 'true':
                    return True
                if node.text.strip() == 'false':
                    return False
                
        if have_settings:
            # Case : take a snapshot
            # the job settings do not contain the option : so no debug
            return False  
    except:
        # be cool
        pass
    
    # probably in test mode...
    return True



report_path = None

def get_report_path():
    global report_path
    return report_path

def set_report_path(path):
    global report_path
    report_path = path


reports = []

def _add_report(name, status, label, value, secondary_label, secondary_value, detail_report_path):
    global reports
    
    # check values
    if status not in ['OK', 'KO', 'Warning', None]:
        raise RuntimeError('Invalid status for report.')
    
    if type(name) != str:
        raise RuntimeError('Invalid name for report, str expected.')

    if type(label) != str:
        raise RuntimeError('Invalid label for report, str expected.')

    if type(value) != str:
        raise RuntimeError('Invalid value for report, str expected.')

    if secondary_label and type(secondary_label) != str:
        raise RuntimeError('Invalid secondary_label for report, str expected.')

    if secondary_value and type(secondary_value) != str:
        raise RuntimeError('Invalid secondary_value for report, str expected.')

    if detail_report_path and type(detail_report_path) != str:
        raise RuntimeError('Invalid detail_report_path for report, str expected.')
    
    plugin = get_current_plugin()
    
    reports.append((name, status, label, value, secondary_label, secondary_value, detail_report_path, plugin.name if plugin else ''))

def _create_xml_report_file():
    global reports
    global report_path
    
    if not report_path:
        return
    
    import logging
    
    logging.info('Publishing %s reports', len(reports))
    
    import xml.etree.ElementTree as etree
    
    root = etree.Element("reports")
    
    for name, status, label, value, secondary_label, secondary_value, detail_report_path, plugin in reports:
        
        report_node = etree.Element("report")
        
        report_node.attrib['name'] = name
        if status:
            report_node.attrib['status'] = status
        report_node.attrib['label'] = label
        report_node.attrib['value'] = value
        if secondary_label:
            report_node.attrib['label2'] = secondary_label
        if secondary_value:
            report_node.attrib['value2'] = secondary_value
        if detail_report_path:
            report_node.attrib['path'] = detail_report_path
        if plugin:
            report_node.attrib['extension'] = plugin
        
        root.append(report_node)

    tree = etree.ElementTree(root)
    tree.write(report_path)    
    
    
current_event = None

def get_current_event():
    global current_event
    return current_event

def set_current_event(event):
    global current_event
    current_event = event


current_plugin = None

def get_current_plugin():
    global current_plugin
    return current_plugin

def set_current_plugin(plugin):
    global current_plugin
    current_plugin = plugin


