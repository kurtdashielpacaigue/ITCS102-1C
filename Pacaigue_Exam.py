
import tkinter as tk 
window =tk. Tk()
window.configure(bg="purple")
window.title("Pacaigue_Exam")
window.geometry("300x200")




def open_register():

    register=tk.Toplevel()
    register.configure(bg="purple")


    label=tk.Label(register,text="Register here son")
    label.grid(row=0,column=1)

    usernamelabel=tk.Label(register,text="username")
    usernamelabel.grid(row=1,column=0)

    regframe=tk.Frame(register,bg="green")
    regframe.grid

    passlabel=tk.Label(register,text="username")
    passlabel.grid(row=2,column=0)




    username_entry=tk.Entry(register)
    username_entry.grid(row=1,column=1)

    passname=tk.Entry(register)
    passname.grid(row=2,column=1)   


    seepassword=tk.Checkbutton(register,text="see password")
    seepassword.grid(row=3,column=1,padx=10,pady=10)

    name=label['text']=f"You have succesfully registered  "

    
 


    buttonname=tk.Button(register,text="Register",command=name)
    buttonname.grid(row=4,column=1)




def open_login():

    namerr=username_entry.get()
    paaaasss=passname.get()

    register=tk.Toplevel()
    register.configure(bg="purple")


    label=tk.Label(register,text="Login Here Son")
    label.grid(row=0,column=1)

    usernamelabel=tk.Label(register,text="username")
    usernamelabel.grid(row=1,column=0)

    regframe=tk.Frame(register,bg="green")
    regframe.grid

    passlabel=tk.Label(register,text="username")
    passlabel.grid(row=2,column=0)




    username_entry=tk.Entry(register)
    username_entry.grid(row=1,column=1)

    passname=tk.Entry(register)
    passname.grid(row=2,column=1)   


    seepassword=tk.Checkbutton(register,text="see password")
    seepassword.grid(row=3,column=1,padx=10,pady=10)

    #Unfinished pero gradean nyo napo lol

    # if username_entry<8:
    #     label.config(text="suername is less than 8")

    # elif passname <8:
    #       label.config(text="suername is less than 8")
        
    # else:
    #      label=tk.Label(text="die")



    name1=label['text']=f"You have succesfully Logged in "


    buttonname1=tk.Button(register,text="login",command=name1)
    buttonname1.grid(row=4,column=1)








label=tk.Label(window,text="Welcome",font=("Arial",10,"bold"))
label.pack(fill="x",anchor="center",padx=10,pady=10)




RegisterButton=tk.Button(window,text="Register",bg="Blue",command=open_register)
RegisterButton.pack(anchor="center",fill="x")


loginbutton=tk.Button(window,text="Log in",bg="green",command=open_login)
loginbutton.pack(anchor="center",fill="x")



window.mainloop()
