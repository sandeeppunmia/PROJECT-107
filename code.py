import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
student_df = df.loc[df['student_id']=="TRL_xsl"]
print(student_df)

df = pd.read_csv('data.csv')
fig = px.scatter(df,x='student_id',y='level',color='attempt')
fig.show()