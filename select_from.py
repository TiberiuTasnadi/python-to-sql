def getFromDB(atr,brand,model):
    try:
        db=connectDB()

        #cur is a cursor created to save all the rows
        cur = db.cursor()
        #Now we read each row saved in cur

        cur.execute("SELECT %s FROM software3d.printers WHERE brand='%s' AND model='%s' ;"%(atr, brand, model))

        for row in cur.fetchall():
            return row[0]

        db.commit()
        db.close()
        cur.close()

    except MySQLdb.Error, e:
    #Errors
        if 1054 in e:
            print "The atribute doesn't exist."
        if 1146 in e:
            print "The table doesn't exist."
        if 1045 in e:
            print "Wrong password or the user doesn't exist."
        if 1049 in e:
            print "Database not found."
        else:
            print e
