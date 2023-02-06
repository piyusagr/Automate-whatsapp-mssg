from tkinter import *
import pywhatkit as pwk
from tkinter import ttk 

root=Tk()
root.title("Automate Whatsapp")
root.geometry("900x1000+150+50")

root.resizable(False,False)
 
# name of the app
titlename=Label(root,text="AUTO WHATSAPP MESSAGE SEND", font=('arial black',19,'bold'),
                bg='grey',fg='green',bd=5,relief=RIDGE,width=35)
titlename.pack(side=TOP)


#  whatsapp message send personally at given time
def mssgpersonal():
    # send button fucntion
    def sendd():
        mssg=messageentry.get(1.0,'end-1c')
        if phoneval.get() and str(hourval.get()) and str(minval.get()) and mssg:  
            pwk.sendwhatmsg(phoneval.get(),mssg,int(hourval.get()),int(minval.get()),15,00)
            data=Label(frames,text="" , font=('arial',18,'bold'), width=15,fg='Gray')
            data.grid(row=7,column=1,padx=15,pady=12,sticky=W)
            data.config(text="message sent")
        
        else:
            data=Label(frames,text="" , font=('arial',18,'bold'), width=15,fg='Gray')
            data.grid(row=7,column=1,padx=15,pady=12,sticky=W)
            data.config(text="enter detail properly")
            
    # frames
    frames=Frame(root,bg='lightgreen')
    frames.place(x=23,y=250,width=850,height=700)

    phoneval=StringVar()
    hourval=StringVar()
    minval=StringVar()

    # enter phone number
    phoneno=Label(frames,text="Phone number : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
    phoneno.grid(row=1,column=0,padx=16,pady=10)

    phoneentry=Entry(frames,textvariable=phoneval,bg='lightgray',fg="Green",bd=3,relief=RAISED,width=16,font=('arial',18,'italic'),highlightthickness=2,highlightcolor='blue')
    phoneentry.grid(row=1,column=1)

    # enter the message u need to send
    message=Label(frames,text="Message Send : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
    message.grid(row=2,column=0,padx=10,pady=16)

    messageentry=Text(frames,font=('arial',18,'italic'),bg='lightgray',width=16,height=7,fg='green',highlightthickness=2,highlightcolor='blue',bd=3,relief=RAISED)
    messageentry.grid(row=2,column=1)

    # enter the hour and minute to be send at that time
    # hour
    hour=Label(frames,text="Hours : ",font=('arial',18,'bold'),bg='lightgray', width=15,fg='green')
    hour.grid(row=3,column=0,padx=16,pady=10)

    options=[i for i in range(1,25)]
    hourentry= ttk.Combobox(frames,textvariable=hourval,values=options,width=15,height=20,justify=CENTER,font=('arial',18,'italic'))
    hourentry.grid(row=3,column=1,padx=16,pady=10)
    hourval.set('--select option--')

    # minute
    minutes=Label(frames,text="Minute : ",font=('arial',18,'bold'),bg='lightgray', width=15,fg='green')
    minutes.grid(row=4,column=0,padx=16,pady=10)

    optiond=[i for i in range(1,61)]
    minuteentry= ttk.Combobox(frames,textvariable=minval,values=optiond,width=15,height=20,justify=CENTER,font=('arial',18,'italic'))
    minuteentry.grid(row=4,column=1,padx=16,pady=10)
    minval.set('--select option--')

    # send button personally
    btn=Button(frames,text='Send Message',command=sendd, width=18,font=('times new roman',15,'bold'),bg='blue',fg='white',activebackground='white',activeforeground='blue',highlightthickness=2 , highlightcolor='black')
    btn.grid(row=6, column=0,sticky=E)

#  whatsapp message send personally instantly
def mssgpersonalinstant():
    # send button fucntion
    def sendd():
        mssg=messageentry.get(1.0,'end-1c')
        if phoneval.get() and mssg:  
            pwk.sendwhatmsg_instantly(phoneval.get(),mssg)
            data=Label(frames,text="" , font=('arial',18,'bold'), width=15,fg='Gray')
            data.grid(row=5,column=1,padx=15,pady=12,sticky=W)
            data.config(text="message sent")
        
        else:
            data=Label(frames,text="" , font=('arial',18,'bold'), width=15,fg='Gray')
            data.grid(row=5,column=1,padx=15,pady=12,sticky=W)
            data.config(text="enter detail properly")

    frames=Frame(root,bg='lightgreen')
    frames.place(x=23,y=250,width=850,height=700)
    
    phoneval=StringVar()

    # enter phone number
    phoneno=Label(frames,text="Phone number : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
    phoneno.grid(row=1,column=0,padx=16,pady=10)

    phoneentry=Entry(frames,textvariable=phoneval,bg='lightgray',fg="Green",bd=3,relief=RAISED,width=16,font=('arial',18,'italic'),highlightthickness=2,highlightcolor='blue')
    phoneentry.grid(row=1,column=1)

    # enter the message u need to send
    message=Label(frames,text="Message Send : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
    message.grid(row=2,column=0,padx=10,pady=16)

    messageentry=Text(frames,font=('arial',18,'italic'),bg='lightgray',width=16,height=7,fg='green',highlightthickness=2,highlightcolor='blue',bd=3,relief=RAISED)
    messageentry.grid(row=2,column=1)

    # send button personally
    btn=Button(frames,text='Send Message',command=sendd, width=18,font=('times new roman',15,'bold'),bg='blue',fg='white',activebackground='white',activeforeground='blue',highlightthickness=2 , highlightcolor='black')
    btn.grid(row=4, column=0,sticky=E)

# whatsapp group message send at given time
def groupmssgtime():        
    def group():
        mssg=messageentry.get(1.0,'end-1c')
        if groupnval.get() and str(hourval.get()) and str(minval.get()) and mssg: 
            pwk.sendwhatmsg_to_group(groupnval.get(),mssg,int(hourval.get()),int(minval.get()),15,00)
            data=Label(frames,text="" , font=('arial',18,'bold'), width=15,fg='Gray')
            data.grid(row=7,column=1,padx=15,pady=12,sticky=W)
            data.config(text="message sent")
        
        else:
            data=Label(frames,text="" , font=('arial',18,'bold'), width=15,fg='Gray')
            data.grid(row=7,column=1,padx=15,pady=12,sticky=W)
            data.config(text="enter detail properly")

    frames=Frame(root,bg='lightgreen')
    frames.place(x=23,y=250,width=850,height=700)

    groupnval=StringVar()
    hourval=StringVar()
    minval=StringVar()

     #enter the name og group
    groupname=Label(frames,text="Group adminID  : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
    groupname.grid(row=1,column=0,padx=16,pady=10)

    Groupentry=Entry(frames,textvariable=groupnval,bg='lightgray',fg="Green",bd=3,relief=RAISED,width=16,font=('arial',18,'italic'),highlightthickness=2,highlightcolor='blue')
    Groupentry.grid(row=1,column=1)

    # enter the message u need to send
    message=Label(frames,text="Message Send : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
    message.grid(row=2,column=0,padx=10,pady=16)

    messageentry=Text(frames,font=('arial',18,'italic'),bg='lightgray',width=16,height=7,fg='green',highlightthickness=2,highlightcolor='blue',bd=3,relief=RAISED)
    messageentry.grid(row=2,column=1)

    # enter the hour and minute to be send at that time
    # hour
    hour=Label(frames,text="Hours : ",font=('arial',18,'bold'),bg='lightgray', width=15,fg='green')
    hour.grid(row=3,column=0,padx=16,pady=10)

    options=[i for i in range(1,25)]
    hourentry= ttk.Combobox(frames,textvariable=hourval,values=options,width=15,height=20,justify=CENTER,font=('arial',18,'italic'))
    hourentry.grid(row=3,column=1,padx=16,pady=10)
    hourval.set('--select option--')

    # minute
    minutes=Label(frames,text="Minute : ",font=('arial',18,'bold'),bg='lightgray', width=15,fg='green')
    minutes.grid(row=4,column=0,padx=16,pady=10)

    optiond=[i for i in range(1,61)]
    minuteentry= ttk.Combobox(frames,textvariable=minval,values=optiond,width=15,height=20,justify=CENTER,font=('arial',18,'italic'))
    minuteentry.grid(row=4,column=1,padx=16,pady=10)
    minval.set('--select option--')
    
    # send button mssg
    btn=Button(frames,text='Send Group Message',command=group, width=18,font=('times new roman',15,'bold'),bg='blue',fg='white',activebackground='white',activeforeground='blue',highlightthickness=2 , highlightcolor='black')
    btn.grid(row=6,column=1,sticky=W)


# whatsapp group message send instantly
def groupmssgtimeinstant():        
    def group():
        mssg=messageentry.get(1.0,'end-1c')
        if groupnval.get() and mssg: 
            pwk.sendwhatmsg_to_group_instantly(groupnval.get(),mssg)
            data=Label(frames,text="" , font=('arial',18,'bold'), width=15,fg='Gray')
            data.grid(row=4,column=1,padx=15,pady=12,sticky=W)
            data.config(text="message sent")
        
        else:
            data=Label(frames,text="" , font=('arial',18,'bold'), width=15,fg='Gray')
            data.grid(row=4,column=1,padx=15,pady=12,sticky=W)
            data.config(text="enter detail properly")

    frames=Frame(root,bg='lightgreen')
    frames.place(x=23,y=250,width=850,height=700)

    groupnval=StringVar()

     #enter the name og group
    groupname=Label(frames,text="Group adminID  : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
    groupname.grid(row=1,column=0,padx=16,pady=10)

    Groupentry=Entry(frames,textvariable=groupnval,bg='lightgray',fg="Green",bd=3,relief=RAISED,width=16,font=('arial',18,'italic'),highlightthickness=2,highlightcolor='blue')
    Groupentry.grid(row=1,column=1)

    # enter the message u need to send
    message=Label(frames,text="Message Send : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
    message.grid(row=2,column=0,padx=10,pady=16)

    messageentry=Text(frames,font=('arial',18,'italic'),bg='lightgray',width=16,height=7,fg='green',highlightthickness=2,highlightcolor='blue',bd=3,relief=RAISED)
    messageentry.grid(row=2,column=1)

    # send button mssg
    btn=Button(frames,text='Send Group Message',command=group, width=18,font=('times new roman',15,'bold'),bg='blue',fg='white',activebackground='white',activeforeground='blue',highlightthickness=2 , highlightcolor='black')
    btn.grid(row=3,column=1,sticky=W)

# personal list mssg
def personallistmssg():
    l,i=[],0

    # to send message 
    def mssgsend():
        mssg=messageentry.get(1.0,'end-1c')
        for phone in l:
            pwk.sendwhatmsg_instantly(phone,mssg)
        l.clear()
    
    # to add phone no in a loop
    def morenumber():
        nonlocal i
        if len(l)==9:
            btn['state']=DISABLED

        
        phoneno=Label(frames,text="Phone number : ",font=('arial',16,'bold'),bg='lightgray',width=13 ,fg="Green")
        phoneno.grid(row=1,column=0,padx=16,pady=10)
        phoneentry=Entry(frames,textvariable=phoneval,bg='lightgray',fg="Green",bd=3,relief=RAISED,width=15,font=('arial',16,'italic'),highlightthickness=2,highlightcolor='blue')
        phoneentry.grid(row=1,column=1)
        if len(l)<=10:
            data=Label(frames,text="" , font=('arial',14,'bold'), width=15,fg='Gray')
            data.grid(row=i,column=2,padx=15,pady=12,sticky=W)
            data.config(text=phoneentry.get())
            i+=1
            l.append(phoneentry.get())
            # print(l)

    frames=Frame(root,bg='lightgreen')
    frames.place(x=23,y=250,width=850,height=720)
    
    # variable of phone number
    phoneval=StringVar()

    # add more phone number option
    btn=Button(frames,text='Add more number',command=morenumber, width=18,font=('times new roman',12,'bold'),bg='blue',fg='white',activebackground='white',activeforeground='blue',highlightthickness=2 , highlightcolor='black')
    btn.grid(row=0,column=1,sticky=E)

    # enter phone number
    phoneno=Label(frames,text="Phone number : ",font=('arial',16,'bold'),bg='lightgray',width=13 ,fg="Green")
    phoneno.grid(row=1,column=0,padx=16,pady=10)

    phoneentry=Entry(frames,textvariable=phoneval,bg='lightgray',fg="Green",bd=3,relief=RAISED,width=15,font=('arial',16,'italic'),highlightthickness=2,highlightcolor='blue')
    phoneentry.grid(row=1,column=1)
    
    # enter the message u need to send
    message=Label(frames,text="Message Send : ",font=('arial',16,'bold'),bg='lightgray',width=13 ,fg="Green")
    message.grid(row=2,column=0,padx=10,pady=16)

    messageentry=Text(frames,font=('arial',16,'italic'),bg='lightgray',width=15,height=4,fg='green',highlightthickness=2,highlightcolor='blue',bd=3,relief=RAISED)
    messageentry.grid(row=2,column=1)

    # send button mssg
    btns=Button(frames,text='Send Message',command=mssgsend, width=13,font=('times new roman',15,'bold'),bg='blue',fg='white',activebackground='white',activeforeground='blue',highlightthickness=2 , highlightcolor='black')
    btns.grid(row=3,column=0,sticky=W)

# frames
frames=Frame(root,bd=3,relief=RAISED,bg='lightgreen')
frames.place(x=10,y=68,width=880,height=925)

# button for mssg sending selection

btn=Button(frames,text='Personal Message ',command=mssgpersonal, width=14,font=('times new roman',12,'bold'),bg='lightgray',fg='black',activebackground='lightgray',activeforeground='black',highlightthickness=2 , highlightcolor='black')
btn.grid(row=0,column=0,sticky=W)

btn=Button(frames,text='Personal MssgInstant' ,command=mssgpersonalinstant, width=16,font=('times new roman',12,'bold'),bg='lightgray',fg='black',activebackground='lightgray',activeforeground='black',highlightthickness=2 , highlightcolor='black')
btn.grid(row=0,column=1,sticky=W)

btn=Button(frames,text='Group Message ',command=groupmssgtime, width=14,font=('times new roman',12,'bold'),bg='lightgray',fg='black',activebackground='lightgray',activeforeground='black',highlightthickness=2 , highlightcolor='black')
btn.grid(row=0,column=2,sticky=W)

btn=Button(frames,text='Group Mssginstantly ',command=groupmssgtimeinstant, width=16,font=('times new roman',12,'bold'),bg='lightgray',fg='black',activebackground='lightgray',activeforeground='black',highlightthickness=2 , highlightcolor='black')
btn.grid(row=0,column=3,sticky=W)

btn=Button(frames,text='Personal MssgList',command=personallistmssg, width=14,font=('times new roman',12,'bold'),bg='lightgray',fg='black',activebackground='lightgray',activeforeground='black',highlightthickness=2 , highlightcolor='black')
btn.grid(row=1,column=0,sticky=W)

root.mainloop()