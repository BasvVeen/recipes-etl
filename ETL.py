import urllib.request
import urllib.error
import json
import pandas as pd
import os

cookTime = "cookTime"
prepTime = "prepTime"


def load_json_from_url(url):
    """This function returns the json data from an url in the form of a Pandas DataFrame."""

    try:
        with urllib.request.urlopen(url) as url_data:
            data = [json.loads(line) for line in url_data]

            dataframe = pd.DataFrame(data)

    except urllib.error.URLError:
        print("URLError: Not connected to the internet, using local file.")
        directory = os.getcwd()
        with open(directory + "\\recipes.json") as f:
            data = [json.loads(line) for line in f]

            dataframe = pd.DataFrame(data)

    return dataframe


def filter_recipes(ingredients, df):
    """This function returns the recipes in the dataframe that make use of certain ingredients. These ingredients
    should be contained in a list."""

    filtered_df = df[df['ingredients'].str.contains('|'.join(ingredients))].reset_index(drop=True)

    return filtered_df


def make_numeric(columns, dataframe):
    """This function returns the input columns as a numeric type by removing any .

    The inputs are the filtered dataframe and the columns you want to make numeric."""

    dataframe[columns] = dataframe[columns].replace(r'[\D]', '', regex=True)

    return dataframe[columns].apply(pd.to_numeric, errors="coerce")


def determine_difficulty(times, recipes):
    """This function determines the difficulty of a recipe based on the prepTime and cookTime. If the total time exceeds
        60 minutes, then it is hard, between 30 and 60 minutes, then medium, below 30 then easy, otherwise unknown.

        The inputs of the function are the two time columns from make_numeric and the dataframe."""

    total_time = times.loc[:, [cookTime, prepTime]].sum(axis=1)

    recipes["difficulty"] = total_time.apply(lambda x: "Hard" if x > 60 else ("Medium" if 30 < x < 60 else
                                                                             ("Easy" if 0 < x < 30 else "Unknown")))

    return recipes


def write_to_csv(output):
    directory = os.getcwd()

    output.to_csv(directory + "\\chilies_recipes_wdifficulty.csv", index=False)

    print("The csv file has been created at the following location: " + directory)

    return


def main():
    df = load_json_from_url("https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json")

    filtered_recipes = filter_recipes(["chile", "chili"], df)

    test = make_numeric([cookTime, prepTime], filtered_recipes)

    recipes_out = determine_difficulty(test, filtered_recipes)

    write_to_csv(recipes_out)


if __name__ == "__main__":
    main()
