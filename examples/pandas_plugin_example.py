'''
Examples of using the SparkToPandas Package:
'''

#Installation:
#pip install SparkToPandas

#Importing required packages:
from SparkToPandas.pandas_plugin import spark_pandas
from pyspark.sql import SparkSession

#initialize the spark session:
spark = SparkSession.builder.appName("MyApp").getOrCreate()
pd = spark_pandas(spark)

#read the csv file:
file_path = r'C:\Users\Home\Downloads\train_data_jigsaw.csv'
df = pd.read_csv(file_path)

#displaying first five rows
pd.head(df,5)

#displaying last five rows
pd.head(df,-5)

#subsetting columns:
print(df.columns)
new_df = pd.subset_columns(['id','comment_text'],df)
new_df.show()

#sorting the dataframe:
#ascending order
new_df = pd.sort_df(df,ascending = True , col_name = 'id')
new_df.show()

#descending order
new_df = pd.sort_df(df,ascending = False, col_name= "id")
new_df.show()

#fill null values
new_df = pd.fillna(df,value=5)
new_df.show()

#dropping null value:
new_df = pd.drop_na(df)
new_df.show()




