
import pandas as pd

df = pd.read_csv(r"F:\Data Analytics\Projects\FULL DATASET\customer_shopping_behavior.csv")



# data formating

df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
df = df.rename(columns = {'purchase_amount_(usd)' : 'purchase_amount'})

#data cleaning
print(df.head(5))
print(df.info())

print(df.isnull().sum())

# filling null values by median of each category

df['review_rating'] = df.groupby('category')['review_rating'].transform(lambda x : x.fillna(x.median()))

print(df.isnull().sum())

#create ellsential columns

labels = ['young_adult', 'adult', 'middle_age', 'senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
print(df.head())

#delete extra columns

print(df[['discount_applied', 'promo_code_used']].head())

print((df['discount_applied'] == df['promo_code_used']).all())

df = df.drop('promo_code_used', axis=1)
print(df.head(5))



# data import into sql 

    

from sqlalchemy import create_engine

username = "root"
password = "SSSSS5"
host     = "localhost"
port     = "3306"
database = "customerdb"

engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}")

df.to_sql("customers", con=engine, if_exists="replace", index=False)
print("Data transfer into SQL successfully")