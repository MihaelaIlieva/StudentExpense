#import loginpage
#import database.basicqueries as basicqueries
from tkinter import Tk, Label, PhotoImage, Entry, Button, Spinbox, StringVar, OptionMenu

class RegisterPage:

    def __init__(self):
        self.root = Tk()
        self.root.title("Student Expense - Register Page")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.MAIN_COLOUR = '#346c99'
        self.FONT_COLOUR = '#8c198f'
        self.FONT_COLOUR = '#ffffff'
        
        self.root.config(bg=self.MAIN_COLOUR)
        self.error_message = None    

        self.text_label = Label(self.root, text="Please put in your wanted credentials", font=(None, 20), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.text_label.place(relx=0.5, rely=0.10, anchor="center")

        self.picture_label = Label(self.root, bg=self.MAIN_COLOUR)
        self.picture_label.place(relx=0.5, rely=0.24, anchor="center", width=450, height=245)
        self.picture_image = PhotoImage(file = "D:\StrypesLab\StudentExpense\StudentExpense\exp1.png")
        self.picture_label.configure(image=self.picture_image)

        self.username_label = Label(self.root, text="Username", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.username_label.place(relx=0.5, rely=0.37, anchor="center")

        self.password_label = Label(self.root, text="Password", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.password_label.place(relx=0.5, rely=0.43, anchor="center")
        
        self.age_label = Label(self.root, text="Age", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.age_label.place(relx=0.5, rely=0.49, anchor="center")
        
        self.gender_label = Label(self.root, text="Gender", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.gender_label.place(relx=0.5, rely=0.55, anchor="center")
        
        self.year_label = Label(self.root, text="Year in school", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.year_label.place(relx=0.5, rely=0.61, anchor="center")
        
        self.major_label = Label(self.root, text="Major", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.major_label.place(relx=0.5, rely=0.67, anchor="center")
        

        self.username_entry = Entry(self.root, font=(None, 14), width=21)
        self.username_entry.place(relx=0.5, rely=0.40, anchor="center")

        self.password_entry = Entry(self.root, font=(None, 14), show="*", width=21)
        self.password_entry.place(relx=0.5, rely=0.46, anchor="center")
        
        self.age_entry = Spinbox(self.root, font=(None, 14), from_=10, to=100, width=20)
        self.age_entry.place(relx=0.5, rely=0.52, anchor="center")
        
        self.gender_options = ["Male", "Female", "Non-binary"]
        self.selected_option = StringVar()
        self.selected_option.set(self.gender_options[0])
        
        self.gender_entry = OptionMenu(self.root, self.selected_option,*self.gender_options)
        self.gender_entry.place(relx=0.5, rely=0.58, anchor="center")
        self.gender_entry.config(width=31)
        
        self.year_options = ["Freshman", "Sophomore", "Junior", "Senior"]
        self.selected_year_option = StringVar()
        self.selected_year_option.set(self.year_options[0])
        
        self.year_entry = OptionMenu(self.root, self.selected_year_option,*self.year_options)
        self.year_entry.place(relx=0.5, rely=0.64, anchor="center")
        self.year_entry.config(width=31)
        
        self.major_options = ["Economics", "Computer Science", "Engineering", "Psychology", "Biology"]
        self.selected_major_option = StringVar()
        self.selected_major_option.set(self.major_options[0])  # Set the default option
        
        # Create the OptionMenu for majors
        self.major_entry = OptionMenu(self.root, self.selected_major_option, *self.major_options)
        self.major_entry.place(relx=0.5, rely=0.70, anchor="center")
        self.major_entry.config(width=31)        

        self.login_button = Button(self.root, text="Register", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.register, width=10)
        self.login_button.place(relx=0.5, rely=0.77, anchor="center")

        self.error_message_label = Label(self.root, text=self.error_message, font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.error_message_label.place(relx=0.5, rely=0.81, anchor="center")
        
        self.root.mainloop()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.error_message = "Please fill in all fields."
            self.error_message_label.config(text=self.error_message)

        # elif basicqueries.check_for_same_username(username):
        #     self.error_message = "Username already exists. Please choose another one."
        #     self.error_message_label.config(text=self.error_message)
        # else:
        #     basicqueries.add_user(username, password)
        #     self.error_message = "Successfully registered. Please log in."
        #     self.error_message_label.config(text=self.error_message)
        #     self.root.after(500, lambda: self.redirect_to_loginpage())

    def redirect_to_loginpage(self):
        self.root.destroy()
        # loginpage.LoginPage()

if __name__ == "__main__":
    register_page = RegisterPage()