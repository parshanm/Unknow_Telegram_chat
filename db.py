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
            connection.commit()
            return 'done'

    def get_info(self, user_id):
        with sqlite3.connect('unknow.db') as connection:
            cursor = connection.cursor()
            data = cursor.execute("SELECT * FROM user WHERE user_id=?", (user_id, )).fetchone()
        print(data)
        return data
    
    def add_user(self, info : dict):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """
                INSERT INTO user VALUES(?, ?, ?, ?, ?)
                """
                cursor.execute(query, (info['user_id'], info['chat_id'], info['first_name'], info['gender'],
                                        info['age']))
                connection.commit()
                print('done')
                return 'done'
            except Exception as e:
                print(e)
                return e

    def add_admin(self, info : dict):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """
                INSERT TO admins VALUES(?, ?, ?, ?)
                """
                cursor.execute(query, (info['user_id'], info['chat_id'], info['first_name'], info['gender']))
                connection.commit()
                return 'done'
            except Exception as e:
                print(e)
                return e

    def delete_user(self, user_id):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """UPDATE user SET first_name =? WHERE user_id=?"""
                cursor.execute(query, ('unknow',user_id))
                connection.commit()
                return 'done'
            except Exception as e:
                print(e)
                return e

    def delete_admin(self, user_id):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """DELETE FROM admins WHERE user_id=?"""
                cursor.execute(query, (user_id,))
                connection.commit()
                return 'done'
            except Exception as e:
                print(e)
                return e
            
    def update_user(self, user_id, info : dict):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                for i,k in info.items():
                    query = f"UPDATE user SET {i} = ? WHERE user_id = ?"
                    cursor.execute(query, (k, user_id))
                return 'done'
            except Exception as e:
                print(e)
                return e
                
    def check_admin(self, user_id):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """SELECT user_id FROM admins"""
                res = cursor.execute(query).fetchall()
                print(f'res: {res}')
                if user_id in res:
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
                return e
            
    def check_user(self, user_id):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """SELECT user_id FROM user"""
                res = cursor.execute(query).fetchall()
                user_id = (user_id,)
                print(res)
                if user_id in res:
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
                return e
    
    def get_all_users(self):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """SELECT * FROM user"""
                res = cursor.execute(query).fetchall()
                return res
            except Exception as e:
                print(e)

    def get_all_admin(self):
        with sqlite3.connect('unknow.db') as connection:
            try:
                cursor = connection.cursor()
                query = """SELECT * FROM admins"""
                res = cursor.execute(query).fetchall()
                return res
            except Exception as e:
                print(e)

if __name__ == '__main__':
    data = Data()
    res = data.get_info(6353815381)
    print(res[0])