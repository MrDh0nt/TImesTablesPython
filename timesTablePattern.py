import turtle as do

def drawTimesTable(n,t):
	do.reset()
	do.speed(0)
	coords = []
	for i in range(0,n):
		do.forward((1000/n))
		do.left((360/n))
		coords.append(do.pos())
	i = 0
	test = n * t
	for i in range(0,test):
		coords.append(coords[i])
		
	for i in range(0,n):
		do.setpos(coords[i])
		do.setpos(coords[(i*t)])
		do.setpos(coords[i])

