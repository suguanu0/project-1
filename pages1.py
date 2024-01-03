from tkinter import *
root=Tk()
input=Entry(root,text="resalt",width=40)
input.place(x=0,y=0)
def gta(pages):
    current=input.get()
    input.delete(0,END)
    input.insert(0,str(current)+str(pages))





button=Button(root,text="1",command=lambda:gta(1))
button.place(x=5,y=50)
root.mainloop()