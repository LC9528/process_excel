import MySQLdb
import math
import roundUp as rd

class sql:
    
    def __init__(self):
        self.db = MySQLdb.connect(host=localhost,user=username, passwd=password, db=dbname, charset="utf8")
        self.cursor = self.db.cursor()

#insert rate to db
    def inTCMUR(self, TUMUR_rate, year, wk, region, country, product):
        sql = "INSERT INTO TCMUR (YEAR, WEEK, REGION, COUNTRY, PRODUCT_GROUP, TCMUR_RATE)VALUES (%s, %s, %s, %s, %s, %s)"
        collectTCMUR = []
        for i in range(len(TUMUR_rate)):
            if math.isnan(TUMUR_rate[i]):
                continue
            else:
                collectTCMUR.append((int(year), int(wk) , region , country[i], product, rd.round_up(TUMUR_rate[i],2)))
        self.cursor.executemany(sql, collectTCMUR)
        self.db.commit()

    def inTCMURTotal(self, TCMUR_total_rate, year, wk, region, country, product):
        sql = ("INSERT INTO TCMUR (YEAR, WEEK, REGION, COUNTRY, PRODUCT_GROUP, TCMUR_RATE)VALUES (%s, %s, '%s', '%s', %s, %s)"
                % (int(year), int(wk) , region , country, product, rd.round_up(TCMUR_total_rate,2)))
        self.cursor.execute(sql)
        self.db.commit()
        self.cursor.close()
        self.db.close()   





