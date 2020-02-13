from PIL import Image



'''
we are going to cut up the image into 50x50 pixel pieces so
we are going to insure that the size of the image has a width and
height that are divisiable by 50 to the nearest
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
def break_into_tiles(image):
    width, height = image.size
    for upper in range(height // 50):
        print('hi')
        for left in range(width // 50):
            print('bye')
            (left,upper,right,lower) = (left*50,upper*50,left*50+50,upper*50+50)
            temp_tile = image.crop((left,upper,right,lower))
            #collect RGB values and put them into a 2-D array that we will pass through the params as well
            rgb = temp_tile.convert('RGB')

def main():

    image = Image.open("test.jpg")      #simple test will need to ask user for picture
    image = resize(image)
    width, height = image.size
    print(height)
    print(width)
    break_into_tiles(image)
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

if __name__ == '__main__':
    main()
