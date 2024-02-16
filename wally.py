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

root.mainloop()
