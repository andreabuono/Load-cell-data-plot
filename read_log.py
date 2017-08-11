import matplotlib.pyplot as plt

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


fig = plt.figure()
fig_1 = fig.add_subplot(111)
fig_1.grid(True, lw = 2, ls = '--', c = '.75')
fig_1.plot(volt_mes, avg_Fz,linewidth=2, c='blue')
fig_1.plot(volt_set, avg_Fz,linewidth=2, c='red')
fig_1.set_xlabel('Voltage (V)')
fig_1.set_ylabel('Thrust (N)')

print avg_Fz

plt.show()

