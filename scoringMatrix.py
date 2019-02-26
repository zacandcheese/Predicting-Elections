import numpy as np
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
		
	def train(self, input_vector, target_vector):
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
		
		#print("Output Error", output_errors)
		"""
		# update the weights:
		tmp = output_errors #* output_vector2 * (1.0 - output_vector2)
		#print("tmp first pass", tmp)
		tmp = sigmoid(tmp)
		#print("tmp second pass", tmp)
		tmp = self.learning_rate * np.dot(tmp, output_vector_hidden)
		#print("tmp third pass", tmp)
		#print("weights", self.weights_hidden_out)
		
		#NEED TO MAKE A MATRIX
		self.weights_hidden_out = tmp.T + self.weights_hidden_out
		"""
		#----------------------------PART 1------------------------------#
		coefficient_of_error = -1 * error * (sigmoid(error) - 0.5)
		self.weights_hidden_out =  (1 - coefficient_of_error) * self.weights_hidden_out
		
		
		#----------------------------PART 2------------------------------#
		"""
		# calculate hidden errors:
		
		print("hidden errors", hidden_errors)
		# update the weights:
		print(sigmoid(error))
		tmp = hidden_errors * (sigmoid(error)) * (1 - sigmoid(error))
		x = self.learning_rate * np.dot(input_vector.T, tmp)
		print(x)
		self.weights_in_hidden += x
		"""
		hidden_errors = np.dot(output_errors, self.weights_hidden_out.T) #returns [value1, value2, value3, ... valueN]
		print(hidden_errors[0][0])
		identity_matrix = np.zero(self.num_of_weights,self.num_of_weights)
		
		
		coefficient_of_error = -1 * error * (sigmoid(error) - 0.5) * (1-(sigmoid(error)-0.5)) #normalize it
		self.weights_in_hidden #matrix that has been modified
		
	def run(self, input_vector):
		output_vector = np.dot(input_vector, self.weights_in_hidden)
		output_vector = np.dot(output_vector, self.weights_hidden_out)
		return output_vector

		
if __name__ == '__main__':
	
	input = [1,2]
	print(input)
	
	matrix = scoringMatrix(num_of_factors = len(input),num_of_weights = 2, learning_rate = 0.6)
	#TRAIN THE MATRIX
	train_data = [(1,2,4),(1,2,4),(1,3,6),(1,3,6)]
	for i in range(2):
		for set in train_data:
			matrix.train(set[0:-1],set[-1])
		
	print(matrix.run(input))