import csv
import plotly.express as px
with open("coffoe_vs_sleep.csv") as cs_file:
    df=csv.DictReader(cs_file)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
    fig.show()