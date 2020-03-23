from tkinter import *
import os

root=Tk()
root.geometry('500x500')
root.title('The Machine Learning Module')

def fire():
    try:
        file= r'C:/Users/dell/Desktop/k-means.py'
        os.startfile(file)
    except:
        print('Their is a Problem in a Path!')


def face():
    try:
        file=r'C:/Users/dell/Desktop/Python Codes/object.py'
        os.startfile(file)
    except:
        print('Their is a Problem in a Path!')

def cam():
    try:
        file=r'C:/Users/dell/Desktop/Python Codes/random.py'
        os.startfile(file)
    except:
        print('Their is a Problem in a Path!')

def rob():
    try:
        file=r'C:/Users/dell/Desktop/inherit.py'
        os.startfile(file)
    except:
        print('Their is a Problem in a Path!')
    
    


btn1=Button(root, text='Fire module', bd='3', height=10, width=20, font=10, command=fire).grid(row=5, column=1 ,padx=30, pady=10)
btn2=Button(root, text='Face Detect module', bd='3', height=10, width=20, font=10, command=face).grid(row=5, column=4, pady=10)

btn3=Button(root, text='Camera module', bd='3', height=10, width=20, font=10, command=cam).grid(row=10, column=1 ,padx=30, pady=10)
btn4=Button(root, text='Roberry module', bd='3', height=10, width=20, font=10, command=rob).grid(row=10, column=4, pady=10)


root.resizable(0, 0)
root.mainloop()
