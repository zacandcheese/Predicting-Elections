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
def doNothing(x):
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
		self.weights_hidden_out = np.random.rand(self.num_of_weights, 1)
		
	def train(self, input_set, target_vector, start_value = 0):#Changed input
		# input_vector and target_vector can be tuple, list or ndarray
		output_vector2 = np.zeros(shape = (1,1))
		output_vector2[0,0] = start_value
		
							#RUN THROUGH AND FIGURE OUT ERROR IF WE JUST INTIALLY RAN IT#
		#------------------------------------------------------------------------------------------------------#								
		for input_vector in input_set:
			input_vector = np.array(input_vector, ndmin=2)
			target_vector = np.array(target_vector, ndmin=2)
			
			
			#input 
			output_vector1 = np.dot(input_vector, self.weights_in_hidden)
			output_vector_hidden = output_vector1
			
			#output
			output_vector2 += np.dot(output_vector_hidden, self.weights_hidden_out)
		
		#ERROR
		output_errors = target_vector - output_vector2   
		self.method("Output Vector: " + str(output_vector2))#Toggle print
		time.sleep(1)
		error = output_errors[0,0]
		if abs(error) < 3: return True
		sign_of_error = 1 if error >= 0 else -1
		sign_of_target = 1 if target_vector[0] >= start_value else -1#FIXED changed to 50
		sign_of_output = 1 if output_vector2[0] >= 0 else -1
		
		if(sign_of_output == sign_of_target):
			sign_of_comp = 1 #compatibility
		else:
			sign_of_comp = -1
		
		#Error should be large because it had compounded over time.

		
														#PART 1#
		#------------------------------------------------------------------------------------------------------#
		coefficient_of_error = (1-(-1*sign_of_comp * ((sigmoid((error))-1/2)) * self.learning_rate))*sign_of_comp
		
		self.method("COE FIRST PASS: " + str(coefficient_of_error) + str(sigmoid((error))) + str(error))
		
		self.weights_hidden_out =  (coefficient_of_error) * self.weights_hidden_out
		
		#print(self.weights_hidden_out)
		
		
														#PART 2#
		#-------------------------------------------------------------------------------------------------------#
		hidden_errors = np.dot(output_errors, self.weights_hidden_out.T) #returns [value1, value2, value3, ... valueN]

		identity_matrix = np.zeros((self.num_of_weights,self.num_of_weights))
		i = 0
		
		for err in hidden_errors[0]:
			sign_of_error = 1 if err >= 0 else -1
			#coefficient_of_error = (1-sigmoid(err))*err*sign_of_error  #normalize it
			coefficient_of_error = 1-(-1*sign_of_comp * ((sigmoid((err))-1/2)) * self.learning_rate)
			
			self.method("HIDDEN ERROR "+str(i)+":"+ str(err)+str(coefficient_of_error))
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
	with open(name_of_file + " compiled.txt", 'r') as fin:
		b = json.load(fin)
		for canidate in b.keys():
			print(canidate)
			sumarr = [];
			
			for entry in b[canidate]:
				a = np.array(entry)
				sumarr.append(a)
				matrix = scoringMatrixOverTime(num_of_factors = 5, num_of_weights = 2, learning_rate = 0.3, method = doNothing)
			for i in range(300):
				matrix.train(sumarr,1,50)
				if(i%100 == 0):print(i)
			
			print(matrix.getMatrix())
			print("-----------",matrix.run(sumarr, 50))
	pass