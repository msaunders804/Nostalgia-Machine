from PIL import Image
import numpy as np
import sqlite3
from sqlite3 import Error
import math
import os

'''
we are going to cut up the image into 50x50 pixel pieces so
we are going to insure that the size of the image has a width and
height that are divisiable by 25 to the nearest
ex:
    124 -> 100
    126 -> 150
'''
def resize(image):
    width, height = image.size
    if width % 50 != 0:
        if width % 50 < 25:
            width = width - width % 50
        else:
            width = width + 50 - width % 50
    if height % 50 != 0:
        if height % 50 < 25:
            height = height - height % 50
        else:
            height = height + 50 - height % 50
    return image.resize((width,height))

'''
breaks the image into tiles that way we can collect the RGB values and put them into a 
2-D array that will eventually be used to create our photomosaic
'''
def break_into_tiles(image,rgb_ave):
    width, height = image.size
    for upp in range(height // 25):
        for lef in range(width // 25):
            (left,upper,right,lower) = (lef*25,upp*25,lef*25+25,upp*25+25)
            temp_tile = image.crop((left,upper,right,lower))
            rgb_pix = list(temp_tile.getdata())
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
            rgb_ave.append(temp_rgb)

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

    current_min = ['placeholder',100000]

    for row in rows:
        track_min(row,current_tile,current_min)

    return current_min[0]


def track_min(row,current_tile,current_min):
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

    s_red = row[1]
    s_green = row[2]
    s_blue = row[3]
    t_red = current_tile[0]
    t_green = current_tile[1]
    t_blue = current_tile[2]

    result = math.sqrt(math.pow(s_red - t_red, 2) + math.pow(s_green - t_green, 2) + math.pow(s_blue - t_blue, 2))

    if result < current_min[1]:
        current_min[0] = row[0]
        current_min[1] = result


def main(pic):
    rgb_ave = []
    image = Image.open(pic)      #simple test will need to ask user for picture
    image = resize(image)
    width, height = image.size
    break_into_tiles(image,rgb_ave)

    conn = create_connection(r'images_rgb.db')

    new_im = Image.new('RGB',(width,height))
    i = 0
    for upp in range(height // 25):
        for lef in range(width // 25):

            '''
            will need to find the source image here
            by using distance equation again all source image rgb values
            '''
            path = os.getcwd()
            os.chdir("testpictures")

            #script -> finds closest image
            temp_im = Image.open(query_rgb_values(conn,rgb_ave[i]))
            i += 1
            temp_im2 = temp_im.convert('RGB')
            (left,upper,right,lower) = (lef*25,upp*25,lef*25+25,upp*25+25)
            new_im.paste(temp_im2,(left,upper,right,lower))

    new_im.show()
    image.show()

#testing cropping into small pieces, messing around with how the tuple works
'''
rig = 50
low = 50
for upp in range(16):
    for lef in range(16):
        (left,upper,right,lower) = (lef*50,upp*50,rig*lef+50,low*upp+50)
        image2 = image.crop((left,upper,right,lower))
'''
#testing some pillow properties
''''
(left,upper,right,lower) = (0,0,200,200)
image2 = image.crop((left,upper,right,lower))
image2.show()

(left,upper,right,lower) = (200,0,400,200)
image2 = image.crop((left,upper,right,lower))
image2.show()

(left,upper,right,lower) = (400,0,600,200)
image2 = image.crop((left,upper,right,lower))
image2.show()

(left,upper,right,lower) = (600,0,800,200)
image2 = image.crop((left,upper,right,lower))
image2.show()
'''

'''if __name__ == '__main__':
    main()'''
