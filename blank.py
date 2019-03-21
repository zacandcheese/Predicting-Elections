def doNothing(input):
	pass
def anything (method):
	print("before")
	method("hello")

anything(doNothing)

import scoring
import scoringMatrix
import json, numpy 

arr1, arr2 = scoring.loadMatrix("Comstock Wexton Matrix.txt")
matrix = scoringMatrix.scoringMatrixOverTime(in_matrix = arr1, out_matrix = arr2)

name_of_file = "Comstock Wexton tweets.txt"
with open(name_of_file + " compiled.txt", 'r') as fin:
	b = json.load(fin)
	listArr = []
	
	for canidate in b.keys():
		print(canidate)
		sumarr = [];
		
		for entry in b[canidate]:
			a = numpy.array(entry)
			sumarr.append(a)
		listArr.append(sumarr)
		
		
#print("-----------",matrix.run(listArr[0]))
#print("-----------", matrix.run(listArr[1]))

import graphing
import operator
matrix1, x1, y1 = matrix.run(listArr[0])
matrix2, x2, y2 = matrix.run(listArr[1])
#graphing.GraphCompiled(x1, y1, x2, y2 )
#NEED TO CONVERT TO USE X1-X2 AND HAVE DATES

"""
for i in range(x2[0],x2[-1]):
	print(x2[j], j, i)
	if(x2[j] == i):
		dict1[i] = y1[j]
		j+=1
		print("i'm here", j)
	else:
		dict1[i] = 0
"""
	

def Order(x1, y1):
	j=0;
	i = 0
	dict1 = {}
	last = 0;
	for x in x1:
		dict1[x] = y1[j]-last
		last = y1[j]
		j+=1
	for x in range(x1[0],283):#FIXME
		try:
			dict1[x]
		except KeyError:
			dict1[x] = 0;
	x1s = sorted(dict1.items() ,  key=lambda x: (x[0]) )
	final_x = []
	final_y = []
	for tuple in x1s:
		final_x.append(tuple[0])
		final_y.append(tuple[1])
	return final_x, final_y

x1, y1 = Order(x1, y1)
x2, y2 = Order(x2, y2)

y = [(a_i - b_i) for a_i, b_i in zip(y1, y2)] #CORRECT GRAPH OF DIFFERENCE PER DAY

graphing.Graph(x1, y, "Dates", "Comstock v. Wexton")
y_1 = []
y_2 = []
last = 0
for i in range(len(y1)):
	y_1.append(y1[i]+last)
	last += y1[i]
last = 0
for i in range(len(y2)):
	y_2.append(y2[i]+last)
	last += y2[i]

print(y_1)
graphing.GraphCompiled(x1, y1, x2, y2 ) #CORRECT GRAPH OF DIFFERENCE OVER TIME


						#CORRECT GRAPH FOR PERCENTAGE OF PEOPLE
#---------------------------------------------------------------------------------#
y = []
y_1 = []
y_2 = []
difference = 0
for i in range(len(y1)):
	difference += y1[i] - y2[i]
	
	y_1.append(50+(difference/2)) #CANDIDATE 1
	y_2.append(50-(difference/2)) #CANDIDATE 2

graphing.GraphCompiled(x1, y_1, x2, y_2 ) #CORRECT GRAPH OF DIFFERENCE OVER TIME
	
