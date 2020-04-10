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
        conn = sqlite4.connect(db_file)
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
    spongebob_list = []
    #roll_through_images(folder?,spongebob_list)
    c.execute('INSERT INTO spongebob_rgb VALUE (?,?)', spongebob_list)

def find_rgb(image,spongebob_list):
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
    temp_rgb = (r_average//counter,g_average//counter,b_average//counter)
    spongebob_list.append((image,temp_rgb))


def roll_through_images():
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


if __name__ == '__main__':
    create_project(create_conn(r'images_rgb.db'))

