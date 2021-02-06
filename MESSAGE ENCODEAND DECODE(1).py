from tkinter import *
from PIL import Image,ImageTk
import base64

root= Tk()
root.geometry("900x550")
root.resizable(5,5)
root.title("MESSAGE - ENCODE AND DECODE")

back_ground=Image.open("scape.jpg")
back_ground = back_ground.resize((1370,720))
picture=ImageTk.PhotoImage(back_ground)

#define variables
Password = StringVar(root)
Text=StringVar(root)
result=StringVar(root)

#modes(1)
modes=["Encode","Decode"]
tkvari=StringVar(root)
tkvari.set(modes[0])

show = 0 
##functions##
#Function to show password
def showPassword():
    global show
    if show==0:
        e.configure(show="")
        b.configure(text="Unshow")
        show=1 
    else:
        e.configure(show="x")
        b.configure(text="Show")
        show = 0  
#function to encode
def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))    
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 
#function to decode
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))    
    return "".join(dec) 
#function for mode
def mode():
    if(tkvari.get() == modes[0]):
        result.set(Encode(Password.get(), Text.get()))
    elif(tkvari.get() == modes[1]):
        result.set(Decode(Password.get(), Text.get()))
    else:
        result.set('Invalid Mode')
#Function to reset and exit
def Reset():
    Text.set("")
    Password.set("")
    tkvari.set("")
    result.set("")

def Exit():
    root.destroy()
##Labels and buttons
Label(root,image=picture).pack()
Label(root, text ='ENCODE / DECODE',font = 'Times 20 bold underline'
      ,bg='medium orchid1').place(x=270,y=40)
Label(root, text ='BUILT TO LEARN PROJECT-KCG COLLEGE OF TECHNOLOGY', font = 'helvetica 14 bold',fg="brown",
      bg='peachpuff').place(x = 200,y= 500)
Label(root, text="MESSAGE",font="Times 20",fg="black",bg='sandybrown').place(x=200,y=170)
Entry(root,bg="khaki1",textvariable=Text,font = 'arial 19').place(x=480,y=170)

Label(root, text="KEY",font="Times 20",fg="black",bg='sandybrown').place(x=200,y=220)
e = Entry(root,show="x",width=20,bg="khaki1",textvariable = Password,font = 'arial 10')
e.place(x=480,y=220)

b=Button(root,text="Show",command = showPassword,padx =6,width =6,bg ='violet',font="HELVETICA 12 bold")
b.place(x=680,y=220)

Label(root, text="MODE",font="Times 20",fg="black",bg='sandybrown').place(x=200,y=270)
e1=Entry(root,font = "helvetica 12 bold")
OptionMenu(root,tkvari,*modes).place(x=480,y=270)

Label(root, text="RESULT",font="Times 20",fg="black",bg='sandybrown').place(x=200,y=350)
Entry(root,bg="khaki1",textvariable=result,font = 'Helvetica 20 bold').place(x=480,y=350)

Button(root,text="RESULT",command=mode,padx =6,width =6,bg ='green yellow',font="helvetica 11 bold",anchor='center' ).place(x=150,y=430)
Button(root,text="RESET",command=Reset,padx =6,width =6,bg ='deepskyblue',font="helvetica 11 bold",anchor='center').place(x=380,y=430)
Button(root,text="EXIT",command=Exit,padx =6,width =6,bg ='firebrick1',font="helvetica 11 bold",anchor='center').place(x=600,y=430)

root.mainloop()