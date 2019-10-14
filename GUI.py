from tkinter import *
root=Tk()       #create GUI
root.title('text to speech')
root.geometry('600x400')
root.resizable(True,True)

L1=Label(root,text='text to speech conversion',
         font=('Arial',20,'italic'),fg='RED')
L1.place(x=120,y=50)
L2=Label(root,text='enter text',
         font=('Arial',15),fg='blue')
L2.place(x=100,y=150)
E1=Entry(root,font=('Arial',15,'bold'),fg='blue')
E1.place(x=200,y=150)
B1=Button(root,text='continue',
          font=('Arial',15,'bold'),fg='red')
B1.place(x=220,y=200)

#root.mainloop()    #terminate GUI
