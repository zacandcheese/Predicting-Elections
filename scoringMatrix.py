import numpy as np
import time
"""

input		hidden		output
vector		network		vector
f1	
f2			  w1
f3			  w2		  sum
f4			  w3
f5			  wn
fn	


[1,								[5x5]
 2,			[1] - w1	[5x5]
 3,			[1] - w2	[5x5]
 4,	   .    [1] - w3 = 	[5x5]	
 5,			[1] - wn	[5x5]
 n]

^^^^ WRONG ^^^


|factors|		|hidden in|												|hidden out|		
					[1,
					 2,
[1,2,3,4,5] (dot)  	 3,	= [55]
					 4,
					 5]						[55,							[1
									-----> 	 55,	----> [55,55,55] (dot)	 1	= score
											 55]							 1]
					 [1,					
					  2,
			(dot)	  3, = [55]	
					  4,
					  5,]
					  
		
		
basically
1x5 mulitplied by a 5xN = 1xN where N is the number of weights 
and that can be converted to a sum in the final step
					
"""
def doNothing(x = None, y = None):
	pass
	
def sigmoid(x):
	return 1 / (1 + np.exp(-x))

activation_function = sigmoid

class scoringMatrix:
	def __init__(self, num_of_factors, num_of_weights, learning_rate):
		self.num_of_factors = num_of_factors
		self.num_of_weights = num_of_weights
		self.learning_rate = learning_rate
		self.create_weight_matrice()
		
		
	def create_weight_matrice(self):
		self.weights_in_hidden = np.random.rand(self.num_of_factors, self.num_of_weights)
		self.weights_hidden_out = np.random.rand(self.num_of_weights, 1)
		
	def train(self, input_vector, target_vector):#Changed input
		# input_vector and target_vector can be tuple, list or ndarray
		input_vector = np.array(input_vector, ndmin=2)
		target_vector = np.array(target_vector, ndmin=2)
		
		#input 
		output_vector1 = np.dot(input_vector, self.weights_in_hidden)
		output_vector_hidden = output_vector1
		
		#output
		output_vector2 = np.dot(output_vector_hidden, self.weights_hidden_out)
			
		output_errors = target_vector - output_vector2

		"""
		I have the error
		i get the relative error
		I multiply the last or hidden out by a certain function
		sigma()
		
		I multiply the second or hidden in by a certain function
		sigma()*(1 - sigma())
		
		so if i get close to zero my error reaches zero and 
		relative is zero
		
		if i am above
		error is positive
		and sigmoid > 0.5
		and i want to lower the weights
		
		error is negative
		sigmoid is < 0.5
		and i want to increase the weights
		"""
		error = output_errors[0,0]
		relative_error = error/target_vector[0,0]
		#print(output_vector2)
		#print("Output Error", output_errors)

		#----------------------------PART 1------------------------------#
		coefficient_of_error = -1 * error * (sigmoid(error)) * self.learning_rate
		"""
		if( coefficient_of_error > 0):
			print("+++++++++++++")
		else:
			print("-------------")
		"""
		self.weights_hidden_out =  (1 - coefficient_of_error) * self.weights_hidden_out
		
		
		#----------------------------PART 2------------------------------#
		hidden_errors = np.dot(output_errors, self.weights_hidden_out.T) #returns [value1, value2, value3, ... valueN]

		identity_matrix = np.zeros((self.num_of_weights,self.num_of_weights))
		i = 0
		for err in hidden_errors[0]:
			coefficient_of_error = -1* err * (sigmoid(err)) * self.learning_rate * (1-sigmoid(err)) #normalize it
			identity_matrix[i][i] = coefficient_of_error
			i+=1
		
		tmp = (np.dot(self.weights_in_hidden , identity_matrix)) #matrix that has been modified
		self.weights_in_hidden += tmp
		
	def run(self, input_vector):
		output_vector = np.dot(input_vector, self.weights_in_hidden)
		output_vector = np.dot(output_vector, self.weights_hidden_out)
		return output_vector

