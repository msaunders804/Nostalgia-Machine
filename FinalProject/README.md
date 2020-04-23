# Nostalgia-Machine
COP4930 Python Project

#Team Use for start
Things to consider:
  What background image will we default to if they choose to play snake witout using image creator;
  making opiton to only make image and not play game?
  
  Gen. Outline (what needs to be done):
    GUI - Megan;
    Photomosaic Logic - Bryan;
    Script to get and store photos from tv shows offline;
    Build database to store these;
    Script to auto resize images to be squares for photmosaic;
    Snake logic;
    
Overall idea:
  Gui will hae menu that allows play to create new image or play snake on default;
  User inputs image;
  Create Photomosaic of images of selected show from offline (in DB);
  Inverse colors on photomosaic image so that we can have the snake be that color;
  Set image as background of snake game;
  Play snake game; 
  Return to menu;
  
  #How to run write up
  1. Run scrape.py for each movie you would like
  2. Run resize_saved.py to resize all the scraped images
  3. Run push_source_im_to_sql_w_rbg.py for each more to store the resized images into the database
  4. Ensure you have all your scripts and images in the same file
  5. Run nostalgia_machine.py and HAVE FUN!
  
