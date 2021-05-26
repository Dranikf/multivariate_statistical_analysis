import plotly.express as px

df = px.data.gapminder()

print(df)

#fig = px.bar(df, x="continent", y="pop", color="continent",
#  animation_frame="year", animation_group="country", range_y=[0,4000000000])

fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

fig.show()