class scoringMatrixOverTime:
	def __init__(self, in_matrix, out_matrix):
		self.weights_in_hidden = in_matrix
		self.weight_hidden_out = out_matrix
		
	def __init__(self, num_of_factors = None, num_of_weights = None, learning_rate = None, method = None, in_matrix = None, out_matrix = None):
		if learning_rate is not None:
			self.num_of_factors = num_of_factors
			self.num_of_weights = num_of_weights
			self.learning_rate = learning_rate
			self.method = method
			
			self.create_weight_matrice()
		else:
			self.weights_in_hidden = in_matrix
			self.weights_hidden_out = out_matrix
			
	def create_weight_matrice(self):
		self.weights_in_hidden = np.random.rand(self.num_of_factors, self.num_of_weights)
		#for i in range(len(self.weights_in_hidden)):
		#	if (i%2 == 0):
		#		self.weights_in_hidden[i] *= -1
		self.weights_hidden_out = np.random.rand(self.num_of_weights, 1)
	
	def train(self, input_set, target_vector, start_value = 0):#Changed input
		# input_vector and target_vector can be tuple, list or ndarray
		output_vector2 = np.zeros(shape = (1,1))
		output_vector2[0,0] = start_value
		
		temp_sum = 0#TEMP
							#RUN THROUGH AND FIGURE OUT ERROR IF WE JUST INTIALLY RAN IT#
		#------------------------------------------------------------------------------------------------------#								
		for input_vector in input_set:
			input_vector = np.array(input_vector, ndmin=2)
			target_vector = np.array(target_vector, ndmin=2)

			temp_sum += input_vector[0,self.num_of_factors-1]#----------------------TEMP------------------
			#input 
			output_vector1 = np.dot(input_vector, self.weights_in_hidden)
			output_vector_hidden = output_vector1
			
			#output
			output_vector2 += np.dot(output_vector_hidden, self.weights_hidden_out)
		
		#ERROR
		
		self.method("SUM", temp_sum)#TEMP
		output_errors = target_vector - output_vector2   
		self.method("Output Vector: " + str(output_vector2))#Toggle print
		#time.sleep(1)
		error = output_errors[0,0]

		
		
														#PART 1#
		#------------------------------------------------------------------------------------------------------#
		coefficient_of_error = 1+((sigmoid((error))-1/2) * self.learning_rate) #First Derivative
		
		self.method("COE FIRST PASS: " + str(coefficient_of_error) + " " + str(sigmoid((error)))+ " " + str(error))
		
		self.weights_hidden_out = (coefficient_of_error) * self.weights_hidden_out
		
		
		
		
														#PART 2#
		#-------------------------------------------------------------------------------------------------------#
		hidden_errors = np.dot(output_errors, self.weights_hidden_out.T) #returns [value1, value2, value3, ... valueN] in a list form
		identity_matrix = np.zeros((self.num_of_weights,self.num_of_weights))
		
		i = 0
		for err in hidden_errors[0]:

			coefficient_of_error = 1+(	((sigmoid(err) * (1-(sigmoid(err))))	- 1/4) * self.learning_rate) #Second Derivative
			
			self.method("HIDDEN ERROR "+ str(i) +":"+ str(err)+str(coefficient_of_error))
			identity_matrix[i][i] = coefficient_of_error
			i+=1
		
		tmp = (np.dot(self.weights_in_hidden , identity_matrix)) #matrix that has been modified
		self.weights_in_hidden = tmp
		return False
		
		
	def run(self, input_set, start_value = 0):#set
		"""output_vector = np.dot(input_vector, self.weights_in_hidden)
		output_vector = np.dot(output_vector, self.weights_hidden_out)
		return output_vector"""#OG
		ylist = []
		xlist = []
		
		output_vector2 = np.zeros(shape = (1,1))
		output_vector2[0,0] = start_value
		for input_vector in input_set:
			input_vector = np.array(input_vector, ndmin=2)
			
			#input 
			output_vector1 = np.dot(input_vector, self.weights_in_hidden)
			output_vector_hidden = output_vector1
			
			#output
			output_vector2 += np.dot(output_vector_hidden, self.weights_hidden_out)
			#list.append(np.dot(output_vector_hidden, self.weights_hidden_out)[0][0])
			ylist.append(output_vector2[0][0])
			xlist.append(input_vector[0][0])
		return output_vector2, xlist, ylist

	def getMatrix(self):
		return self.weights_in_hidden, self.weights_hidden_out



		
if __name__ == '__main__':
	
	import scoring
	import json
	name_of_file = "Comstock Wexton tweets.txt"
	final_result_file = "Comstock Wexton poll.txt"
	final_result = 0
	
	with open(final_result_file, 'r') as file:
		dict = json.load(file)
		final_result = dict['11/6']
	#name_of_file = "Kaine Stewart tweets.txt"
	#name_of_file = "Brat Spanberger tweets.txt"

	#dict = ConvertTweets(name_of_file)
	
	matrix = scoringMatrixOverTime(num_of_factors = 5, num_of_weights = 3, learning_rate = 0.3, method = doNothing)#Changed
	
	with open(name_of_file + " compiled.txt", 'r') as fin:
		b = json.load(fin)
		big_list = []
		for candidate in b.keys():
			print(candidate)
			sumarr = [];
			
			for entry in b[candidate]:
				a = np.array(entry)
				sumarr.append(a)
			
			big_list.append(sumarr)
	
	for i in range(3001):
		result_list = [45,55]
		matrix.train(big_list[i%2],result_list[i%2],0)
		if(i%100 == 0):print(i)
	
	print(matrix.getMatrix())
	print("-----------",matrix.run(big_list[0], 0))
	print("-----------",matrix.run(big_list[1], 0))
	pass