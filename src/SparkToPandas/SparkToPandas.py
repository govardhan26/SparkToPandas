from pyspark.sql import SparkSession
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Spark_pandas:
    def __init__(self,spark):
        self.spark = spark

    def read_csv(self,file_location, header = True):
        df = self.spark.read.csv(file_location , header = header)
        return df

    def conditional_func(self,x):
        return x + 1

    def column_creator(self,df,primary_column, new_column_name,user_func):
        new_df = df.withColumn(new_column_name, user_func(df[primary_column]))
        return new_df

    def head(self,df,n):
        new_df = pd.DataFrame(df.tail(-(n)), columns=df.columns) if n < 0 else pd.DataFrame(df.head(n), columns=df.columns)
        print(new_df)

    def subset_columns(self,column_names,df):
        new_df = df.select(*column_names)
        return new_df

    def sort_df(self,df,col_name, ascending = True):
        return df.sort(col_name,ascending = ascending)

    def drop_na(self,df,col_name = None):
        if col_name == None:
            return df.na.drop()
        else:
            return df.na.drop(subset= col_name)

    def fillna(self,df,value, col_name = None):
        if col_name == None:
            return df.na.fill(value)
        else:
            return df.na.fill(value,subset= col_name)


    def barChart(self,df, x, y, hue, title, aspect = 'horizontal'):
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

        sns.catplot(x = x, y = y, hue = hue ,data = df, kind = "bar")
        plt.title(title)
        plt.show()








