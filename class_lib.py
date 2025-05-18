import mysql.connector

class Py24db:
    def __init__(self):
        self.__host = "192.168.3.34" # ホスト名
        self.__user = "carpling_system_admin" # ﾕｰｻﾞｰ名
        self.__passwd = "carpling_admin" # パスワード
        self.__db = "" # DB名
        self.__reccnt = 0 # レコード数
        self.__con = mysql.connector.connect(
        host = self.__host,
        user = self.__user,
        passwd = self.__passwd,
        db = self.__db
        )

    def selectSql(self,sql):
        cur = self.__con.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        self.__reccnt = len(res)
        return res

    def excSql(self,sql):
        cur=self.__con.cursor()
        cur.execute(sql)
        self.__con.commit()
        cur.close()
