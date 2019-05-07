import os, sys, mysql.connector

photoFormats = ['.jpg', '.png', '.tiff', '.bmp', '.pdf']

def insert_photo(cmd, photo):
    print("I need some more info before you %s, %s").format(cmd.upper(), photo.upper())
    Speed = input("What was the Shutter Speed in seconds? (eg. 1/4)")
    Film = input("What type of film was used?")
    f_stop = input("What was the Shutter Speed? (eg. f/2.8)")
    Color =  input("Is this a color photo? (Y/n)")

    query = """
         INSERT INTO Photo(PhotoID, Speed, Film, `F-Stop`, Color, Resolution, Price, `Date`, TransID, PName, PBDate)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)
         ON DUPLICATE KEY UPDATE
         PhotoID=%s, Speed=%s, Film=%s, `F-Stop`=%s, Color=%s, Resolution=%s, Price=%s, `Date`=%s, TransID=%s, PName=%s, PBDate=%s;
     """
    cursor.execute(query, (PhotoID, Speed, Film, f_stop, Color, Resolution, Price, `Date`, TransID, PName, PBDate))


def remove_photo():
    query = """
         SELECT PhotoID, PName
         FROM Photo 
         Order by PhotoID;
     """
    print("I need some more info before you %s, %s").format(cmd, photo)
    pID = input("What is the photoID for the photo you wish to remove?")

    query = """
         DELETE FROM `Photo`
         Where PhotoID=%s;
     """
    try:
        cursor.execute(pID)
    except:
        print("Err: Invalid selection, try again")
        remove_photo(cmd,photo)

    print("Photo removed successfully.")

# app [insert/update/remove] [photo]
cmd, photo = sys.argv[1:]

if photo[-4:] not in photoFormats:
    print("Err: Unsupported Photo Type")
    sys.exit()

try:
    database = mysql.connector.connect(host="sql.njit.edu", user="md537", password="freshen77", database="md537"
    )
except mysql.connector.Error as err:
    print(err)
    database.close()
    sys.exit()

cursor = database.cursor()

if(cmd.lower() == "update"):
    insert_photo(cmd, photo)
if(cmd.lower() == "delete"):
    remove_photo(cmd, photo)