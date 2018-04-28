import psycopg2

CONN_INFO = {
    'host': '127.0.0.1',
    'port': 5432,
    'user': 'postgres',
    'pass': 'root',
}

CONN_STR = 'host={host} port={port} user={user} password={pass}'.format(**CONN_INFO)

class DB:
    def __init__(self, verbose=True, conn_config=CONN_STR):
        self.verbose = verbose
        self.conn_config = conn_config
        print("DB config [ %s ]" % self.conn_config)
        print("verbose = %s" % str(self.verbose))
        

    def query_dml(self, query):
        result = []
        try:
            conn = psycopg2.connect(self.conn_config)
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if self.verbose:
                print(rows)
            cols = tuple([d[0] for d in cursor.description])
            for row in rows:
                dic = dict(zip(cols, row))
                result.append(dic)
        except Exception as err:
            if self.verbose:
                print(err)
            return -1
        finally:
            cursor.close()
            conn.commit()
            conn.close()
            return result

    def query_ddl(self, query):
        try:
            conn = psycopg2.connect(self.conn_config)
            cursor = conn.cursor()
            cursor.execute(query)
            if self.verbose:
                print("everything ok")
        except Exception as err:
            if self.verbose:
                print(err)
            return -1
        finally:
            cursor.close()
            conn.commit()
            conn.close()
            return 0
        

def test_DB():
    db = DB(verbose=True)
    db.query_ddl("create table personas(id int, nombre text)")
    db.query_dml("insert into personas(id, nombre) values(594930345, 'Jose Perez')")
    db.query_dml("insert into personas(id, nombre) values(845939394, 'Luis Varquero')")
    db.query_dml("insert into personas(id, nombre) values(858588383, 'Pedro Sanchez')")
    rest = db.query_dml("select * from personas")

    print(rest)
    for e in rest:
        print(e)








