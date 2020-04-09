import resize_script

#change the length of the for loop to number of images in file that need resizing
for i in range(0, 100):
    i =str(i)
    sourcename= "img_"+i+".jpg"
    resize_script.resize_source(sourcename)
