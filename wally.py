from tkinter import *

root=Tk()
root.geometry('750x600')
root.title('Viktoriia')
root.iconbitmap('coffee.ico')

text=Label(text='Gamma editor', font='Arial 20')
text.pack()

img=PhotoImage(file='Wally.png')
lb=Label(image=img)
lb.pack()

def set_gamma(val):
    img['gamma']=val

scale=Scale(from_=1, to=10, length=700, orient=HORIZONTAL, command=set_gamma)
scale.pack()

root.mainloop()
