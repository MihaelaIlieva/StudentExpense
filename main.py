#import loginpage
#import registerpage
from tkinter import Tk, Label, PhotoImage, Button

class MainPage:

    def __init__(self):
        
        self.root = Tk()
        self.root.title("Student Expense")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # self.root["bg"]="#354255"
        # '#100235'
        self.MAIN_COLOUR = "#346c99"
        self.FONT_COLOUR = '#8c198f'
        self.FONT_COLOUR = '#ffffff'
        
        self.root.config(bg=self.MAIN_COLOUR)

        # self.background_label = Label(self.root)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1, width=1500, height=1500)
        #self.background_image = PhotoImage(file = "D:/StrypesLab/StudentExpense/StudentExpense/e.png")
        #self.background_label.configure(image=self.background_image)

        self.text_label = Label(self.root, text="Welcome to Mihaela's Student Expense Analiser", font=(None, 20), bg=self.MAIN_COLOUR, fg =self.FONT_COLOUR)
        self.text_label.place(relx=0.5, rely=0.15, anchor="center")

        self.subtext_label = Label(self.root, text="A place where you can evaluate your financial decisions", font=(None, 14), bg=self.MAIN_COLOUR, fg =self.FONT_COLOUR)
        self.subtext_label.place(relx=0.5, rely=0.20, anchor="center")


        self.picture_label = Label(self.root, bg=self.MAIN_COLOUR)
        self.picture_label.place(relx=0.5, rely=0.35, anchor="center", width=450, height=275)
        self.picture_image = PhotoImage(file = "D:\StrypesLab\StudentExpense\StudentExpense\exp1.png")
        self.picture_label.configure(image=self.picture_image)


        self.login_label = Label(self.root, text="Already have an account?", font=(None, 14), bg=self.MAIN_COLOUR, fg =self.FONT_COLOUR)
        self.login_label.place(relx=0.5, rely=0.50, anchor="center")

        self.login_button = Button(self.root, text="Login", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.open_login_page, width=10)
        self.login_button.place(relx=0.5, rely=0.55, anchor="center")

        self.login_label = Label(self.root, text="New to the game portal?", font=(None, 14), bg=self.MAIN_COLOUR, fg =self.FONT_COLOUR)
        self.login_label.place(relx=0.5, rely=0.60, anchor="center")

        self.register_button = Button(self.root, text="Register", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.open_register_page, width=10)
        self.register_button.place(relx=0.5, rely=0.65, anchor="center")
        
        self.root.mainloop()

    def open_login_page(self):
        self.root.destroy()
        #loginpage.LoginPage()

    def open_register_page(self):
        self.root.destroy()
        #registerpage.RegisterPage()

if __name__ == "__main__":

    app = MainPage()
