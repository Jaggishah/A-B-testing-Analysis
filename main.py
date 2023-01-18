import pandas as pd
import datetime
from datetime import date , timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

control_data = pd.read_csv("control_group.csv",sep = ';')
test_data = pd.read_csv("test_group.csv",sep = ';')
print(control_data.head())
print(test_data.head())
control_data.columns = ["Campaign Name", "Date", "Amount Spent", 
                        "Number of Impressions", "Reach", "Website Clicks", 
                        "Searches Received", "Content Viewed", "Added to Cart",
                        "Purchases"]
test_data.columns = ["Campaign Name", "Date", "Amount Spent", 
                        "Number of Impressions", "Reach", "Website Clicks", 
                        "Searches Received", "Content Viewed", "Added to Cart",
                        "Purchases"]
# print(control_data.head())
# print(test_data.head())

print(control_data.isnull().sum())

print(test_data.isnull().sum())


# has to fill null values..

control_data["Number of Impressions"].fillna(value=control_data["Number of Impressions"].mean(), 
                                             inplace=True)
control_data["Reach"].fillna(value=control_data["Reach"].mean(), 
                             inplace=True)
control_data["Website Clicks"].fillna(value=control_data["Website Clicks"].mean(), 
                                      inplace=True)
control_data["Searches Received"].fillna(value=control_data["Searches Received"].mean(), 
                                         inplace=True)
control_data["Content Viewed"].fillna(value=control_data["Content Viewed"].mean(), 
                                      inplace=True)
control_data["Added to Cart"].fillna(value=control_data["Added to Cart"].mean(), 
                                     inplace=True)
control_data["Purchases"].fillna(value=control_data["Purchases"].mean(), 
                                 inplace=True)

A_Bdata = control_data.merge(test_data,how="outer").sort_values(["Date"])
A_Bdata = A_Bdata.reset_index(drop=True)

print(A_Bdata.head())

print(A_Bdata["Campaign Name"].value_counts())

figure  = px.scatter(
                    data_frame=A_Bdata,
                    x = "Number of Impressions",
                    y = "Amount Spent",
                    size= "Amount Spent",
                    color="Campaign Name",
                

)
figure.show()