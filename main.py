from database_manager import DatabaseManager

# Connection string: Server=localhost\SQLEXPRESS01;Database=master;Trusted_Connection=True;

def read_file_to_string(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data


if __name__ == '__main__':
    db = DatabaseManager('localhost', 'master')
    df = db.execute_query(read_file_to_string('sqlcode.sql'))
    df.to_excel('output.xlsx', index=False)
    print(df)
