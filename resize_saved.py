import resize_script
import os

path = os.getcwd()
os.chdir("testpictures")

for i in range(0,100):
    i = str(i)
    sourcename = "img_"+i+".jpg"
    try:
        resize_script.resize_source(sourcename)
    except:
        os.remove(sourcename)
