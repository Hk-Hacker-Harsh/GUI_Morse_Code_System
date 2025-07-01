#Imports
from tkinter import *
from tkinter import messagebox
import winsound                                    #Beep Sound
import time
import webbrowser


#Def
def playmorse():
    for i in morse.get(1.0,END):
        if i == '1':
            winsound.Beep(2500,550)
        elif i == '0':
            winsound.Beep(2500,200)
        elif i == " ":
            time.sleep(2)
        elif i == "/":
            time.sleep(3)
        else:
            break
 
def reset():
    playbut.config(state=DISABLED)
    proceed.config(state=NORMAL, background="white")
    morse.config(state=NORMAL, background="white")
    txt.config(state=NORMAL, background="white")
    morse.delete(1.0,END)
    txt.delete(1.0,END)

def convert():
    playbut.config(state=ACTIVE)
    proceed.config(state=DISABLED, background="lightgrey")
    morse.config(state=DISABLED, background="lightgrey")
    txt.config(state=DISABLED, background="lightgrey")

    if txt.get(1.0,END).strip():
        morseencode()
    elif morse.get(1.0,END).strip():
        morsedecode()
    else:
        messagebox.showinfo(title="Error while Proceeding", message="Both Text and Morse were in Used!!")

def morseencode():                           #Morse Encode
    moralp = txt.get(1.0,END)
    morlst=[]
    morstr=""
    moralp = list(moralp)

    for i in moralp:
        for j in i:
            match j:
                case "A" | "a":
                    morlst.append('01')
                case "B" | "b":
                    morlst.append('1000')
                case "C" | "c":
                    morlst.append('1010')
                case "D" | "d":
                    morlst.append('100')
                case "E" | "e":
                    morlst.append('0')
                case "F" | "f":
                    morlst.append('0010')
                case "G" | "g":
                    morlst.append('110')
                case "H" | "h":
                    morlst.append('0000')
                case "I" | "i":
                    morlst.append('00')
                case "J" | "j":
                    morlst.append('0111')
                case "K" | "k":
                    morlst.append('101')
                case "L" | "l":
                    morlst.append('0100')
                case "M" | "m":
                    morlst.append('11')
                case "N" | "n":
                    morlst.append('10')
                case "O" | "o":
                    morlst.append('111')
                case "P" | "p":
                    morlst.append('0110')
                case "Q" | "q":
                    morlst.append('1101')
                case "R" | "r":
                    morlst.append('010')
                case "S" | "s":
                    morlst.append('000')
                case "T" | "t":
                    morlst.append('1')
                case "U" | "u":
                    morlst.append('001')
                case "V" | "v":
                    morlst.append('0001')
                case "W" | "w":
                    morlst.append('011')
                case "X" | "x":
                    morlst.append('1001')
                case "Y" | "y":
                    morlst.append('1011')
                case "Z" | "z":
                    morlst.append('1100')
                case "0":
                    morlst.append('11111')
                case "1":
                    morlst.append('01111')
                case "2":
                    morlst.append('00111')
                case "3":
                    morlst.append('00011')
                case "4":
                    morlst.append('00001')
                case "5":
                    morlst.append('00000')
                case "6":
                    morlst.append('10000')
                case "7":
                    morlst.append('11000')
                case "8":
                    morlst.append('11100')
                case "9":
                    morlst.append('11110')
                case " ":
                    morlst.append('/')
                case ".":
                    morlst.append('010101')
                case ",":
                    morlst.append('110011')
                case ":":
                    morlst.append('111000')
                case "?":
                    morlst.append('001100')
                case "'":
                    morlst.append('011110')
                case "-":
                    morlst.append('100001')
                case "/":
                    morlst.append('10010')
                case "(":
                    morlst.append('10110')
                case ")":
                    morlst.append('101101')
                case "\"":
                    morlst.append('010010')
                case "=":
                    morlst.append('10001')
                case "+":
                    morlst.append('01010')
                case "@":
                    morlst.append('011010')
    for i in morlst:
        morstr = morstr + i
        morstr = morstr + " "
    
    morse.config(state=NORMAL)
    morse.delete(1.0,END)    
    morse.insert(1.0,morstr)
    morse.config(state=DISABLED, background="lightgrey")
    
