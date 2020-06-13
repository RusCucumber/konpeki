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
        DBMS = "postgresql"
        USER = "hzgkkbhhfsktbx"
        PASS = "59daad22673fac8ce670d17cefb4db6d8f2e4210f93772d40a1ca4765771e68d"
        HOST = "ec2-3-231-16-122.compute-1.amazonaws.com"
        DB = "d74j7rocds33bn"
        TABLE = "konpeki"
        db = dataset.connect("{0}://{1}:{2}@{3}/{4}".format(DBMS, USER, PASS, HOST, DB))
        table = db[TABLE]
        return table
