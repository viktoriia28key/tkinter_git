from tkinter import *

root=Tk()
root.geometry('750x550')
root.title('Viktoriia')
root.iconbitmap('coffee.ico')

img=PhotoImage(file='Wally.png')
lb=Label(image=img)
lb.pack()

root.mainloop()
