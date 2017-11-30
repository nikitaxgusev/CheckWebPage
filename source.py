import MainBuildMode
from tkinter import *

root=Tk()

#root.geometry("200x100")
app=MainBuildMode.Application(root)
root.resizable(width=False,height=False)
root.mainloop()