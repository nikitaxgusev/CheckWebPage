from tkinter import *
import webbrowser

class Application(Frame):
    """GUI-application with two buttons that inter in Internet"""

    def __init__(self,master):
        """Initilization the frame"""
        super(Application,self).__init__(master)
        master.title("WebEnter")
        master.geometry("210x130")
        self.grid()

        self.create_widgets()

    def create_widgets(self):
        """Creating label and several buttons"""
        self.lbl_welcome=Label(self,text="Choose the web site:")
        self.lbl_welcome.grid(row=0,column=1)

        self.btn_one=Button(self,text="VK",command=self.enterVK,height = 1, width =10)
        self.btn_one.grid(row=1,column=1)

        self.btn_two=Button(self,text="Instagram",command=self.enterINST,height = 1, width =10)
        self.btn_two.grid(row=2,column=1)

        self.btn_three = Button(self, text="Email", command=self.enterEMAIL,height = 1, width =10)
        self.btn_three.grid(row=3, column=1)

        self.btn_four = Button(self, text="Google", command=self.enterGOOGLE, height=1, width=10)
        self.btn_four.grid(row=1, column=2)

        self.btn_five = Button(self, text="Translator", command=self.enterGTranslate, height=1, width=10)
        self.btn_five.grid(row=2, column=2)


#Connect with web-adresses
    def enterVK(self):
        webbrowser.open("https://vk.com/", new=0, autoraise=True)

    def enterINST(self):
        webbrowser.open("https://www.instagram.com/", new=0, autoraise=True)

    def enterEMAIL(self):
        webbrowser.open("https://e.mail.ru/messages/inbox/", new=0, autoraise=True)

    def enterGOOGLE(self):
        webbrowser.open("https://google.com/", new=0, autoraise=True)

    def enterGTranslate(self):
        webbrowser.open("https://translate.google.ru/", new=0, autoraise=True)


if __name__=="__main__":
    print("ERROR.You have run a module. You must import it.\n")
    input("Enter any ker fro exit.\n")