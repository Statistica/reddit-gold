# Written by Jonathan Saewitz, released March 26th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import json, plotly.plotly as plotly, plotly.graph_objs as go

########################
#        Config        #
########################

graph_title="Reddit Gold Given By Month"

x_axis_title="Date"
y_axis_title="# of Reddit Gold given"

filename="gold_by_month.json"
########################
#      End Config      #
########################


months=[]
gilds=[]
for line in open(filename, 'r'):
	cur_line=json.loads(line)
	cur_year=cur_line['cur_year'][2:]
	months.append(cur_line['cur_month'] + "/" + cur_year)
	gilds.append(int(cur_line['gilded']))

trace = go.Bar(
    x = months,
    y = gilds
)

layout=go.Layout(
	title=graph_title,
	xaxis=dict(
		title=x_axis_title,
	),
	yaxis=dict(
		title=y_axis_title,
	)
)

data=[trace]
fig = go.Figure(data=data, layout=layout)
plotly.plot(fig)
