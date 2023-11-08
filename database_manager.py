import sqlalchemy as sa
import pandas as pd


class DatabaseManager:
    """Class that manages database"""

    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.engine = sa.create_engine('mssql+pymssql://' + server + '/' + database)

    def read_table(self, table_name):
        """Returns table_name as a pandas dataframe."""
        df = pd.read_sql(f'SELECT * FROM {table_name}', self.engine)
        return df

    def execute_query(self, query):
        """Executes custom sql query and returns as a pandas dataframe."""
        with self.engine.connect() as connection:
            result = connection.execute(sa.text(query))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            connection.commit()
        return df

    def execute_non_query(self, sql):
        """Executes SQL script with no return"""
        with self.engine.connect() as connection:
            connection.execute(sa.text(sql))
            connection.commit()
