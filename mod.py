import sys
import datetime
import random
import dataset

class Konpeki:
    def __init__(self):
        now_second = datetime.datetime.now()
        random.seed(now_second)
        self.id = random.randint(0, 199)

    def get_url(self):
        try:
            table = self.__db()
            res = table.find_one(id = self.id)
            if res is None:
                sys.exit(1)
            return res["url"]
        except:
            return "NG"

    def __db(self):
        DBMS = "dbms"
        USER = "user_name"
        PASS = "password"
        HOST = "host"
        DB = "db_name"
        TABLE = "table"
        db = dataset.connect("{0}://{1}:{2}@{3}/{4}".format(DBMS, USER, PASS, HOST, DB))
        table = db[TABLE]
        return table
