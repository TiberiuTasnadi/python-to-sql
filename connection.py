def connectDB():
    try:
        dic={
            "host":'localhost',
            #host=place where is the database
            "user":'root',
            #user = user that has privileges on the db
            "passwd": 'sector7g',
            #password of the user
        }
        db = MySQLdb.connect(**dic)

        return db

    except MySQLdb.Error, e:
    #Errors
        print e
