import sqlite3

class Data:
    def add(self):
        with sqlite3.connect('unknow.db') as connection:
            cursor = connection.cursor()
            table_create_query = """
                CREATE TABLE IF NOT EXISTS user(
                id integer primary key,
                first_name text,
                gender text,
                age integer
                );
            """
            cursor.execute(table_create_query)
            

if __name__ == '__main__':
    data = Data()
    data.add()
