import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge


df=pd.read_csv("/home/trungsanglong25/Desktop/historical_RAPTOR_by_player.csv")
df.columns=["name","id","season","poss","minutes_played","offense","defense","total","war_total","war_reg_season","war_playoffs","predator_offense","predator_defense","predator_total","pace_impact"]
print(df)
print()

print("Describe")
print(df.describe())
print()

#player stat sort by season
print("Player stat sort by season")
print(df.corr()["season"].sort_values())
print()

print(df["pace_impact"].isnull().value_counts())
df["pace_impact"]=df["pace_impact"].replace(np.nan,df["pace_impact"].astype("float").mean())
print()

#predict
# print(df.columns)
features=["offense","defense","total","predator_offense","predator_defense","predator_total","pace_impact"]

#train_test_split
x_train,x_test,y_train,y_test=train_test_split(df[features],df["war_playoffs"],test_size=0.3,random_state=42)

#train by linear regression
lm=LinearRegression()
lm.fit(x_train,y_train)
print(lm.predict(x_test))

#Input: 'offense', 'defense', 'total', 'predator_offense', 'predator_defense','predator_total', 'pace_impact'

#predict by Linear Regression
print(x_test.columns)
print(x_test)
print("predict by Linear Regression: ",lm.predict(x_test))
print()
#predict by pipeline
sd=StandardScaler()
pf=PolynomialFeatures()

Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]

pipe=Pipeline(Input)
pipe.fit(x_train,y_train)
print("predict by Pipeline: ",pipe.predict(x_test))
print()
df.to_csv("player.csv")