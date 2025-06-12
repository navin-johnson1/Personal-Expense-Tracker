#PERSONAL EXPENSE TRACKER

from datetime import datetime
import csv
import pandas as pd

#Global variable
expenses = []

#Function to load the expenses
def addexpense(expenses):
    #Enter date
    date = input("Enter the date (YYYY-MM-DD):")
    while date == '':
        date = input("Date cannot be empty. Enter the date (YYYY-MM-DD):")
    
    #Enter category
    category = input("Enter the category (Food, Travel, Entertainment etc):")
    while category == '':
        category = input("Category cannot be empty. Enter the category (Food, Travel, Entertainment etc):")
    
    #Enter amount
    amount1 = input("Enter the amount spent:")
    while True:
        if amount1 == '':
            amount1 = input("Amount cannot be empty. Enter the amount spent:")
            continue
        if amount1.replace('.', '', 1).isdigit():
            amount = float(amount1)
            if amount > 0:
                break
            else:
                amount1 = input("Amount must be greater than 0. Enter the amount spent:")
        else:
            amount1 = input("Invalid amount. Enter a numeric value for the amount spent:")
    
    #Enter description
    description = input("Description:")
    while description == '':
        description = input("Description cannot be empty. Description:")
    
    #Create the dictionary
    entry = {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }
    
    #Append latest entry to the array
    expenses.append(entry)
    
    #Asking user if they want to view the expenses
    view_option = input("Do you want to view your expenses? Yes or no?")
    if view_option == "Yes" or view_option == "yes" or view_option == "YES" or view_option == "Y" or view_option == "y":
        viewexpense(expenses)
    
    # Save expenses to file
    saveexpense(expenses)
    
    return expenses


#Function to view expenses
def viewexpense(expenses):
    #Prints all the expenses
    print(expenses)

#Function to compare the budget with expense
def comparebudgetwithexpense(budget, expenses):
    totalexpense = 0
    for i in expenses:
        totalexpense = totalexpense + i['Amount']
        #print("Total expense" + str(totalexpense))

    if totalexpense <= budget:
        print("You are within budget")
        diff = budget - totalexpense
        print("You have $" + str(diff) + " left for the month")
    else:
        print("You have exceeded your budget!")
        diff = totalexpense - budget
        print("You went over by $" + str(diff))

#Function to track the user's budget
def trackexpense(expenses):
    #Insert monthly budget
    budget = float(input("Please enter your monthly budget:"))
    #Calling the comparison function
    comparebudgetwithexpense(budget, expenses)

def saveexpense(expenses):
   df = pd.DataFrame(expenses)
   df.to_csv('expenses.csv', index = False)
 
expenses = loadexpenses()
print("Hello! Welcome to your Personal Expense Tracker. What would you like to do today?")
while True:
    print("Option 1: Add an expense")
    print("Option 2: View your expenses")
    print("Option 3: Track budget")
    print("Option 4: Save expensese")
    print("Option 5: Exit")
    option = int(input("Enter your choice (Acceptable values are 1, 2, 3, 4 and 5):\n"))
    
    if option == 1:
        while True:
            expenses = addexpense(expenses)
            value = input("Do you want to add more expenses? Yes or no?")
            if value == "No" or value == "no" or value == "NO" or value == "N" or value == "n":
                break
    elif option == 2:
        viewexpense(expenses)
    elif option == 3:
        trackexpense(expenses)
    elif option == 4:
        saveexpense(expenses)
    elif option == 5:
        print("Thanks for your time!")
        break
    else:
        print("Invalid option!")
        break