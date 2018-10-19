
import cx_Oracle

CONN_INFO = {
    'host': '127.0.0.1',
    'port': 1521,
    'user': 'sys',
    'pass': 'manager',
}

CONN_STR = '{user}/{pass}@{host}:{port}'.format(**CONN_INFO)

class DB:
    def __init__(self):
        self.conn = cx_Oracle.connect(CONN_STR, mode = cx_Oracle.SYSDBA)

    def query_dml(self, query, params={}):
        cursor = self.conn.cursor()
        rows = cursor.execute(query, params).fetchall()
        cols = tuple([d[0] for d in cursor.description])
        result = []
        for row in rows:
            dic = dict(zip(cols, row))
            result.append(dic)
        cursor.close()
        return result

    def query_ddl(self, query, params={}):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, params)
            print("everything ok")
        except cx_Oracle.Error as err:
            print(err)
            return -1
        return 0

def test_oracle():

    QUERY_DML = '''
                select * 
                    from aviones
                '''

    QUERY_DDL = '''
                create table personas(
                    id int
                    nombre varchar(30)
                )
                '''

    db = DB()
    result = db.query_mdl(QUERY_MDL)
    print(result)
    for e in result:
        print(e)
