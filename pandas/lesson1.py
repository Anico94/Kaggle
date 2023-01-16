# Lesson 1 of the kaggle pandas course

import pandas as pd 

#1

fruits = pd.DataFrame({"Apples": [30], "Bananas": [21]})

print(fruits)


#2

fruit_sales = pd.DataFrame({"Apples": [35,41], "Bananas":[21,34]}, index = ["2017 Sales", "2018 Sales"])

print(fruit_sales)

#3 

ingredients = pd.Series(["4 cups", "1 cup", "2 large", "1 can"], index = ['Flour', 'Milk', "Eggs", "Spam",], name = "Dinner")

print(ingredients)