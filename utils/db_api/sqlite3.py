import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

###################################### Users ######################################
    
    def add_user(self, user_id: int, full_name: str, referral: str, number: str = 'none', ball: str = '0' ):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO users(user_id, full_name, referral, number, ball) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, full_name, referral, number,  ball), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def top(self):
        sql = """
        SELECT * FROM users ORDER BY ball > 0 DESC LIMIT 30;
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, user_id):
        result = self.execute(
            sql = "SELECT * FROM users WHERE user_id=?",
            parameters=(user_id,),
            fetchall=True
        )   
        return result
    
    def get_invited(self, referral):
        return self.execute("SELECT referral FROM users WHERE referral=?", (referral,), fetchall=True)
    
    def select_number(self, user_id):
        result = self.execute(
            sql = "SELECT number FROM users WHERE user_id=?",
            parameters=(user_id,),
            fetchall=True
        )
        return result


    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)
    
    def update_number(self, number, user_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE users SET number=? WHERE user_id=?
        """
        return self.execute(sql, parameters=(number, user_id), commit=True)

    def update_ball(self, ball, user_id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE users SET ball = (ball + ?) WHERE user_id=?
        """
        return self.execute(sql, parameters=(ball, user_id), commit=True)

    def update_all_balls(self):
        sql = """
        UPDATE users SET ball = 0
        """
        return self.execute(sql, commit=True)

    def delete_users(self):
        self.execute("DELETE FROM users WHERE TRUE", commit=True)

    def deduct_balance(self, user_id, amount_spent):
        # SQL to deduct balance from user's account
        sql = """
        UPDATE users SET ball = (ball - ?) WHERE user_id=?
        """
        return self.execute(sql, parameters=(amount_spent, user_id), commit=True)


    
    
    
###################################### Kanal vs File ######################################

    def add_channel(self, channel: str):
        sql = """
            INSERT INTO Channel(channel) VALUES(?)
            """
        self.execute(sql, parameters=(channel,), commit=True)

    def check_channel(self, channel):
        return self.execute("SELECT channel FROM Channel WHERE channel=?", (channel,), fetchone=True)

    def select_channels(self):
        return self.execute("SELECT * FROM Channel WHERE TRUE",fetchall=True)

    def select_all_channels(self):
        sql = """
        SELECT * FROM Channel WHERE TRUE
        """
        return self.execute(sql, fetchall=True)

    def select_all_channel(self):
        sql = """
        SELECT * FROM Channel
        """
        return self.execute(sql, fetchall=True)

    def add_file(self, file_id: str, caption: str, ids: str):
        sql = """
               INSERT INTO files(file_id, caption, ids) VALUES(?, ?, ?)
               """
        self.execute(sql, parameters=(file_id, caption, ids), commit=True)

    def select_video(self, ids):
        result = self.execute(
            sql="SELECT * FROM files WHERE ids=?",
            parameters=(ids,),
            fetchall=True
        )
        return result

    def delete_channel(self, channel):
        return self.execute("DELETE FROM Channel WHERE channel=?", (channel,), commit=True)

###################################### Sovga ######################################

    def add_sovga(self, text: str):
        sql = """
               INSERT INTO sovga(text) VALUES(?)
               """
        self.execute(sql, parameters=(text,), commit=True)

    def select_all_sovga(self):
        sql = """
        SELECT * FROM sovga
        """
        return self.execute(sql, fetchall=True)

    def select_sovga(self, id):
        result = self.execute(
            sql="SELECT * FROM sovga WHERE id=?",
            parameters=(id,),
            fetchall=True
        )
        return result

    def update_sovga(self, text, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE sovga SET text = ? WHERE id=?
        """
        return self.execute(sql, parameters=(text, id), commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
