from tkinter import *
root = Tk()
root.geometry("600x600")
frame_one = Frame(root)
frame_one.pack()
def hello():
    print("Hello World")

button_one = Button(frame_one, text="Hello?",command = hello)
button_one.pack()
root.mainloop()
