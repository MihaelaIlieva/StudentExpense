import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
def make_user_statistics(username, age, gender, year_in_school, major, monthly_income, financial_aid,
                        tuition, housing, food, transport, book_supplies, entertainment,
                        personal_care, technology, health_Wellness, miscellaneous, payment_method, root):
    
    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)
    
    labels = ["Monthly tuition", "Housing", "Food", "Transport", "Book supplies", "Enterntainment",
              "Personal care", "Technology", "Health and wellness", "Miscellaneous"]
    
    data = np.array([tuition/12, housing, food, transport, book_supplies, entertainment,
                        personal_care, technology, health_Wellness, miscellaneous])
    
    max_index = np.argmax(data)
    explode_array = [0.1 if i == max_index else 0 for i in range(len(data))]
    
    ax.pie(data, labels=labels, startangle=0, explode=explode_array, autopct="%1.1f%%")
    
    # Create a canvas and add the figure to it
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    
    # Add the canvas to the Tkinter window
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    
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
 
# Creates a scatter plot
def plot_forest(group, titlePrefix, parameter1, parameter2):

    anomaly_name = parameter1 + "_" + parameter2

    plt.figure(figsize=(10, 6))
    plt.scatter(group[parameter1],
                group[parameter2],
                c=group["AnomalyScore_" + anomaly_name],
                cmap='coolwarm', edgecolor='k')
    plt.xlabel(parameter1)
    plt.ylabel(parameter2)
    plt.title(titlePrefix + " " +  parameter1 + "   vs   " +  parameter2)
    plt.colorbar(label='Anomaly Status (True = Anomaly, False = Normal)')
    plt.grid(True)
    plt.show()

# Takes the tree and based on wanted features creates the decision function
def calc_decision_function(iso_forest, data, parameter1, parameter2):
    
    features = data[[parameter1,parameter2]]
    # Compute the anomaly scores using decision_function
    return iso_forest.decision_function(features)
#    custom_threshold = -0.005 # Define your custom threshold here
#    # Apply the custom threshold
#    group['IsAnomaly'][anomaly_name] = group['AnomalyScores'][anomaly_name] < custom_threshold


# input is the data frame we are working on 
# with two paramets for the X and Y axis of the data
def fit_forest(data, parameter1, parameter2):
    # Selecting the relevant columns for Isolation Forest
    #features = df[['Year_in_school_encoded', 'Tuition']]
    features = data[[parameter1, parameter2]]
    anomaly_name = parameter1 + "_" + parameter2

    # Initialize and fit the Isolation Forest model
    iso_forest = IsolationForest(n_estimators=500, contamination=0.05)  # Adjust contamination parameter as needed
    # Creates the tree for the given number of dividors
    iso_forest.fit(features)
    # Store the data for plotting
    # How certain it is that it is an anomaly for each point
    data["AnomalyScore_" + anomaly_name] = iso_forest.decision_function(features)
    

    return iso_forest

df = read_file("D:\StrypesLab\StudentExpense\StudentExpense\expenses.csv")
print(df)

static_features = ['Monthly_income']

features = [ 'Tuition', 'Housing', 'Food', 'Transportation', 
            'Books_supplies', 'Entertainment', 'Personal_care', 
            'Technology', 'Health_wellness', 'Miscellaneous']

categorical_feature = ['Year_in_school']

label_encoder = LabelEncoder()
groups = df.groupby(categorical_feature)


# get info on the current member
current_user_data = df.iloc[0]
user_group =current_user_data[categorical_feature].values[0]

new_data_df = pd.DataFrame([current_user_data])

group = groups.get_group(user_group)

anomalyValues = {}
    
# foreach feature other than monthly income 
# construct a pair such as Monthly_Income vs X 
# to create a 2d data subset to use isolation forest algorithm on

for feature2 in features:
    forest = fit_forest(group, static_features[0], feature2)

    #get the first record as the decision function input
    # is only the current user
    anomaly_val = calc_decision_function(forest, new_data_df, static_features[0], feature2)[0]
    anomaly_name = static_features[0] + "_" + feature2
    anomalyValues[anomaly_name] = anomaly_val

    plot_forest(group, user_group, static_features[0], feature2)
    
print(anomalyValues)