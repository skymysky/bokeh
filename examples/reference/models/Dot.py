import numpy as np

from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, Dot, Grid, LinearAxis, Plot

N = 9
x = np.linspace(-2, 2, N)
y = x**2
sizes = np.linspace(10, 20, N)

source = ColumnDataSource(dict(x=x, y=y, sizes=sizes))

plot = Plot(
    title=None, plot_width=300, plot_height=300,
    min_border=0, toolbar_location=None)

glyph = Dot(x="x", y="y", size="sizes", line_color="#dd1c77", fill_color=None)
plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

curdoc().add_root(plot)

show(plot)
