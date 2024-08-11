import profilepage
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from tkinter import Tk, Label, Button, TOP, BOTH

class StatisticsDisplay:

    def __init__(self, username, age, gender, year, major, income, aid, tuition, housing, food,
                                         transportation, books_supplies, entertainment, personal_care, technology,
                                         health_and_wellness, miscellaneous, payment_method):
        # The window
        self.root = Tk()
        
        # The parameters
        self.username = username
        self.age = np.int32(age)
        self.gender = gender
        self.year = year
        self.major = major
        self.income = np.int32(income)
        self.aid = np.int32(aid)
        self.tuition = np.int32(tuition)
        self.housing = np.int32(housing)
        self.food = np.int32(food)
        self.transportation = np.int32(transportation)
        self.books_supplies = np.int32(books_supplies)
        self.entertainment = np.int32(entertainment)
        self.personal_care = np.int32(personal_care)
        self.technology = np.int32(technology)
        self.health_and_wellness = np.int32(health_and_wellness)
        self.miscellaneous = np.int32(miscellaneous)
        self.payment_method = payment_method
        
        
        # Screen configurations
        self.root.title("Statistics")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.config(bg='#346c99')

        self.title_font = (None, 16, "bold")
        self.stats_font = (None, 12)
        self.highlight_color = '#ffb300'
        
        self.MAIN_COLOUR = '#346c99'
        self.FONT_COLOUR = '#8c198f'
        self.FONT_COLOUR = '#ffffff'
        
        self.profile_page_button = Button(self.root, text="Profile page", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.back_to_profile, width=15, height=2)
        self.profile_page_button.place(relx=0.95, rely=0.03, anchor="center")
        
        self.statistics_label = Label(self.root, text="Check your statistics here", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.statistics_label.place(relx=0.5, rely=0.10, anchor="center")
        
        text_info = f"{self.username}, {self.age}, {self.gender}, {self.year}, {self.major}, {self.payment_method}"
        
        self.info_label = Label(self.root, text=text_info, font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.info_label.place(relx=0.5, rely=0.15, anchor="center")
        
        text_addition = f"""Monthly income:{self.income}, Tuition:{self.tuition}, Housing:{self.housing}, Food:{self.food}, 
        Transportation:{self.transportation}, Books:{self.books_supplies}, Entertainment:{self.entertainment},
        Personal care:{self.personal_care}, Technology:{self.technology}, Health and wellness:{self.health_and_wellness}, Miscellaneous:{self.miscellaneous}"""
        
        self.info_label = Label(self.root, text=text_addition, font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.info_label.place(relx=0.5, rely=0.20, anchor="center")
        
        self.pie_button = Button(self.root, text="Budget breakdown", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.show_basic_pie_chart, width=15, height=2)
        self.pie_button.place(relx=0.44, rely=0.30, anchor="center")
        
        self.advice_button = Button(self.root, text="Advice on budget", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.show_advice, width=15, height=2)
        self.advice_button.place(relx=0.56, rely=0.30, anchor="center")
        
        self.tuition_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.tuition_label.place(relx=0.30, rely=0.45, anchor="center")
        
        self.housing_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.housing_label.place(relx=0.30, rely=0.50, anchor="center")
        
        self.food_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.food_label.place(relx=0.30, rely=0.55, anchor="center")

        # Transportation
        self.transportation_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.transportation_label.place(relx=0.30, rely=0.60, anchor="center")

        # Books_supplies
        self.books_supplies_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.books_supplies_label.place(relx=0.30, rely=0.65, anchor="center")

        # Entertainment
        self.entertainment_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.entertainment_label.place(relx=0.30, rely=0.70, anchor="center")

        # Personal_care
        self.personal_care_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.personal_care_label.place(relx=0.30, rely=0.75, anchor="center")

        # Technology
        self.technology_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.technology_label.place(relx=0.30, rely=0.80, anchor="center")

        # Health_wellness
        self.health_wellness_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.health_wellness_label.place(relx=0.30, rely=0.85, anchor="center")

        # Miscellaneous
        self.miscellaneous_label = Label(self.root, font=(None, 12), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.miscellaneous_label.place(relx=0.30, rely=0.90, anchor="center")

        self.root.mainloop()

    def back_to_profile(self):
        username = self.username
        self.root.destroy()
        profilepage.ProfilePage(username)
        
    def create_user_dataframe(self):
        data = {
        'Username': [self.username],
        'Age': [self.age],
        'Gender': [self.gender],
        'Year_in_school': [self.year],
        'Major': [self.major],
        'Monthly_income': [self.income],
        'Aid': [self.aid],
        'Tuition': [self.tuition*12],
        'Housing': [self.housing],
        'Food': [self.food],
        'Transportation': [self.transportation],
        'Books_supplies': [self.books_supplies],
        'Entertainment': [self.entertainment],
        'Personal_care': [self.personal_care],
        'Technology': [self.technology],
        'Health_wellness': [self.health_and_wellness],
        'Miscellaneous': [self.miscellaneous],
        'Payment_method': [self.payment_method]
        }

        df = pd.DataFrame(data)
        return df
        
    def show_basic_pie_chart(self):
        
        self.make_user_statistics(self.username, self.age, self.gender, self.year, self.major, self.income, self.aid,
                        self.tuition, self.housing, self.food, self.transportation, self.books_supplies, self.entertainment,
                        self.personal_care, self.technology, self.health_and_wellness, self.miscellaneous, self.payment_method, self.root)
    
    def show_advice(self):
        # Reads the information
        df = self.read_file("D:\StrypesLab\StudentExpense\StudentExpense\expenses.csv")
        print(df)

        # Static analisys parameter
        static_features = ['Monthly_income']

        # Parameters for the analisys
        features = [ 'Tuition', 'Housing', 'Food', 'Transportation', 
                    'Books_supplies', 'Entertainment', 'Personal_care', 
                    'Technology', 'Health_wellness', 'Miscellaneous']

        # What is the common characteristic
        categorical_feature = ['Year_in_school']

        # Grouping by characteristic
        groups = df.groupby(categorical_feature)


        # Get info on the current member
        current_user_data = self.create_user_dataframe()
        user_group =current_user_data[categorical_feature].values[0][0]

        # The user's group that we need to inspect
        group = groups.get_group(user_group)

        anomalyValues = {}
            
        # foreach feature other than monthly income 
        # construct a pair such as Monthly_Income vs X 
        # to create a 2d data subset to use isolation forest algorithm on

        for feature2 in features:
            
            forest = self.fit_forest(group, static_features[0], feature2)

            # is only the current user
            anomaly_val = self.calc_decision_function(forest, current_user_data, static_features[0], feature2)[0]
            anomaly_name = static_features[0] + "_" + feature2
            anomalyValues[anomaly_name] = anomaly_val

            # Shows the plot of the forest
            self.plot_forest(group, user_group, static_features[0], feature2)
            
        # Prints the values of the user
        print(anomalyValues)
        
        okay_text = "You are managing this just fine!"
        not_okay_text = "You can reevaluate this category's budgeting!"
        
        text_array = []
        
        # Check which values are okay and which need to be overlooked again
        for key, value in anomalyValues.items():
            if value < 0:
                text_array.append(not_okay_text)
            else:
                text_array.append(okay_text)
        
        # Add the feedback
        self.tuition_label.config(text=f"Tuition: {text_array[0]}")
        self.housing_label.config(text=f"Housing: {text_array[1]}")
        self.food_label.config(text=f"Food: {text_array[2]}")
        self.transportation_label.config(text=f"Transportation: {text_array[3]}")
        self.books_supplies_label.config(text=f"Books supplies: {text_array[4]}")
        self.entertainment_label.config(text=f"Entertainment: {text_array[5]}")
        self.personal_care_label.config(text=f"Personal care: {text_array[6]}")
        self.technology_label.config(text=f"Technology: {text_array[7]}")
        self.health_wellness_label.config(text=f"Health and wellness: {text_array[8]}")
        self.miscellaneous_label.config(text=f"Miscellaneous: {text_array[9]}")
        

    # adding a new column to the data frame, specifically needed for sum of incomes and expenses

    def add_incomes_column(self, data_frame, column_name):
        
        income_columns = ['Monthly_income', 'Financial_aid']
        data_frame[column_name] = np.int64(data_frame[income_columns].sum(axis=1))
        
        return data_frame


    def add_expenses_column(self, data_frame, column_name):
        
        expense_columns = ['Tuition', 'Housing', 'Food', 'Transportation', 'Books_supplies', 
                    'Entertainment', 'Personal_care', 'Technology', 'Health_wellness', 
                    'Miscellaneous']
        
        # remove 11 times the tuition because it is annual
        data_frame[column_name] = np.int64(data_frame[expense_columns].sum(axis=1) - data_frame["Tuition"]*11/12)
        
        return data_frame

    # reading the csv with the correct separator for the columns and adding needed columns
    def read_file(self, path_to_file):
        
        data_frame = pd.read_csv(path_to_file, sep=';')
        data_frame = self.add_incomes_column(data_frame, "Monthly_incomes")
        data_frame = self.add_expenses_column(data_frame, "Monthly_expenses")
        
        return data_frame

    # get user's financial breakdown as pie chart
    def make_user_statistics(self, username, age, gender, year_in_school, major, monthly_income, financial_aid,
                            tuition, housing, food, transport, book_supplies, entertainment,
                            personal_care, technology, health_Wellness, miscellaneous, payment_method, root):
        
        
        labels = ["Monthly tuition", "Housing", "Food", "Transport", "Book supplies", "Enterntainment",
                "Personal care", "Technology", "Health and wellness", "Miscellaneous"]
        
        data = np.array([tuition/12, housing, food, transport, book_supplies, entertainment,
                            personal_care, technology, health_Wellness, miscellaneous])
        
        max_index = np.argmax(data)
        explode_array = [0.1 if i == max_index else 0 for i in range(len(data))]
        
        plt.pie(data, labels=labels, startangle=0, explode=explode_array, autopct="%1.1f%%")
        plt.show()
    
    # if the incomes are bigger than the expenses, i.e. they are enough
    def can_save_money(self, incomes, expenses):
        return incomes > expenses


    def get_average_tuition(self, data_frame):
        return ((data_frame['Tuition']/12) / data_frame['Monthly_expenses'] * 100).mean()


    def get_average_factor(self, data_frame, factor_name):
        return ((data_frame[factor_name]) / data_frame['Monthly_expenses'] * 100).mean()


    def get_debtor_percentage(self, data_frame):
        debtors =np.array(data_frame["Index"][data_frame["Monthly_incomes"]<data_frame["Monthly_expenses"]])
        return debtors
    
    
    def plot_forest(self, group, title_prefix, parameter1, parameter2):

        anomaly_name = parameter1 + "_" + parameter2

        plt.figure(figsize=(10, 6))
        plt.scatter(group[parameter1],
                    group[parameter2],
                    c=group["AnomalyScore_" + anomaly_name],
                    cmap='coolwarm', edgecolor='k')
        plt.xlabel(parameter1)
        plt.ylabel(parameter2)
        plt.title(title_prefix + " " +  parameter1 + "   vs   " +  parameter2)
        plt.colorbar(label='Anomaly Status (Cold = Anomaly, Warm = Normal)')
        plt.grid(True)
        plt.show()

    # Takes the tree and based on wanted features creates the decision function
    def calc_decision_function(self, iso_forest, data, parameter1, parameter2):
        
        features = data[[parameter1,parameter2]]
        # Compute the anomaly scores using decision_function
        return iso_forest.decision_function(features)

    # Returns the forest
    def fit_forest(self, data, parameter1, parameter2):
        # Selecting the relevant columns for Isolation Forest
        #features = df[['Year_in_school_encoded', 'Tuition']]
        features = data[[parameter1, parameter2]]
        anomaly_name = parameter1 + "_" + parameter2

        # Initialize and fit the Isolation Forest model
        iso_forest = IsolationForest(n_estimators=500, contamination=0.05)
        # Creates the tree for the given number of dividors
        iso_forest.fit(features)
        # Store the data for plotting
        # How certain it is that it is an anomaly for each point
        # outliers are < 0 inliners are > 0 
        data["AnomalyScore_" + anomaly_name] = iso_forest.decision_function(features)
    
        return iso_forest
    
    
if __name__ == "__main__":
    username = "mihinka"
    app = StatisticsDisplay(username, 22, "Female", "Senior", "Computer Science", 1000, 450, 150, 600, 300, 15, 10, 50, 50, 15, 50, 100, "Cash")