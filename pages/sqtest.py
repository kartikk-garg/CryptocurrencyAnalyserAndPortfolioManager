import sqlite3

def createDbAndTable():
    con = sqlite3.connect('data.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE Coins
                (Date text, Symbol text, Name text, qty real, price real)''')

    con.commit()
    con.close()


def add(date, name, symbol, quantity, price):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    
    rows = read()
    con.commit()
    for row in rows:
        if symbol in row:
            qtyold = row[3]
            priceold = row[4]

            newqty = qtyold + quantity
            newprice = (qtyold*priceold + quantity*price)/(qtyold + quantity)
            query = f"""Update Coins set qty ={newqty} where  symbol = {symbol}"""

    else:
        cur.execute(f"INSERT INTO Coins VALUES ('{date}','{symbol}','{name}',{quantity},{price})")
    
    con.commit()
    con.close()

def read():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Coins")
    con.commit()
    
    rows = cur.fetchall()
    con.close()
    for row in rows:
        print(row)

    return rows

# createDbAndTable()
# add('2022-01-01','BTC','Bitcoin',1.0,50.20)
# data = read()
    

