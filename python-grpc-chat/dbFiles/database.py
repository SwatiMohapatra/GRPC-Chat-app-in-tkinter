import sqlite3

conn = sqlite3.connect("user.db") #error 3
c = conn.cursor()
print("Connection Established")

# create a table user
c.execute(''' CREATE TABLE IF NOT EXISTS user (
            id integer primary key autoincrement,
            username text,
            password text
)
''')
#c.execute(f"DROP TABLE account")

# create account table


# c.execute(f"DELETE FROM account")
conn.commit()
# PRAGMA foreign_keys=on;

#make user class
    
# def get_all():
#     global c
#     c.execute(f"SELECT * FROM user WHERE username='amrit' AND password='123'")
#     rows = c.fetchall()
#     print(len(rows))

def signup(username,password):
    global c
    c.execute(f"SELECT * FROM user WHERE username='{username}'") #error 1. plz refer the last pages of my coding diary to know abt the blunder i was commiting
    if len(c.fetchall()) > 0:
        print("username already exists,  kindly login to continue")
    else:
        c.execute(f'INSERT INTO user (username,password) VALUES ("{username}","{password}")') #error 2
        conn.commit()
        print("New usermade.")

def validate(username,password):
    global c
    print("username"+username)
    c.execute(f"SELECT * FROM user WHERE username='{username}' AND password='{password}'")
    
    if not c.fetchone():
        print("Login Credentials are Wrong.")
        return 0
    else:
        print("Welcome")
        return 1