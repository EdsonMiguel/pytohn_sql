import MySQLdb


host = "localhost"
user= "user_py"
password="[2GD$Qu8"
db = "app_py"
port = 3306


con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)


def select(fields, tables, where=None):
    global c
    query = (f"SELECT {fields} FROM {tables}")    
    if(where):
        query = query + (f' WHERE {where}') 
    c.execute(query)
    return c.fetchall()



def insert(values, table, fields=None):
    global c, con

    query = (f'INSERT INTO {table} ')
    if(fields):
        query = query " ("+ fields +") "
    query = " VALUES " + ",".join(["("+ v + ")" fro v in values])
    
    print(query)
    
