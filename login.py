'''
The file is intended for adjusting portal users and their passwords and entering new ones
'''
# In code used modules
import sqlite3
import datetime

#work with DB
class Users:
    """This Class:
         def add_new(): added new users and password,
         def check_name(): check for a exist users,
         def update_password(): update existing password
    """
    dataname = sqlite3.connect('users.db')
    variable = dataname.cursor()
    with dataname:
        variable.execute("""
    CREATE TABLE IF NOT EXISTS
    users(
    user str PRIMARY KEY,
    passw str,
    data str,
    renew_data str)
        """)
    dataname.commit()
    dataname.close()
    def __init__(self, user, passw, data, renew_data=None):
        self.user = user
        self.passw = passw
        self.data = data
        self.renew_data = renew_data

#ADD new User and their password
    def add_new(self):
        dataname = sqlite3.connect('users.db')
        variable = dataname.cursor()
        with dataname:
            variable.execute(f"INSERT INTO users (user, passw, data) VALUES ('{self.user}', '{self.passw}', '{self.data}')")
        dataname.commit()
        dataname.close()
        print(f'Vartotojas {self.user} įtrauktas')

#check for existing user name
    def check_name(self):
        dataname = sqlite3.connect('users.db')
        values = dataname.cursor()
        with dataname:
            if values.execute(f"SELECT user FROM users WHERE user=='{self.user}'"):
                print(f'{self.user} vartotojo vardas egzistuoja')
        dataname.close()
#Update for existing password
    def update_password(self, new_password):
        self.new_password = new_password
        dataname = sqlite3.connect('users.db')
        variable = dataname.cursor()
        variable.execute("UPDATE users SET passw = '{self.new_password}', renew_data = '{datetime.datetime.now()}' WHERE user == '{self.user}'")
        print(f'Vartotojo {self.user} slaptažodis atnaujintas')



a = Users('BY00001', 'ABC123', datetime.datetime.now(), None)
#a.add_new()
a.update_password('AAAAAA')



