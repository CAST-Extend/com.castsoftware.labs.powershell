'''
Get tables ocontent into memory and restore it latter

## saves the content of result tables into a variable
content = get_tables_content( metadata, tables)

...

## put back those tables as before
restore_tables_content(engine, content)



Created on 25 avr. 2015

@author: MRO
'''
from sqlalchemy import MetaData, Table

"""
set of tables to save/restore
"""
result_tables = ['acc',
                 'accbook',
                 'accbooksymb',
                 'accraw',
                 'accsymb',
                 'anaattr',
                 'anadsc',
                 'anainf',
                 'anajob',
                 'anapro',
                 'anaproset',
                 'appset',
                 'dfc',
                 'dss_positions',
                 'fusacc',
                 'jobanalysisproperties',
                 'keydat',
                 'keypar',
                 'keys',
                 'objdsc',
                 'objdscref',
                 'objects',
                 'objects_similarities',
                 'objfilref',
                 'objfulnam',
                 'objinf',
                 'objpar',
                 'objpos',
                 'objpro',
                 'opetrack',
                 'prodep',
                 'proroot',
                 'refpath',
                 'ref_info_kind',
                 'usr',
                 'usrpro',
                 'usrprojob',
                 'usrproroot']


def get_tables_content(engine, schema, tables):
    """
    Save the tables content into a variable
    """
    result = {}
    
    metadata = MetaData(bind=engine, schema=schema)
        
    for tableName in tables:
        
        table_content = []
        table = Table(tableName, metadata, autoload=True, autoload_with=engine)

        for row_data in engine.execute(table.select()):  # add table rows
            table_content.append(row_data)
            
        result[table] = table_content
        
    return result

def restore_tables_content(engine, content):
    """
    Restore the tables content from a variable
    """
    
    for table, table_content in content.items():

        # first delete all
        query = table.delete()
        engine.execute(query)
          
        # weird : if the content is empty, the insert query fails
        # so simply skip when nothing to do
        if table_content:
            query = table.insert()
            connection = engine.connect()
             
            connection.execute(query, table_content)
