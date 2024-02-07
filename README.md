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

This ETL loads a json file from the url provided. As the json file was not yet formatted in the right way (not separated by commas and put between two [], I load it using list comprehension in combination with the loads function from the json library. It goes through the url line by line. 

In case one is not connected to the internet, I have build in a try-except clause that will still run with the use of the downloaded recipes.json file. Just like the url part, this one goes through the json file line by line and loads in into a pandas dataframe. 

After loading in the data, the script filters the dataframe to only give the rows that have some form of chile in their ingredients. This includes misspellings and the singular form of the words (so chile, chili, chilies, chiles, chilis). By filtering for chile and chili, this will encompass all options. 
