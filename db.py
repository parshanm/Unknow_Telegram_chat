import sqlite3

class Data:
    def add_table(self):
        with sqlite3.connect('unknow.db') as connection:
            cursor = connection.cursor()
            table_create_query = """
                CREATE TABLE IF NOT EXISTS user(
                user_id INTEGER PRIMARY KEY,
                chat_id INTEGER,
                first_name TEXT,
                gender TEXT,
                age INTEGER
                );
            """
            cursor.execute(table_create_query)
            connection.commit()

            table_create_query_admin = """
                CREATE TABLE IF NOT EXISTS admins(
                user_id INTEGER PRIMARY KEY,
                chat_id INTEGER,
                first_name text,
                gender text
                );
            """
            cursor.execute(table_create_query_admin)

    def get_info(self, user_id):
        with sqlite3.connect('unknow.db') as connection:
            cursor = connection.cursor()
            data = cursor.execute("SELECT * FROM user WHERE user_id=?", (user_id, ))
        print(data.fetchone())
        return data.fetchone()
    
    def add_user(self, info : dict):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """
                INSERT TO user VALUES(?, ?, ?, ?, ?)
                """
                cursor.execute(query, (info['user_id'], info['chat_id'], info['first_name'], info['gender'],
                                        info['age']))
                connection.commit()
            except Exception as e:
                print(e)

    def add_admin(self, info : dict):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """
                INSERT TO admin VALUES(?, ?, ?, ?)
                """
                cursor.execute(query, (info['user_id'], info['chat_id'], info['first_name'], info['gender']))
                connection.commit()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    data = Data()
    data.get_info(1)
