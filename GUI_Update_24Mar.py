from tkinter import *
from tkinter import filedialog
import random
from threading import Thread

page = Tk()

############################################################################################################################################################################################################
                                                                                    #Mosaic Input Screen
############################################################################################################################################################################################################
def inPage_thread():
    Thread(target= InImagePage).start()
def InImagePage():
    subpage = Toplevel(page)
    #create file browse that allows users to input image file
    def Upload(event = None):
        filename = filedialog.askopenfilename()
        choiceFile = filename
    Button(subpage,text = 'Select Your Image', command = Upload).place(relx = 0.47, rely = 0.05)
    
    subpage.configure(bg = '#1b8f1b')
    subpage.geometry('1500x1500')
    Label(subpage, text = "Select your TV show:", bg = '#1b8f1b', font = 'fixedsys').place(relx = 0.45, rely = 0.1)
    var = IntVar()
    

    def choice():
        show = var.get() #this value will be used to pass into mosaic

    R1 = Radiobutton(subpage, text = 'Spongebob Squarepants', bg = '#ff7f27',highlightbackground = "#ff7f27", variable = var, value = 1, font = 'fixedsys', command = choice).place(relx =0.45, rely = 0.15)
    R2 = Radiobutton(subpage, text = 'Fairly Odd Parents', bg = '#ff7f27', highlightbackground = '#ff7f27', variable = var, value = 2, font = 'fixedsys', command = choice).place(relx = 0.45, rely = 0.18)
    R3 = Radiobutton(subpage, text = 'Danny Phantom', bg = '#ff7f27',highlightbackground = '#ff7f27',variable = var, value = 3, font = 'fixedsys', command = choice).place(relx = 0.45, rely = 0.21)
    R4 = Radiobutton(subpage, text = 'Rocket Power', bg = '#ff7f27',highlightbackground = '#ff7f27', variable = var, value = 4, font = 'fixedsys', command = choice) .place(relx = 0.45, rely = 0.24)

    #use command to run script to create photomosaic passing in inputted file and have it return then display on this screen below the choice

    Label(subpage, text = "Here is your photomosaic: ", bg = '#1b8f1b', font = 'fixedsys').place(relx = 0.45, rely = 0.3)
    c = random.randint(0,8)
    mylines = []
    with open('facts.txt', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)
    Label(subpage, text = 'Did you know:\n', bg = '#1b8f1b', font = 'fixedsys').place(relx = 0.47, rely = 0.35)
    fact = Text(subpage, relief = FLAT, width = 35, wrap = WORD, bg = '#1b8f1b', font = 'fixedsys', highlightbackground = '#1b8f1b')
    fact.insert(INSERT, mylines[c])
    fact.config(state = DISABLED)
    fact.place(relx = 0.43, rely = 0.4)

    #Design features for subpage
    splat = PhotoImage(file='splat2.png')
    splatlab =Label(subpage, image = splat, bg = '#1b8f1b')
    splatlab.place(relx = 0.65, rely = 0.13) 
    splatlab.image = splat

    def refresh_fact():
        fact.config(state = NORMAL)
        c = random.randint(0,8)
        fact.delete('1.0', END)
        fact.insert(INSERT,mylines[c]) 
        fact.config(state = DISABLED)
        fact.place(relx = 0.43, rely = 0.4)
        fact.after(20000, refresh_fact)

    fact.after(20000, refresh_fact)
    
    def close():
        subpage.destroy()

    Button(subpage, text = 'Return to main menu', width =45, command = close).place(relx = 0.7, rely = 0.8)
    Button(subpage, text = 'Play snake with your photomosaic', width = 45, command = snake).place(relx = 0.2, rely = 0.8)
    
############################################################################################################################################################################################################
                                                                                        #Import Snake code to run
###########################################################################################################################################################################################################
def snake():
    import snake.py

############################################################################################################################################################################################################
                                                                                        #Import Login code to run
############################################################################################################################################################################################################
def login():
    login = Toplevel(page)
    label = Label(login, text = "login")
    label.pack()
    login.geometry('800x800')
############################################################################################################################################################################################################
                                                                                        #exit page
############################################################################################################################################################################################################
def exit():
    page.destroy()

############################################################################################################################################################################################################
                                                                                        #Main page program
############################################################################################################################################################################################################
logo = PhotoImage(file = "NMLogo.png")
introPic = PhotoImage(file = "titleNick.png")
slime = PhotoImage(file = "slime2.png")
Label(page, image = logo, bg = '#ff7f27').place(relx = 0.33, rely = 0.3)
Label(page, image = slime, bg = '#ff7f27').place(relx = 0, rely = 0)
Label(page, image = slime, bg = '#ff7f27').place(relx = 0.63, rely = 0)
Label (page, image=introPic, bg="#58ca00") .place(relx = 0.1, rely = 0.)
Label(page, text = "Created by: Byan Coleman, Megan Saunders, Matt Aparte, Oliva Wright c.2020", bg = '#ff7f27').place(relx=0,rely=0.97)

fairly = PhotoImage(file = "fairly.png")
danny = PhotoImage(file = "Danny.png")
sponge = PhotoImage(file = "Sponge.png")
rocket = PhotoImage(file = "rocket.png")

Label(page, image = fairly, bg = '#ff7f27').place(relx = 0.1, rely = 0.5)
Label(page, image = danny, bg = '#ff7f27').place(relx = 0.6, rely = 0.2)
Label(page, image = sponge, bg = '#ff7f27').place(relx = 0.2, rely = 0.2)
Label(page, image = rocket, bg = '#ff7f27').place(relx = 0.7, rely = 0.5)

page.title("Menu")
page.configure(width = 1500, height = 1500, bg = '#ff7f27')

Button(page, text = "Click here to submit your image", width = 45, command = inPage_thread).place(relx=0.2,rely=0.8) 
Button(page, text = "Click here to play snake without custom background", width = 45, command = snake).place(relx = 0.55, rely = 0.8)
Button(page, text = "Login", width = 10, command = login).place(relx = 0.9, rely = 0.08)
Button(page, text = "Exit", width = 10, command = exit).place(relx = 0.9, rely = 0.03)
page.mainloop()
