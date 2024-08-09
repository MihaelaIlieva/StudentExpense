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
    
    
# if the incomes are bigger than the expenses, i.e. they are enough
def can_save_money(incomes, expenses):
    return incomes > expenses


def get_average_tuition(data_frame):
    return ((data_frame['Tuition']/12) / data_frame['Monthly_expenses'] * 100).mean()


def get_average_factor(data_frame, factor_name):
    return ((data_frame[factor_name]) / data_frame['Monthly_expenses'] * 100).mean()

def get_debtor_percentage(data_frame):
    debtors =np.array(data_frame["Index"][data_frame["Monthly_incomes"]<data_frame["Monthly_expenses"]])
    return debtors

data_frame = read_file("D:\StrypesLab\StudentExpense\StudentExpense\expenses.csv")
make_user_statistics(0,"gay","freshman", "cs", 1500, 300, 1000, 1200, 300, 50, 30, 100, 70, 30, 75, 150, "card")
print(get_debtor_percentage(data_frame))

# # average values in prc
# AVG_TUITION_PRC = get_average_tuition(data_frame)
# AVG_HOUSING_PRC = get_average_factor(data_frame,"Housing")
# AVG_FOOD_PRC = get_average_factor(data_frame,"Food")
# AVG_TRANSPORTATION_PRC = get_average_factor(data_frame,"Transportation")
# AVG_BOOKS_PRC = get_average_factor(data_frame,"Books_supplies")
# AVG_ENTERTAINMENT_PRC = get_average_factor(data_frame, "Entertainment")
# AVG_PERSONAL_CARE_PRC = get_average_factor(data_frame,"Personal_Care")
# AVG_TECHNOLOGY_PRC = get_average_factor(data_frame,"Technology")
# AVG_HEALTH_WELLNESS_PRC = get_average_factor(data_frame,"Health_wellness")
# avg_prc = [AVG_TUITION_PRC, AVG_HOUSING_PRC, AVG_FOOD_PRC, AVG_TRANSPORTATION_PRC, AVG_BOOKS_PRC, 
#            AVG_ENTERTAINMENT_PRC, AVG_PERSONAL_CARE_PRC, AVG_TECHNOLOGY_PRC, AVG_HEALTH_WELLNESS_PRC]
# AVG_MISCELLANEOUS_PRC = 100 - np.sum(avg_prc)
# avg_prc.append(AVG_MISCELLANEOUS_PRC)


# current_person = [10, 10, 10, 20, 10, 5, 10, 15, 10]

# diff = current_person - avg_prc
# sorted = sorted(diff)

# for i in diff:
#     # bigger than average
#     if i > 0:
#         pass



