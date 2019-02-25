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
		
		output_vector1 = np.dot(input_vector, self.weights_in_hidden)
		output_vector_hidden = activation_function(output_vector1)
        
		output_vector2 = np.dot(output_vector_hidden, self.weights_hidden_out)
		output_vector_network = activation_function(output_vector2)
		
		output_errors = target_vector - output_vector_network
		
		# update the weights:
		tmp = output_errors * output_vector_network * (1.0 - output_vector_network)
		
		tmp = self.learning_rate * np.dot(tmp, output_vector_hidden)
		self.weights_hidden_out = self.weights_hidden_out + tmp[0,0]
		# calculate hidden errors:
		hidden_errors = np.dot(output_errors, self.weights_hidden_out.T)
		
		# update the weights:
		tmp = hidden_errors * output_vector_hidden * (1.0 - output_vector_hidden)
		self.weights_in_hidden += self.learning_rate * np.dot(input_vector.T, tmp)
		
	def run(self, input_vector):
		output_vector = np.dot(input_vector, self.weights_in_hidden)
		output_vector = activation_function(output_vector)
		output_vector = np.dot(output_vector, self.weights_hidden_out)
		return output_vector

		
if __name__ == '__main__':
	input = np.ones((1,3))
	activation_function(input)
	
	input = [1,3]
	print(input)
	
	matrix = scoringMatrix(num_of_factors = len(input),num_of_weights = 10, learning_rate = 0.6)
	#TRAIN THE MATRIX
	train_data = [(1,2,4),(1,2,4),(1,3,6),(1,3,6)]
	for i in range(1000):
		for set in train_data:
			matrix.train(set[0:-1],set[-1])
		
	print(matrix.run(input))