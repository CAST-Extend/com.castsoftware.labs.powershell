"""
dump des données : 

C:\Program Files\CAST\CASTStorageService2\bin\pg_dump.exe --host localhost --port 2280 --username "operator" --no-password  --format plain --data-only --verbose --file "C:\temp\oracle_connection.txt" --schema "b800_mngt" "postgres"

"""

import os
import subprocess



def backup(backup_file, schema, host='localhost', port=2280, user='operator', password='CastAIP'):
    """
    Backup a schema into a file.
    """
    bin_path = get_bin_path()
    
    return_code = subprocess.call([bin_path +'/pg_dump.exe', 
                                   '--host', host,
                                   '--port', str(port),
                                   '--username', user,
                                   '--no-password', 
                                   '--schema', schema,
                                   '-Fc', '--compress=9',
                                   '--file', backup_file,
                                   'postgres'
                                   ], env=dict(os.environ, PGPASSWORD=password))
    
    return return_code
    

def restore(backup_file, host='localhost', port=2280, user='operator'):
    """
    Restore a backup.
    """
    bin_path = get_bin_path()
    
    return_code = subprocess.call([bin_path +'/pg_restore.exe', 
                                   '--host', host,
                                   '--port', str(port),
                                   '--username', user,
                                   '--dbname', "postgres",
                                   '--no-password', 
                                   '--clean',
                                   backup_file,
                                   ])
    print(return_code)
    return return_code


def get_bin_path():
    
    return os.path.join((os.path.dirname(__file__)), 'bin')
