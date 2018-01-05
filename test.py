import pandas as pd
import heapq
import cx_Oracle


try:
    db = cx_Oracle.connect('test/123456@133.133.30.14/xe')
    cr = db.cursor()
    sql = "select * from \"asda\""
    cr.execute(sql)
    rs = cr.fetchall()
    zz = pd.DataFrame(rs, columns=['username', 'password'])
    print(zz)
except:
    print('error')
    raise
finally:
    cr.close()
    db.close()
