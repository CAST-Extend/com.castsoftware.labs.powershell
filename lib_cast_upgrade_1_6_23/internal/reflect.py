'''
Created on 19 mai 2016

@author: MRO
'''
from sqlalchemy import event, Table, Column, String, Integer, TIMESTAMP, Text, Numeric
from .tables import tables


def reflect_table(name, metadata, engine):
    """
    
    """
    
    # search in the static schema
    try:
        global tables
        table_info = tables[name.lower()]
        
        result = Table(table_info['name'],
                       metadata,
                       implicit_returning=False,
                       quote=False)
        
        for column_info in table_info['columns']:
            
            type_info = column_info['type'] 
            if type_info == 'Integer':
                column_type = Integer
            elif type_info == 'String':
                column_type = String(column_info['length'])
            elif type_info == 'Numeric':
                column_type = Numeric
            elif type_info == 'TIMESTAMP':
                column_type = TIMESTAMP
            elif type_info == 'Text':
                column_type = Text

            primary_key = False
            try:
                primary_key = column_info['primary_key']
            except:
                pass

            column = Column(column_info['name'], 
                            column_type,
                            primary_key=primary_key,
                            key=column_info['name'].lower(),
                            quote=False)
            try:
                # for sqlalchemy 1.4.31
                result.append_column(column, replace_existing=True)
            except TypeError:
                # compatibility with 0.9.7 version 
                result.append_column(column)
        
        return result
        
    except KeyError:
#         print('not using cache for', name)
        return do_reflect_table(name, metadata, engine)
    


# see : http://stackoverflow.com/questions/9383837/sqlalchemy-reflection-different-backends-and-table-column-case-insensitivity

@event.listens_for(Table, 'column_reflect')
def listen_for_reflect(inspector, table, column_info):
    "receive a column_reflect event and add key lower case"
    name = column_info['name']
    column_info['key'] = name.lower()


def do_reflect_table(name, metadata, engine):
    """
    Custom reflect wrapper for mixed case and sensitivity
    """
    if engine.dialect.name != 'mssql':
        name = name.lower()
        
    return Table(name, 
                 metadata,
                 implicit_returning=False,
                 autoload=True,
                 autoload_with=engine,
                 keep_existing=True)
