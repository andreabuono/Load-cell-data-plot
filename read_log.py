import os
import numpy.polynomial.polynomial as poly
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import plotly


os.chdir('Test 2')

avg_Fz = []
volt_set = []
volt_mes = []
current_mes = []

# Read the Zero thrust offset
infile = "0.0v.log"
Fz = []
f = open(infile,'r')
for line in f:
	a = line.split(', ')
	if a[0] != 't':
		Fz.append(float(a[3]))
Fz_off = (sum(Fz) / len(Fz))


files = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.7]

#open and read all log files
for k in range(len(files)):
	infile = str(files[k]) + "v.log"
	Fz = []
	f = open(infile,'r')
	for line in f:
		a = line.split(', ')
		if a[0] != 't':
			Fz.append(float(a[3]))

	avg_Fz.append  (((sum(Fz)/len(Fz))-Fz_off)/2)

infile = "voltage_current.log"
f = open(infile,'r')
for line in f:
	a = line.split(' ')
	if a[0] != 'Voltage_set':
		volt_set.append(float(a[0]))
		volt_mes.append(float(a[1]))
		current_mes.append(float(a[2]))

for i in range(len(volt_mes)):
	volt_mes[i] = volt_mes[i]* (65535.0/3.7)
	volt_set[i] = volt_set[i]* (65535.0/3.7)

coefs = poly.polyfit(volt_mes, avg_Fz, 2)
x_new = np.linspace(0,70000)
ffit = poly.polyval(x_new, coefs)

coefs2 = poly.polyfit(current_mes, avg_Fz, 1)
x_new2 = np.linspace(0,2.5)
ffit2 = poly.polyval(x_new2, coefs2)

trace1 = go.Scatter(x=volt_mes, y=avg_Fz, mode = 'markers' , name = 'raw data')
trace2 = go.Scatter(x=x_new, y=ffit, name = 'interpolated')

axis_template_x = dict(
	showgrid= True,
	zeroline = True,
	nticks =20,
	showline = True,
	title = 'PWM-Signal',
	mirror = 'all')

axis_template_y = dict(
	showgrid= True,
	zeroline = True,
	nticks =20,
	showline = True,
	title = 'Thrust (N)',
	mirror = 'all')

layout = go.Layout(
	title = 'Load cell Thrust moded',
	xaxis = axis_template_x,
	yaxis = axis_template_y,
	)

data = [trace1, trace2]

fig = go.Figure(data = data,
	layout = layout)

plotly.offline.plot(fig)