def morsedecode():                           #Morse Decode
    morsede=morse.get(1.0,END)

    mordelst=list(morsede.split())
    mordelst2=[]
    mordestr=""
    
    for i in mordelst:
        match i:
            case '01':
                mordelst2.append('a')

            case '1000':
                mordelst2.append('b')
            
            case '1010':
                mordelst2.append('c')

            case '100':
                mordelst2.append('d')

            case '0':
                mordelst2.append('e')

            case '0010':
                mordelst2.append('f')

            case '110':
                mordelst2.append('g')

            case '0000':
                mordelst2.append('h')

            case '00':
                mordelst2.append('i')

            case '0111':
                mordelst2.append('j')

            case '101':
                mordelst2.append('k')

            case '0100':
                mordelst2.append('l')
            
            case '11':
                mordelst2.append('m')

            case '10':
                mordelst2.append('n')

            case '111':
                mordelst2.append('o')

            case '0110':
                mordelst2.append('p')

            case '1101':
                mordelst2.append('q')

            case '010':
                mordelst2.append('r')

            case '000':
                mordelst2.append('s')

            case '1':
                mordelst2.append('t')

            case '001':
                mordelst2.append('u')

            case '0001':
                mordelst2.append('v')

            case '011':
                mordelst2.append('w')

            case '1001':
                mordelst2.append('x')

            case '1011':
                mordelst2.append('y')

            case '1100':
                mordelst2.append('z')

            case '11111':
                mordelst2.append('0')

            case '01111':
                mordelst2.append('1')

            case '00111':
                mordelst2.append('2')

            case '00011':
                mordelst2.append('3')

            case '00001':
                mordelst2.append('4')

            case '00000':
                mordelst2.append('5')

            case '10000':
                mordelst2.append('6')

            case '11000':
                mordelst2.append('7')

            case '11100':
                mordelst2.append('8')

            case '11110':
                mordelst2.append('9')

            case '010101':
                mordelst2.append('.')

            case '110011':
                mordelst2.append(',')

            case '111000':
                mordelst2.append(':')

            case '001100':
                mordelst2.append('?')

            case '011110':
                mordelst2.append('\'')

            case '100001':
                mordelst2.append('-')

            case '10010':
                mordelst2.append('/')

            case '101101':
                mordelst2.append(')')

            case '10110':
                mordelst2.append('(')

            case '010010':
                mordelst2.append('"')

            case '10001':
                mordelst2.append('=')

            case '01010':
                mordelst2.append('+')

            case '011010':
                mordelst2.append('@')

            case '/':
                mordelst2.append(' ')

            case _ :
                print("Invalid Morse. Please Enter a Correct one.")

    
    

    txt.config(state=NORMAL)
    txt.delete(1.0,END)    
    txt.insert(1.0,mordestr.join(mordelst2))
    txt.config(state=DISABLED, background="lightgrey")

def about():                                 #About Button
    def webp():
        webbrowser.open_new_tab("https://github.com/Hk-Hacker-Harsh/GUI_Morse_Code_System")

    def webx():
        webbrowser.open_new_tab("https://x.com/Hk__Hacker")

    def webgh():
        webbrowser.open_new_tab("https://github.com/Hk-Hacker-Harsh")

    def weblt():
        webbrowser.open_new_tab("https://linktr.ee/Hk.Hacker")


    aboutwin= Toplevel()
    aboutwin.geometry("720x250")
    aboutwin.resizable(0,0)
    aboutwin.config(bg='#f6e947')
    aboutwin.title("About Developer")

    Label(aboutwin, text=f"Created By: HK (Harsh Khandal) Hacker\n", font=("",13,"bold","italic"), bg='#f6e947').place(x=15,y=15)
    Label(aboutwin, text="Project: Morse System (GUI Version)\nDated On: 19 June 2025", font=("",12,""),bg="#f6e947", justify=LEFT).place(x=19,y=65)

    Button(aboutwin, text="Twitter(X)", font=("",9,""),command=webx).place(x=180,y=200,anchor=CENTER)
    Button(aboutwin, text="Github", font=("",9,""),command=webgh).place(x=360,y=200, anchor=CENTER)
    Button(aboutwin, text="Linktr.ee", font=("",9,""),command=weblt).place(x=540,y=200, anchor=CENTER)
    Button(aboutwin, text="Project Repo Link", font=("",9,""),command=webp).place(x=360,y=155, anchor=CENTER)

def Manual():
    def dotsound():
        winsound.Beep(2500,200)            #Dot Beep Sound

    def dashsound():
        winsound.Beep(2500,550)            #Dash Beep Sound

    morsewin=Tk()
    morsewin.geometry("320x160")
    morsewin.config(background="LightBlue")
    morsewin.title("Manual Morse")

    Label(morsewin,text="Manual Morse", font=("",14,"bold", "italic"), background="#ABABFF", relief=RIDGE, bd=5, height=1, width=20).place(x=160,y=45,anchor=S)

    dot=Button(morsewin, text="Dot", font=("",11,"bold"), height=3, width=12, command=dotsound)
    dot.place(x=80,y=100, anchor=CENTER)

    dash=Button(morsewin, text="Dash", font=("",11,"bold"), height=3 , width=12, command=dashsound)
    dash.place(x=240,y=100, anchor=CENTER)

    morsewin.mainloop()



#Code
win = Tk()
win.geometry('600x350')
win.resizable(0,0)

try:
    img = PhotoImage(file='img.png')
    win.iconphoto(True, img)
except Exception as e:
    pass

win.config(background="LightBlue")
win.title("Morse System")

Label(win, text="Text", height=1, width=7, bg="LightGreen", bd=5, relief=RIDGE, font=("",15,"bold","italic")).place(x=15,y=15)
Label(win, text="Morse", height=1, width=7, bg="LightGreen", bd=5, relief=RIDGE, font=("",15,"bold","italic")).place(x=585,y=15, anchor="ne")

txt=Text(win, height=10, width=35)
txt.place(x=15,y=55)
morse=Text(win, height=10, width=35)
morse.place(x=585,y=55,anchor='ne')

proceed=Button(win,text="Proceed",width=8,command=convert)
proceed.place(x=300,y=250,anchor="center")
clear=Button(win,text="Clear",width=8,command=reset)
clear.place(x=300,y=280,anchor="center")

playbut=Button(win,text="Play Morse",command=playmorse, font=("",10,""), state=DISABLED)
playbut.place(x=550,y=300, anchor="e")

About = Button(win, text="About Me", font=("",10,""),command=about)
About.place(x=50,y=300, anchor="w")

Manualbut = Button(win, text="Manual Morse", font=("",10,""),command=Manual)
Manualbut.place(x=300, y=20, anchor=N)

win.mainloop()

# GUI Morse Code System
# Modified on 25/6/2025
# Created By HK (Harsh Khandal) Hacker