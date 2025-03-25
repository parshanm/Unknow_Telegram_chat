import sqlite3

class Data:
    def add_table(self):
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
            connection.commit()

            table_create_query_admin = """
                CREATE TABLE IF NOT EXISTS admins(
                id integer primary key,
                first_name text,
                gender text
                );
            """
            cursor.execute(table_create_query_admin)

    def get_info(self):
        with sqlite3.connect('unknow.db') as connection:
            pass


if __name__ == '__main__':
    data = Data()
    data.get_info()
