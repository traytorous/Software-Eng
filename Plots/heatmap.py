import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')

data = [go.Heatmap(x=df['Day'],
                   y=df['WeekofMonth'],
                   z=df['Recovered'].values.tolist(),
                   colorscale='Jet')]

layout = go.Layout(title='Corona Virus Recovered Cases',
                   xaxis_title="Day of Week", yaxis_title="Week of Month")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')