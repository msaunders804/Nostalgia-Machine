from PIL import Image
import sqlite3
from sqlite3 import Error

def create_conn(db_file):
    '''
    creating a database connection
    this will open a new db if none exsists
    and reworks one that does
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_project(conn):
    '''
    create a cursor and store images and rgb values
    to a db
    '''
    c = conn.cursor()
    fairly_list = []
    roll_through_images(fairly_list)
    print(fairly_list)
    c.execute('DROP TABLE IF EXISTS fairly_rgb')
    c.execute('CREATE TABLE fairly_rgb (image name TEXT, r value INT, g value INT, b value INT)')
    c.executemany('INSERT INTO fairly_rgb VALUES (?,?,?,?)', fairly_list)
    conn.commit()
    conn.close()

def find_rgb(image):
    '''
    find the rgb value of a image
    param -> image
    '''
    rgb_pix = list(image.getdata())
    r_average = 0
    g_average = 0
    b_average = 0
    counter = 0
    for item in rgb_pix:
        r_average += item[0]
        g_average += item[1]
        b_average += item[2]
        counter += 1
    r = r_average//counter
    g = g_average//counter
    b = b_average//counter

    #spongebob_list.append((image,temp_rgb))
    return (r,g,b)

def roll_through_images(fairly_list):
    '''
    roll through a folder
    to send images to find_rgb
    param -> folder?
    param -> spongebob_list
    '''
    '''
    goal here to find length of a folder and run a for
    loop over every image and finding the rgb value and storing them into a list
    '''
    import os

    path = os.getcwd()
    os.chdir("Fairly_testpictures")

    for i in range(1,724):
        i = str(i)
        sourcename = "img_"+i+".jpg"
        try:
            image = Image.open(sourcename)
            r,g,b = find_rgb(image)
            fairly_list.append((sourcename, r,g,b))
        except:
            print(i, "no good")
        

if __name__ == '__main__':
    create_project(create_conn(r'images_rgb.db'))

