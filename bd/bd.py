import psycopg2
from bd.config import host, user, password, db_name

class Database:
    def __init__(self):
        self.conn =  psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name  
        )
        self.conn.autocommit = True 
        self.cur = self.conn.cursor()
        
    def add_tables(self):
        with self.conn:
            self.cur.execute("select * from information_schema.tables where table_name=%s", ('users',))
            if not (bool(self.cur.rowcount)):
                self.cur.execute("""
                    CREATE TABLE users (
                        user_id integer PRIMARY KEY UNIQUE NOT NULL,
                        money integer DEFAULT 0,
                        last_move text DEFAULT 'rest',
                        block_list boolean DEFAULT False)
                    """)
            self.cur.execute("select * from information_schema.tables where table_name=%s", ('bill',))
            if not (bool(self.cur.rowcount)):
                self.cur.execute("""
                    CREATE TABLE bill (
                        user_id integer NOT NULL references users(user_id),
                        user_bill_id integer NOT NULL,
                        bill_status text DEFAULT 'rest',
                        bill_money integer)
                        """)

    def user_exists(self, user_id):  
        with self.conn:
                self.cur.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id, ))
                return(bool(self.cur.fetchone()))
    def add_block_list(self, user_id):
        with self.conn:
                self.cur.execute("UPDATE users SET block_list = True WHERE user_id = %s",(user_id, ))
    def add_user_id(self,user_id):
        with self.conn:
                self.cur.execute("INSERT INTO users (user_id) VALUES (%s)",(user_id, ))
    def add_money(self, money, user_id):
        with self.conn:
                self.cur.execute("UPDATE users SET money = %s WHERE user_id = %s",(money, user_id, ))
    def add_last_move(self, last_move, user_id):
        with self.conn:
                self.cur.execute("UPDATE users SET last_move = %s WHERE user_id = %s",(last_move, user_id, ))
    def get_last_move(self,user_id):
        with self.conn:
                self.cur.execute("SELECT last_move FROM users WHERE user_id = %s", (user_id, ))
                return(self.cur.fetchone()[0])
    def get_money(self,user_id):
        with self.conn:
                self.cur.execute("SELECT money FROM users WHERE user_id = %s", (user_id, ))
                return(self.cur.fetchone()[0])
    def get_users_and_money(self):
        with self.conn:
                self.cur.execute("SELECT user_id, money FROM users ")
                return(self.cur.fetchall())
    def get_block_user(self, user_id):
        with self.conn:
                self.cur.execute("SELECT block_list FROM users WHERE user_id = %s", (user_id, ))
                return(self.cur.fetchone()[0])
    
    def add_bill_values(self, user_id, bill_money, user_bill_id):
        with self.conn:
                self.cur.execute("INSERT INTO bill (user_id, bill_money, user_bill_id) VALUES (%s, %s, %s)",(user_id, bill_money, user_bill_id, ))
    def add_bill_status(self, bill_status, user_bill_id):
        with self.conn:
                self.cur.execute("UPDATE bill SET bill_status = %s WHERE user_bill_id = %s",(bill_status, user_bill_id, ))
    def user_billId_exists(self, user_bill_id):
        with self.conn: 
            self.cur.execute("SELECT user_bill_id FROM bill WHERE user_bill_id = %s", (user_bill_id, ))
            return(bool(self.cur.fetchone()))
    def get_user_bill_id(self,user_id):
        with self.conn:
                self.cur.execute("SELECT user_bill_id FROM bill WHERE user_id = %s", (user_id, ))
                return(self.cur.fetchall()[-1][0])
    def get_bill_status(self,user_bill_id):
        with self.conn:
                self.cur.execute("SELECT bill_status FROM bill WHERE user_bill_id = %s", (user_bill_id, ))
                return(self.cur.fetchone()[0])
    def get_bill_money(self,user_bill_id):
        with self.conn:
                self.cur.execute("SELECT bill_money FROM bill WHERE user_bill_id = %s", (user_bill_id, ))
                return(self.cur.fetchone()[0])