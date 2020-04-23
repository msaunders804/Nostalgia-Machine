from PIL import Image
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        
    return conn

def query_rgb_values(conn,current_tile):
    c = conn.cursor()
    c.execute('SELECT * FROM spongebob_rgb')

    rows = c.fetchall()

    for row in rows:
        print(row) #test//remove
        track_min(row,current_tile)
        
def track_min(row,current_tile)
    '''
    find the value that is the least meaning
    it is the closest in distance to the portion of the
    image we want to replace
    '''
    '''
    sqrt((r2-r1)^2 + (g2-g1)^2 + (b2-b1^2))
    is this less then it currently is?
    this is the new image we use
    '''

if __name__ == '__main__':
    query_rgb_values(create_connection(r'images_rgb.db')
