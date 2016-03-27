# Written by Jonathan Saewitz, released March 26th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import json, plotly.plotly as plotly, plotly.graph_objs as go

########################
#        Config        #
########################
graph_title="Largest Subreddits Who Have Given 0 Gold"

x_axis_title="Subreddit"
y_axis_title="Subreddit size (subscribers)"

filename="zero_gildings.json"
########################
#      End Config      #
########################


subreddits=[]
subscribers=[]
f=open(filename, 'r')
for i in range(10):
	cur_line=json.loads(f.next())
	subreddits.append(cur_line['url'])
	subscribers.append(int(cur_line['subscribers']))
f.close()

trace = go.Bar(
    x = subreddits,
    y = subscribers
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
