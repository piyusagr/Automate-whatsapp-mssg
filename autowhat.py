from tkinter import *
import pywhatkit as pwk
from tkinter import ttk 

root=Tk()
root.title("Automate Whatsapp")
root.geometry("800x900+150+100")

root.resizable(False,False)
 
# name of the app
titlename=Label(root,text="AUTO WHATSAPP MESSAGE SEND", font=('arial black',19,'bold'),
                bg='grey',fg='green',bd=5,relief=RIDGE,width=30)
titlename.pack(side=TOP)

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
   
# frames
frames=Frame(root,bd=3,relief=RAISED,bg='lightgreen')
frames.place(x=10,y=68,width=780,height=780)

phoneval=StringVar()
groupnval=StringVar()
hourval=StringVar()
minval=StringVar()

# enter phone number
phoneno=Label(frames,text="Phone number : ",font=('arial',18,'bold'),bg='lightgray',width=15 ,fg="Green")
phoneno.grid(row=0,column=0,padx=16,pady=10)

phoneentry=Entry(frames,textvariable=phoneval,bg='lightgray',fg="Green",bd=3,relief=RAISED,width=16,font=('arial',18,'italic'),highlightthickness=2,highlightcolor='blue')
phoneentry.grid(row=0,column=1)

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

# send button personally
btn=Button(frames,text='Send Message',command=sendd, width=18,font=('times new roman',15,'bold'),bg='blue',fg='white',activebackground='white',activeforeground='blue',highlightthickness=2 , highlightcolor='black')
btn.grid(row=6, column=0,sticky=E)

# send button mssg
btn=Button(frames,text='Send Group Message',command=group, width=18,font=('times new roman',15,'bold'),bg='blue',fg='white',activebackground='white',activeforeground='blue',highlightthickness=2 , highlightcolor='black')
btn.grid(row=6,column=1,sticky=W)


root.mainloop()