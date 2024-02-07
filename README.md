# recipes-etl

### Packages used
- pandas
- os
- urllib3
- json
- os

In order to run the code you need to open it in the interpreter/editor of your choice. I personally used PyCharm but Spyder or Anaconda work as well. To install the packages/libraries utilised open the terminal belonging to your Python environment.

In the terminal, download and install the packages using the following command : pip install .... (the package name on the place of the dots).

Wait untill the previous one is installed in your Python environment and repeat the process untill all of the packages are installed. 


### Python version used
I have used Python version 3.9.18.

### How to run

To run the ETL, open the ETL.py file in your interpreter and make sure all of the packages are installed and that the recipes.json file is present in the same directory as the .py file. Then connect your interpreter to the Python environment in which you installed the necessary packages. Then run the file, it will create the .csv file in the same directory as the .py file. 

### What it does and how it works

This ETL loads a json file from the url provided. As the json file was not yet formatted in the right way (not separated by commas and put between two [], it loads it using list comprehension in combination with the loads function from the json library. It goes through the url line by line. 

In case one is not connected to the internet, I have build in a try-except clause that will still run with the use of the downloaded recipes.json file. Just like the url part, this one goes through the json file line by line and loads in into a pandas dataframe. 

After loading in the data, the script filters the dataframe to only give the rows that have some form of chile in their ingredients. This includes misspellings and the singular form of the words (so chile, chili, chilies, chiles, chilis). By filtering for chile and chili, this will encompass all options. 

Then, in order to add the cookTime and prepTime columns together to get the total cooking time, the columns need to be of the numeric type. As the cells in the column are strings and can thus also contain empty strings or letters/special characters. So first those need to be removed. This script achieves this by using a regex expression combined with the replace function. This replaces all non-numeric characters in the prepTime and cookTime columns by an empty string. Afterwards the columns can be converted to the numeric type with the help of the to_numeric function from the pandas library. The empty strings get replaced by NAN values, but this does not affect the original dataframe, and does not impact the addition of the columns. 

Then the script determines the difficulty by use of list comprehension as well. First the two columns (output from previous function) are summed together along the 1 axis (along the rows). The sum function ignores NAN values, so summing will result in non-NAN values, even if one of the the columns contain one. 

Then using list comprehension with a couple of nested if else statements it adds a new column to the dataframe, containing the difficulty of the recipes, based on the total of the cookTime and the prepTime (totalTime > 60 min then Hard, 30 min < totalTime < 60 min and Easy when < 30 min). When the column is empty or if the value falls outside of the indicated ranges, the difficulty will state 'Unknown'. 

Then finally, it writes the resulting dataframe to a csv file in the same folder as the .py file it is running. It finds the current directory using the os.getcwd() function, and creates the csv there using to_csv from the pandas library. To confirm the file is created, it prints a statement that it has succeeded and the location in which it is placed. 
