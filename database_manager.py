# import pymssql
import sqlalchemy as sa
import pandas as pd


class DatabaseManager:
    """Class that manages database"""

    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.engine = sa.create_engine('mssql+pymssql://' + server + '/' + database)
        # self.conn = pymssql.connect(server=self.server, database=self.database)
        # self.cursor = self.conn.cursor()
        # mssql://*server_name*\\SQLEXPRESS/*database_name*?trusted_connection=yes

    def read_table(self, table_name):
        """Returns table_name as a pandas dataframe."""
        df = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)
        return df

    def execute_non_query(self, sql):
        """Executes SQL script with no return"""
        with self.engine.connect() as connection:
            connection.execute(sa.text(sql))
            connection.commit()
