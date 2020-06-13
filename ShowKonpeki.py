import datetime
import random
import csv

"""
メモ
・postgresql と dataset のテスト
・heroku でアプリケーションを立てる
・line api の準備
・postgresql の準備（heroku）
・heroku へのデプロイ
"""

def ShowKonpeki():
    f = open("konpeki_no_sora.csv", "r")
    reader = csv.reader(f)
    header = next(reader)
    konpeki_list = [row for row in reader]

    now_second = datetime.datetime.now()
    random.seed(now_second)
    num = random.randint(0, 199)
    print(konpeki_list[num][1])

    f.close()

if __name__ == "__main__":
    ShowKonpeki()