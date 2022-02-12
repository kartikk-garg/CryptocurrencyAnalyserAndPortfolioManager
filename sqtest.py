import sqlite3

# con = sqlite3.connect('data.db')
# cur = con.cursor()

# cur.execute('''CREATE TABLE Coins
#                (Date text, Symbol text, Name text, qty real, price real)''')

# cur.execute("INSERT INTO Coins VALUES ('2022-01-01','BTC','Bitcoin',1,40450)")


def add(date, name, symbol, quantity, price):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO Coins VALUES ({date},{symbol},{name},{quantity},{price})")

def read():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Coins")

    rows = cur.fetchall()
    print(rows)

