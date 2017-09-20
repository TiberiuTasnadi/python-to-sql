import MySQLdb
from openpyxl import load_workbook



"""
    Creation of the main database and all the tables
"""
def createDatabase():
    db=connectDB()

    cur = db.cursor()

    cur.execute("CREATE DATABASE software3d;")

    cur.execute("""CREATE TABLE software3d.printers (
                    brand varchar(20),
                    model varchar(20),
                    printAreaX int,
                    printAreaY int,
                    printAreaZ int,
                    speedMin int,
                    speedMax int,
                    resMax int,
                    resMin int,
                    numberNozzles int,
                    diameterNozzles float,
                    tempMaxNozzles int,
                    tempMinNozzles int,
                    heatedBedMax int,
                    heatedBedMin int,
                    PRIMARY KEY ( brand, model )
    );""")
