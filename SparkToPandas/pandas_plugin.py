"""
SparkToPandas Documentation
-----------------------------

SparkToPandas is a simple plugin alongside of spark, the SparkToPandas was designed to work with pyspark with a syntax more similar to pandas.

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class spark_pandas:
    """
    A supporting functions for pyspark ,which has the syntax similar to pandas
    """

    def __init__(self, spark):
        """

        Accepts the SparkSession as the input

        :param spark: class

        """
        self.spark = spark

    def read_csv(self, file_location, header=True):
        """

        Function to read csv file as a spark rdd

        :param file_location: str
        :param header: bool

        :return: rdd

        """
        df = self.spark.read.csv(file_location, header=header)
        return df

    def read_excel(self, file_location, sheet_name):
        """
        Function to read excel sheet

        :param file_location: str
        :param sheet_name: str

        :return: dataframe

        """
        df = self.spark.read.format("com.crealytics.spark.excel") \
            .option("useHeader", "true") \
            .option("inferSchema", "true") \
            .option("dataAddress", sheet_name) \
            .load(file_location)
        return df

    def read_json(self, file_location):
        """
        Function to read json data

        :param file_location: str

        :return: json obj

        """
        json_obj = self.spark.read.json(file_location)
        return json_obj


    def conditional_func(self, x):
        """

        A sample function, to add x+1 number

        :param x: int

        :return: int

        """
        return x + 1

    def column_creator(self, df, primary_column, new_column_name, user_func):
        """

        Creates a new column based on user defined function and returns the new rdd

        :param df: dataframe
        :param primary_column: str
        :param new_column_name: str
        :param user_func: function

        :return: dataframe

        """
        new_df = df.withColumn(new_column_name, user_func(df[primary_column]))
        return new_df

    def head(self, df, n):
        """

        Prints the head and tail of the dataframe depending on user's choice.

        :param df: dataframe
        :param n: int

        :return: None

        """
        new_df = pd.DataFrame(df.tail(-(n)), columns=df.columns) if n < 0 else pd.DataFrame(df.head(n),
                                                                                            columns=df.columns)
        print(new_df)

    def subset_columns(self, column_names, df):
        """

        Returns a dataframe which the user specified column names.

        :param column_names: list
        :param df: dataframe

        :return: dataframe

        """
        new_df = df.select(*column_names)
        return new_df

    def sort_df(self, df, col_name, ascending=True):
        """

        Function to sort the dataframe in ascending or descending order based on the columns given

        :param df: dataframe
        :param col_name: list
        :param ascending: bool

        :return: dataframe

        """
        return df.sort(col_name, ascending=ascending)

    def drop_na(self, df, col_name=None):
        """

        Drops null values based on user choice. Supports dropping all null values or dropping null values based on column subset

        :param df: dataframe
        :param col_name: str

        :return: dataframe

        """
        if col_name == None:
            return df.na.drop()
        else:
            return df.na.drop(subset=col_name)

    def fillna(self, df, value, col_name=None):
        """

        Fills null values based on user choice.

        :param df: dataframe
        :param value: int/str/float
        :param col_name: str

        :return: dataframe

        """
        if col_name == None:
            return df.na.fill(value)
        else:
            return df.na.fill(value, subset=col_name)

    def describe(self, df, col = None):
        """
        Function to display the basic stats of the dataframe
        :param df: dataframe
        :param col: str
        :return: display attr
        """
        if col == None:
            return df.describe().display()
        else:
            return df.describe([col]).display()


    def print_schema(self, df):
        """
        Function to print the schema of the table:

        :param df: dataframe

        :return: Schema
        """
        return df.printSchema()

    def change_schema(self, df, columns, dataType):
        """
        Function to change the schema of the table

        :param df: dataframe
        :param columns: list
        :param dataType: list

        :return: dataframe

        """
        print("=="*20)
        print("Existing Schema : ")
        df.printSchema()
        print("==" * 20)
        print("Changing Schema : ")
        for idx in range(len(columns)):
            df = df.withColumn(columns[idx],df[columns[idx]].cast(dataType[idx]))
        print("New Schema : ")
        df.printSchema()
        return df

    def barChart(self, df, x, y, hue, title, aspect='horizontal'):
        """

        Plots a barchart using the seaborn module

        :param df: dataframe
        :param x: str
        :param y: str
        :param hue: str
        :param title: str
        :param aspect: str

        :return: None

        """
        df = df.toPandas()
        if aspect == "horizontal":
            try:
                df[y] = df[y].astype(int)
            except ValueError:
                df[y] = df[y].astype(float)
        else:
            try:
                df[x] = df[x].astype(int)
            except ValueError:
                df[x] = df[x].astype(float)

        sns.catplot(x=x, y=y, hue=hue, data=df, kind="bar")
        plt.title(title)
        plt.show()
