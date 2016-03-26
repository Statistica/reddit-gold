# Written by Jonathan Saewitz, released March 26th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import json, plotly.plotly as plotly, plotly.graph_objs as go

########################
#        Config        #
########################
graph_title="Reddit Gold Given By Day Of Week"

x_axis_title="Day Of Week"
y_axis_title="# of Reddit Gold given"

filename="guilds_by_day_of_week.json"
########################
#      End Config      #
########################


weekdays=[]
guilds=[]
for line in open(filename, 'r'):
	cur_line=json.loads(line)
	weekdays.append(int(cur_line['day_of_week']))
	guilds.append(cur_line['gilded_count'])

for i in range(len(weekdays)):
	if weekdays[i]==1:
		weekdays[i]="Sunday"
	if weekdays[i]==2:
		weekdays[i]="Monday"
	if weekdays[i]==3:
		weekdays[i]="Tuesday"
	if weekdays[i]==4:
		weekdays[i]="Wednesday"
	if weekdays[i]==5:
		weekdays[i]="Thursday"
	if weekdays[i]==6:
		weekdays[i]="Friday"
	if weekdays[i]==7:
		weekdays[i]="Saturday"

trace = go.Bar(
    x = weekdays,
    y = guilds
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
