def names_fix(name):
    '''This function takes repeated string values in a column and covert them into one single values '''
    for k, v in cult.items():
        if name.lower() in v:
            return k


"""
Some functions to help cleaning and handling dataframes.
"""
import pandas as pd
def report_missing_values(df):
    """Print a pretty report of missing values."""
    print(pd.DataFrame().isnull())




class Person:
     def __init__(self, name, age):
         self.name = name
         self.name = age

     def introduceyourself(self):
         print("My name is " + self.name)
         print('My age is '+ str(self.age))

author = Person(input('Whats your name?')

