'''resize script'''

from PIL import Image

'''
if we pass an image it will take the size of the and shrink to a sqaure
ex: 1200x500 -> 500x500
ex: 400x450  -> 400x400
'''

def resize_source(image_name):
    image = Image.open(image_name)
    width,height = image.size
    image.show()
    if width < height:
        height = width 
    elif height < width:
        width = height
    image = image.resize((width,height))
    image.save(image_name)
