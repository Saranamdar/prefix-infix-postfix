


from tkinter import *
root=Tk()
root.geometry("600x300")
root.configure(bg="#C4DDFF")
import prefix_infix_postfix





eq=""
exp1=""
result=""

def reset():
    v3.set("")
    v2.set("")

def convert():
    global eq
    global exp1
    buttonpushed()
    t1= var1.get()
    t2= var2.get()
    if(t1=="infix" and t2=="postfix"):
        eq=prefix_infix_postfix.infix_to_postfix(exp1)
        result=eval(exp1)
        v3.set(result)
        v2.set(eq)
    elif(t1=="postfix" and t2=="infix"):
        eq=prefix_infix_postfix.postfix_to_infix(exp1)
        v2.set(eq)
        result=eval(eq)
        v3.set(result)
    elif(t1=="prefix" and t2=="infix"):
        eq=prefix_infix_postfix.prefix_to_infix(exp1)
        v2.set(eq)
        result=eval(eq)
        v3.set(result)
    elif(t1=="infix" and t2=="prefix"):
        eq=prefix_infix_postfix.infix_to_prefix(exp1)
        v2.set(eq)
        result=eval(exp1)
        v3.set(result)
    else:
        print("ERROR")
    
    
    
def buttonpushed():
    global txtb
    global exp1
    exp1= txtb.get()






var1= StringVar(root)
var1.set("infix")
option1 = OptionMenu(root,var1,"prefix","infix","postfix")
option1.grid(row=0,column=0,padx=5,pady=5)

txtb = Entry(root,bg="#7FB5FF",fg="black",font=("Comic Sans MS",15),width=40)
txtb.grid(row=0,column=1,padx=5,pady=5)


var2= StringVar(root)
var2.set("None")
option2 = OptionMenu(root,var2,"prefix","infix","postfix")
option2.grid(row=1,column=0,padx=5,pady=5)

v2=StringVar()
label2 = Label(root,textvariable=v2,width="40",bg="#7FB5FF",fg="BLACK",padx=1,pady=1,font=("Comic Sans MS",15)).grid(row=1,column=1,padx=5,pady=5)

v3=StringVar()
label3 = Label(root,textvariable=v3,width="40",bg="#7FB5FF",fg="BLACK",padx=1,pady=1,font=("Comic Sans MS",15)).grid(row=2,column=1,padx=5,pady=5)

b = Button(root,text="CONVERT",relief=GROOVE,command=convert).place(x=50,y=140)
b2 = Button(root,text="reset",relief=GROOVE,command=reset).place(x=150,y=140)



root.mainloop()







