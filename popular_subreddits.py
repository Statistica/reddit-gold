import json, plotly.plotly as plotly, plotly.graph_objs as go

########################
#        Config        #
########################
graph_title="Reddit Gold Given By Subreddit"

x_axis_title="Subreddit"
y_axis_title="# of Reddit Gold given"
########################
#      End Config      #
########################


subreddits=[]
gilds=[]
f=open('popularly_gilded_subreddits.json', 'r')
for i in range(10):
	cur_line=json.loads(f.next())
	subreddits.append(cur_line['subreddit'])
	gilds.append(int(cur_line['gilded_count']))
f.close()

trace = go.Bar(
    x = subreddits,
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
