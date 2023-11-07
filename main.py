import pymssql
from database_manager import DatabaseManager

# Connection string: Server=localhost\SQLEXPRESS01;Database=master;Trusted_Connection=True;

def read_file_to_string(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

if __name__ == '__main__':
    file_path = 'sqlcode.txt'
    sql = read_file_to_string(file_path)
    print(sql)

    db = DatabaseManager('localhost', 'master')
    db.execute_non_query(sql)
    df = db.read_table("people")
    df.to_excel('output.xlsx', index=False)
    print(df)
