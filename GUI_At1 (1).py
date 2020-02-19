from tkinter import *

page = Tk()

def InImagePage():
    subpage =Toplevel(page)
    label = Label(subpage, text='Image Submission', bg = 'green', font = 25)
    #create file browse that allowsusers to input image file
    subpage.configure(bg = 'green')
    subpage.geometry('1500x1500')
    Label(subpage, text = "Select your TV show:", bg = 'green', font = 40).place(relx = 0.45, rely = 0.1)
    var = IntVar()

    def choice():
        show = var.get() #this value will be used to pass into mosaic

    R1 = Radiobutton(subpage, text = 'Spongebob Squarepants', bg = 'green', variable = var, value = 1, command = choice).place(relx =0.45, rely = 0.15)    
    R2 = Radiobutton(subpage, text = 'Fairly Odd Parents', bg = 'green', variable = var, value = 2, command = choice).place(relx = 0.45, rely = 0.18)
    R3 = Radiobutton(subpage, text = 'Danny Phantom', bg = 'green',variable = var, value = 3, command = choice).place(relx = 0.45, rely = 0.21)
    R4 = Radiobutton(subpage, text = 'Rocket Power', bg = 'green',variable = var, value = 4, command = choice) .place(relx = 0.45, rely = 0.24)
    label.pack()

    #use command to run script to create photomosaic passing in inputted file and have it return then display on this screen below the choice

    Label(subpage, text = "Here is your photomosaic: ", bg = 'green', font = 55).place(relx = 0.45, rely = 0.3)

    def close():
        subpage.destroy()

    Button(subpage, text = 'Return to main menu', width =45, command = close).place(relx = 0.7, rely = 0.8)
    Button(subpage, text = 'Play snake with your photomosaic', width = 45, command = snake).place(relx = 0.2, rely = 0.8)

def snake():
    snakepage = Toplevel(page)
    label = Label(snakepage, text = "Default Snake")
    label.pack()
    snakepage.geometry('1500x1500')

def login():
    login = Toplevel(page)
    label = Label(login, text = "login")
    label.pack()
    login.geometry('800x800')

introPic = PhotoImage(file = "titleNick.png")
slime = PhotoImage(file = "slime2.png")
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

Button(page, text = "Click here to submit your image", width = 45, command = InImagePage).place(relx=0.2,rely=0.8) 
Button(page, text = "Click here to play snake without custom background", width = 45, command = snake).place(relx = 0.6, rely = 0.8)
Button(page, text = "Login", width = 10, command = login).place(relx = 0.9, rely = 0.05)
page.mainloop()
