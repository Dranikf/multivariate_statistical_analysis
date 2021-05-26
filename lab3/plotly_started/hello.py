import plotly.graph_objects as go
import random

my_frames = []

for i in range(200):
    my_frames.append(go.Frame(data = [go.Scatter(x = [random.random()*10, random.random()*10], y = [random.random()*10, random.random()*10])]))



fig = go.Figure(
    data=[go.Scatter(x=[0, 1], y=[0, 1])],
    layout=go.Layout(

        title="Start Title",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ),
    frames=my_frames
)

fig.show()