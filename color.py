#Converts color from one code to another
#Only bewteen Hex & RGB
#Coded by Aman Bhaskar (amanbh2@gmail.com)

from tkinter import *   #imports
import tkinter.font as font
import math

root = Tk() #Main window
root.title("Convert My Color")
root['bg']='#a8dadc'
root.iconbitmap('rainbow.ico')

myFont = font.Font(family='Poppins') #Font used Poppins

#Various labels and boxes
hex_label = Label(root, text="#Hex", font=myFont, bg='#a8dadc',fg='#1d3557')
hex_label.grid(row=0, column=0,pady=5)
hex_box = Entry(root, width=10, borderwidth=0, font=myFont,fg='#353535')
hex_box.grid(row=1,column=0,padx=5,pady=5)

r_label = Label(root, text="R", font=myFont, bg='#a8dadc',fg='#1d3557')
r_label.grid(row=0, column=2,pady=5)
r_box = Entry(root, width=10, borderwidth=0, font=myFont,fg='#353535')
r_box.grid(row=0,column=3,padx=5,pady=5)

g_label = Label(root, text="G", font=myFont, bg='#a8dadc',fg='#1d3557')
g_label.grid(row=1, column=2,pady=5)
g_box = Entry(root, width=10, borderwidth=0, font=myFont,fg='#353535')
g_box.grid(row=1,column=3,padx=5,pady=5)

b_label = Label(root, text="B", font=myFont, bg='#a8dadc',fg='#1d3557')
b_label.grid(row=2, column=2,pady=5)
b_box = Entry(root, width=10, borderwidth=0, font=myFont,fg='#353535')
b_box.grid(row=2,column=3,padx=5,pady=5)

rgb_box = Entry(root, width=10, borderwidth=0, font=myFont,fg='#353535')
rgb_box.grid(row=3,column=1,padx=5,pady=5) #Box to show color

switch=IntVar() #Variable use to determine whether it is HextoRGB or RGBtoHex conversion

def btn_convert():    
    if switch.get()==0:        #HextoRGB conversion
        r_box.delete(0, END)   #Clears existing entries
        g_box.delete(0, END)
        b_box.delete(0, END)
        hex_user=hex_box.get() #Gets entered/existing data from Hex box
        if hex_user[0]=="#":   #If code starts with # it removes it
            hex_user=hex_user[1:]
        R=hex_user[0:2]        #Split hex code for R, G, B values in hexadecimal
        G=hex_user[2:4]
        B=hex_user[4:]
        def myRGB(z):
            def decimal(number): #Converts hexadecimal digits to Decimal digit
                if number == "A" or number == "a":
                    return 10
                if number == "B" or number == "b":
                    return 11
                if number == "C" or number == "c":
                    return 12
                if number == "D" or number == "d":
                    return 13
                if number == "E" or number == "e":
                    return 14
                if number == "F" or number == "f":
                    return 15
                else:
                    return int(number)
            num1=decimal(z[0])
            num2=decimal(z[1])
            return num1*16 + num2 #Convert Hexadecimal values to Decimal values
        
        r_box.insert(0, f"{myRGB(R)}") #Print values of R,G,B
        g_box.insert(0, f"{myRGB(G)}")
        b_box.insert(0, f"{myRGB(B)}")    
        
        color=hex_box.get()
        if color[0]!="#":
            color=f"#{color}"
        rgb_box.configure(bg=f'{color}') #Shows color
    
    if switch.get()==1:        #RGBtoHex conversion
        hex_box.delete(0, END) #Deletes existing data in Hex box
        
        r=int(r_box.get())     #Gets R,G,B values in decimal
        g=int(g_box.get())
        b=int(b_box.get())

        def hex_digit(y):      #Converts decimal digits to hexadecimal digits
            if y<10:
                return y
            else:
                if y==10:
                    return "A"
                if y==11:
                    return "B"
                if y==12:
                    return "C"
                if y==13:
                    return "D"
                if y==14:
                    return "E"
                if y==15:
                    return "F"

        def myhex(x):           #converts decimal to hexadecimal
            h1=math.floor(x/16)
            h2=x%16
            c1=hex_digit(h1)
            c2=hex_digit(h2)
            return f"{c1}{c2}"
                                #Insert Hex color code in hexbox with '#'
        hex_box.insert(0, f"#{myhex(r)}{myhex(g)}{myhex(b)}")
        
        color=hex_box.get()     #Shows color in rgb_box
        rgb_box.configure(bg=f'{color}')

check = Checkbutton(root, text="RGBtoHex",variable=switch) #Checkbutton use to change conversion direction
check.configure(bg='#a8dadc',fg='#1d3557', borderwidth=0,activebackground='#a8dadc', activeforeground='#1d3557')
check.grid(row=2, column=1)

btn_convert=Button(root, text="CONVERT", padx=5,pady=5,command=btn_convert) #Convert Button
btn_convert.configure(fg='#353535', borderwidth=1, font=myFont, bg='#f6bd60', activebackground='#ffffff')
btn_convert.grid(row=1, column=1)


footer1 = Label(root, text="© Aman Bhaskar", font=myFont, bg='#a8dadc',fg='#1d3557')
footer1.grid(row=5, columnspan=4) #watermark

root.mainloop() #end