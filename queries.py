import sys, os, mysql.connector

def sql1():
    query = """
         SELECT * 
         FROM Transaction T, Customer C 
         WHERE C.LoginName=T.LoginName 
         GROUP BY C.CName HAVING AVG(T.TotalAmount)>100;
     """
    cursor.execute(query)

def sql2():
    query = """
        SELECT PhotoID FROM Photo WHERE TransID IS NULL;
    """
    cursor.execute(query)

def sql3():
    query = """
        SELECT C.CName 
        FROM Transaction T, Photo P, Customer C, Models M 
        WHERE C.LoginName=T.LoginName AND T.TransID=P.TransID 
        AND P.PhotoID=M.PhotoID AND M.MName='Jasmine G';
    """
    cursor.execute(query)

def sql4():
    query = """
        SELECT P.PName 
        FROM Photographer P, Influences I 
        WHERE P.PName=I.EPName 
        AND P.PBDate=I.EPBDate AND P.PNationality='United States';
    """
    cursor.execute(query)

def sql5():
    query = """
        SELECT P.PName 
        FROM Photographer P, Photo A, Models M 
        WHERE P.PName=A.PName AND P.PBDate=A.PBDate AND A.PhotoID=M.PhotoID;
    """
    cursor.execute(query)

def sql6():
    query = """
        SELECT P.TransID 
        from Photo as P 
        INNER JOIN Transaction as T on P.TransID = T.TransID 
        having COUNT(P.TransID > 3);
    """
    cursor.execute(query)

def sql7():
    query = """
        SELECT M.MName 
        FROM Models M, Photographer P, Photo A 
        WHERE M.PhotoID=A.PhotoID AND A.PName=P.PName 
        AND A.PBDate=P.PBDate AND P.PName='Joan Chaser';
    """
    cursor.execute(query)

def sql8():
    query = """
        SELECT P.PName 
        FROM Photographer P, Photo A 
        WHERE P.PNAME=A.PName AND P.PBDate=A.PBDate 
        ORDER BY A.Price DESC;
    """
    cursor.execute(query)

def sql9():
    query = """
        DELETE FROM Photo WHERE PhotoID='12';
    """
    cursor.execute(query)

def sql10():
    query = """
        UPDATE Photo SET PName='Maxwell Smith', PBDate='1967-02-06' 
        WHERE PhotoID='12'; 
    """
    cursor.execute(query)

def sql11():
    query = """
        SELECT SUM(T.TotalAmount) AS "Total Sales" 
        FROM Customer C, Transaction T WHERE C.LoginName=T.LoginName 
        AND C.LoginName='Jo';
    """
    cursor.execute(query)

def sql12():
    query = """
        SELECT SUM(DISTINCT T.TotalAmount) AS "Total Sales", P.PName
        FROM Transaction T, Photo A, Photographer P 
        WHERE T.TransID=A.TransID AND P.PName=A.PName AND P.PBDate=A.PBDate 
        GROUP BY P.PName;
    """
    cursor.execute(query)

def sql13():
    query = """
        SELECT SUM(T.TotalAmount) AS "Total Sales Type" 
        FROM Models M, Transaction T, Photo P 
        WHERE M.PhotoID=P.PhotoID AND P.TransID=T.TransID;
    """
    cursor.execute(query)

def sql14():
    query = """
        SELECT SUM(T.TotalAmount) AS "Total Sales", T.TDate
        FROM Transaction T, Photo A, Photographer P 
        WHERE T.TransID=A.TransID AND P.PName=A.PName 
        AND P.PBDate=A.PBDate GROUP BY T.TDate;
    """
    cursor.execute(query)
# app [1-14]
cmd = str(sys.argv[1])

try:
    database = mysql.connector.connect(host="sql.njit.edu", user="md537", password="freshen77", database="md537"
    )
except mysql.connector.Error as err:
    print(err)
    database.close()
    sys.exit()

cursor = database.cursor()

if(cmd.lower() == "1"):
    sql1()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "2"):
    sql2()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "3"):
    sql3()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "4"):
    sql4()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "5"):
    sql5()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "6"):
    sql6()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "7"):
    sql7()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "8"):
    sql8()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "9"):
    sql9()

elif(cmd.lower() == "10"):
    sql10()

elif(cmd.lower() == "11"):
    sql11()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "12"):
    sql12()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "13"):
    sql13()
    data = cursor.fetchall()

    for row in data :
        print (row)
elif(cmd.lower() == "14"):
    sql14()
    data = cursor.fetchall()

    for row in data :
        print (row)
else:
    print("Please enter a command.")
    print("Usage: queries.py [1-14], 0 to exit.")