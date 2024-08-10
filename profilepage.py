import mainpage
from tkinter import Tk, Label, Button, PhotoImage, Spinbox, StringVar, OptionMenu, Canvas

class ProfilePage:
    
    def __init__(self, username):
        
        self.username = username

        self.root = Tk()
        self.root.title("Student Expense - Profile Page")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.MAIN_COLOUR = '#346c99'
        self.FONT_COLOUR = '#8c198f'
        self.FONT_COLOUR = '#ffffff'
        
        self.root.config(bg=self.MAIN_COLOUR)

        self.username_label = Label(self.root, text=f"Welcome {self.username}! Please insert your incomes and expenses.", font=(None, 20), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.username_label.place(relx=0.5, rely=0.15, anchor="center")

        self.picture_label = Label(self.root, bg=self.MAIN_COLOUR, width = 250, height = 175)
        self.picture_label.place(relx=0.5, rely=0.27, anchor="center")
        self.picture_image = PhotoImage(file="D:\StrypesLab\StudentExpense\StudentExpense\exp1.png")
        self.picture_label.configure(image=self.picture_image)
        
        # Create a Canvas widget
        self.line_canvas = Canvas(self.root, width=2, height=500, bd=0, highlightthickness=0, bg=self.MAIN_COLOUR)
        self.line_canvas.place(relx=0.5, rely=0.35, anchor="n")  # Adjust anchor and relx/rely as needed

        # Draw a vertical line from y1=50 to y2=250
        self.line_canvas.create_line(0, 30, 0, 750, fill=self.FONT_COLOUR, width=2)

        self.monthly_income_label = Label(self.root, text="Monthly income (and aid)", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.monthly_income_label.place(relx=0.35, rely=0.37, anchor="center")
        
        self.tuition_label = Label(self.root, text="Yearly tuition", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.tuition_label.place(relx=0.65, rely=0.37, anchor="center")
        
        self.housing_label = Label(self.root, text="Housing", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.housing_label.place(relx=0.35, rely=0.45, anchor="center")
        
        self.food_label = Label(self.root, text="Food", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.food_label.place(relx=0.65, rely=0.45, anchor="center")
        
        # Transportation Label
        self.transportation_label = Label(self.root, text="Transportation", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.transportation_label.place(relx=0.35, rely=0.53, anchor="center")

        # Books_supplies Label
        self.books_supplies_label = Label(self.root, text="Books supplies", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.books_supplies_label.place(relx=0.65, rely=0.53, anchor="center")

        # Entertainment Label
        self.entertainment_label = Label(self.root, text="Entertainment", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.entertainment_label.place(relx=0.35, rely=0.61, anchor="center")

        # Personal_care Label
        self.personal_care_label = Label(self.root, text="Personal care", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.personal_care_label.place(relx=0.65, rely=0.61, anchor="center")

        # Technology Label
        self.technology_label = Label(self.root, text="Technology", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.technology_label.place(relx=0.35, rely=0.69, anchor="center")

        # Health_wellness Label
        self.health_wellness_label = Label(self.root, text="Health and wellness", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.health_wellness_label.place(relx=0.65, rely=0.69, anchor="center")

        # Miscellaneous Label
        self.miscellaneous_label = Label(self.root, text="Miscellaneous", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.miscellaneous_label.place(relx=0.35, rely=0.77, anchor="center")

        # Preferred_payment_method Label
        self.preferred_payment_method_label = Label(self.root, text="Preferred payment method", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.preferred_payment_method_label.place(relx=0.65, rely=0.77, anchor="center")
        
        # Monthly income (and aid) Spinbox
        self.incomes_entry = Spinbox(self.root, font=(None, 14), from_=0, to=10000, width=20)
        self.incomes_entry.place(relx=0.35, rely=0.41, anchor="center")

        # Yearly tuition Spinbox
        self.tuition_entry = Spinbox(self.root, font=(None, 14), from_=0, to=100000, width=20)
        self.tuition_entry.place(relx=0.65, rely=0.41, anchor="center")

        # Housing Spinbox
        self.housing_entry = Spinbox(self.root, font=(None, 14), from_=0, to=50000, width=20)
        self.housing_entry.place(relx=0.35, rely=0.49, anchor="center")

        # Food Spinbox
        self.food_entry = Spinbox(self.root, font=(None, 14), from_=0, to=10000, width=20)
        self.food_entry.place(relx=0.65, rely=0.49, anchor="center")

        # Transportation Spinbox
        self.transportation_entry = Spinbox(self.root, font=(None, 14), from_=0, to=10000, width=20)
        self.transportation_entry.place(relx=0.35, rely=0.57, anchor="center")

        # Books_supplies Spinbox
        self.books_supplies_entry = Spinbox(self.root, font=(None, 14), from_=0, to=5000, width=20)
        self.books_supplies_entry.place(relx=0.65, rely=0.57, anchor="center")

        # Entertainment Spinbox
        self.entertainment_entry = Spinbox(self.root, font=(None, 14), from_=0, to=10000, width=20)
        self.entertainment_entry.place(relx=0.35, rely=0.65, anchor="center")

        # Personal_care Spinbox
        self.personal_care_entry = Spinbox(self.root, font=(None, 14), from_=0, to=5000, width=20)
        self.personal_care_entry.place(relx=0.65, rely=0.65, anchor="center")

        # Technology Spinbox
        self.technology_entry = Spinbox(self.root, font=(None, 14), from_=0, to=20000, width=20)
        self.technology_entry.place(relx=0.35, rely=0.73, anchor="center")

        # Health_wellness Spinbox
        self.health_wellness_entry = Spinbox(self.root, font=(None, 14), from_=0, to=10000, width=20)
        self.health_wellness_entry.place(relx=0.65, rely=0.73, anchor="center")

        # Miscellaneous Spinbox
        self.miscellaneous_entry = Spinbox(self.root, font=(None, 14), from_=0, to=10000, width=20)
        self.miscellaneous_entry.place(relx=0.35, rely=0.81, anchor="center")
        
        self.payment_options = ["Credit/Debit Card", "Cash", "Mobile Payment App"]
        self.selected_option = StringVar()
        self.selected_option.set(self.payment_options[0])
        
        self.payment_entry = OptionMenu(self.root, self.selected_option, *self.payment_options)
        self.payment_entry.place(relx=0.65, rely=0.81, anchor="center")
        self.payment_entry.config(width=31)
        
        self.statistics_button = Button(self.root, text="Statistics", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.open_statistics_page, width=15, height=2)
        self.statistics_button.place(relx=0.5, rely=0.65, anchor="center")
        self.statistics_button.place(relx=0.35, rely=0.9, anchor="center")

        self.logout_button = Button(self.root, text="Logout", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.open_main_page, width=15, height=2)
        self.logout_button.place(relx=0.5, rely=0.75, anchor="center")
        self.logout_button.place(relx=0.65, rely=0.9, anchor="center")

        self.root.mainloop()

    def open_statistics_page(self):
        self.root.destroy()
        #statisticspage.StatisticsDisplay(self.username)

    def open_main_page(self):
        self.root.destroy()
        mainpage.MainPage()
        

if __name__ == "__main__":
    profile_page = ProfilePage("Username")
