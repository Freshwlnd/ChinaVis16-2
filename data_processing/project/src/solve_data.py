data = []

with open('te.txt', 'r') as input_file:
	alls = input_file.readlines()
	for a in alls:
		a = a.split(':')[0]+',\n'
		print(a)
		data.append(a)

data.append("['00:00-00:59'")
for i in range(1,24):
	if i<10:
		i = '0'+str(i)
	else:
		i = str(i)
	data.append(",'"+i+":00-"+i+":59'")
data.append(']')

with open('te.txt', 'w') as output_file:
	output_file.writelines(data)