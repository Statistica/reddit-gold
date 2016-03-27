# Written by Jonathan Saewitz, released March 27th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import json, plotly.plotly as plotly, plotly.graph_objs as go

########################
#        Config        #
########################
low_graph_title="Lowest Subscriber:Gold Subreddit Ratios"
high_graph_title="Highest Subscriber:Gold Subreddit Ratios"

x_axis_title="Subreddit"
y_axis_title="Subscriber:Gold ratio"

subreddits_to_graph=50

filename="gold_ratios.json"
########################
#      End Config      #
########################

f=open(filename, 'r')
file_lines=f.readlines()
f.close()

subreddits_low=[]
ratios_low=[]
subreddits_high=[]
ratios_high=[]
for line in range(subreddits_to_graph):
	cur_line=json.loads(file_lines[line])
	subreddits_low.append(cur_line['url'])
	ratios_low.append(float(cur_line['r']))

	cur_line=json.loads(list(reversed(file_lines))[line])
	subreddits_high.append(cur_line['url'])
	ratios_high.append(float(cur_line['r']))

layout=go.Layout(
	title=low_graph_title,
	xaxis=dict(
		title=x_axis_title,
	),
	yaxis=dict(
		title=y_axis_title,
	)
)

trace = go.Bar(
    x = subreddits_low,
    y = ratios_low
)

data=[trace]
fig = go.Figure(data=data, layout=layout)
plotly.plot(fig)

layout=go.Layout(
	title=high_graph_title,
	xaxis=dict(
		title=x_axis_title,
	),
	yaxis=dict(
		title=y_axis_title,
	)
)

trace = go.Bar(
    x = subreddits_high,
    y = ratios_high
)

data=[trace]
fig = go.Figure(data=data, layout=layout)
plotly.plot(fig)
