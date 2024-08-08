import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# adding a new column to the data frame, specifically needed for sum of incomes and expenses

def add_incomes_column(data_frame, column_name):
    
    income_columns = ['Monthly_income', 'Financial_aid']
    data_frame[column_name] = np.int64(data_frame[income_columns].sum(axis=1))
    
    return data_frame

def add_expenses_column(data_frame, column_name):
    
    expense_columns = ['Tuition', 'Housing', 'Food', 'Transportation', 'Books_supplies', 
                   'Entertainment', 'Personal_care', 'Technology', 'Health_wellness', 
                   'Miscellaneous']
    # remove 11 times the tuition because it is annual
    data_frame[column_name] = np.int64(data_frame[expense_columns].sum(axis=1) - data_frame["Tuition"]*11/12)
    
    return data_frame

# reading the csv with the correct separator for the columns and adding needed columns
def read_file(path_to_file):
    
    data_frame = pd.read_csv(path_to_file, sep=';')
    data_frame = add_incomes_column(data_frame, "Monthly_incomes")
    data_frame = add_expenses_column(data_frame, "Monthly_expenses")
    
    return data_frame


# get user's financial breakdown as pie chart
def make_user_statistics(age, gender, year_in_school, major, monthly_income, financial_aid,
                        tuition, housing, food, transport, book_supplies, entertainment,
                        personal_care, technology, health_Wellness, miscellaneous, payment_method):
    
    labels = ["Monthly tuition", "Housing", "Food", "Transport", "Book supplies", "Enterntainment",
              "Personal care", "Technology", "Health and wellness", "Miscellaneous"]
    
    data = np.array([tuition/12, housing, food, transport, book_supplies, entertainment,
                        personal_care, technology, health_Wellness, miscellaneous])
    
    max_index = np.argmax(data)
    explode_array = [0.1 if i == max_index else 0 for i in range(len(data))]
    
    plt.pie(data, labels=labels, startangle=0, explode=explode_array, autopct="%1.1f%%")
    plt.show()
    

print(read_file("D:\StrypesLab\StudentExpense\expenses.csv"))
make_user_statistics(0,"gay","freshman", "cs", 1500, 300, 1000, 1200, 300, 50, 30, 100, 70, 30, 75, 150, "card")