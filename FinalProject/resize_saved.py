import resize_script
import os

path = os.getcwd()
os.chdir("testpictures")

for i in range(724,813):
    i = str(i)
    sourcename = "img_"+i+".jpg"
    #resize_script.resize_source(sourcename)
    try:
        resize_script.resize_source(sourcename)
    except:
        os.remove(sourcename)
