#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt

expenses = {
    'Rent': 15000,
    'Groceries': 5000,
    'Utilities': 3000,
    'Transport': 2000,
    'Savings': 10000
}

income = 35000
total_expense = sum(expenses.values())
balance = income - total_expense

print("Remaining Balance:", balance)

# Visualization
labels = expenses.keys()
sizes = expenses.values()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Monthly Expenses Distribution")
plt.show()

