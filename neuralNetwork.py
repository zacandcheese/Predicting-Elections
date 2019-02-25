#https://www.python-course.eu/neural_networks_with_python_numpy.php
"""
import numpy as np
input_vector = np.array([2,4,11])
input_vector = np.array(input_vector, ndmin=2).T #Makes it horizontal
print(input_vector, input_vector.shape)
"""

"""

sigmoid function = 1 / (1 + e ^ -x)

"""
import numpy as np
from scipy.stats import truncnorm
#from scipy.special import expit as activation_function

def truncated_normal(mean, sd, low, upp):
	return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

@np.vectorize
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
activation_function = sigmoid

class NeuralNetwork:
	def __init__(self,
				num_of_in_nodes,
				num_of_out_nodes,
				num_of_hidden_nodes,
				learning_rate):
		self.num_of_in_nodes = num_of_in_nodes
		self.num_of_out_nodes = num_of_out_nodes
		self.num_of_hidden_nodes = num_of_hidden_nodes
		self.learning_rate = learning_rate
		self.create_weight_matrices()
		
	def create_weight_matrices(self):
		rad = 1 / np.sqrt(self.num_of_in_nodes)
		X = truncated_normal(mean = 0,sd = 1, low = -rad, upp = rad)
		self.weights_in_hidden = X.rvs((self.num_of_hidden_nodes, self.num_of_in_nodes))
		X = truncated_normal(mean = 0,sd = 1, low = -rad, upp = rad)
		self.weights_hidden_out = X.rvs((self.num_of_out_nodes, self.num_of_hidden_nodes))
		
	def train(self, input_vector, target_vector):
		# input_vector and target_vector can be tuple, list or ndarray
        
		input_vector = np.array(input_vector, ndmin=2).T
		target_vector = np.array(target_vector, ndmin=2).T
        
		output_vector1 = np.dot(self.weights_in_hidden, input_vector)
		output_vector_hidden = activation_function(output_vector1)
        
		output_vector2 = np.dot(self.weights_hidden_out, output_vector_hidden)
		output_vector_network = activation_function(output_vector2)
		
		output_errors = target_vector - output_vector_network
		# update the weights:
		tmp = output_errors * output_vector_network * (1.0 - output_vector_network)     
		tmp = self.learning_rate  * np.dot(tmp, output_vector_hidden.T)
		self.weights_hidden_out += tmp
		# calculate hidden errors:
		hidden_errors = np.dot(self.weights_hidden_out.T, output_errors)
		# update the weights:
		tmp = hidden_errors * output_vector_hidden * (1.0 - output_vector_hidden)
		self.weights_in_hidden += self.learning_rate * np.dot(tmp, input_vector.T)
		
	def run(self, input_vector):
		"""
		running the network with an input vector.
		input_vector can be tuple, list or ndarray
		"""
		#turning the input vector into a column vector
		input_vector = np.array(input_vector, ndmin = 2).T 
		output_vector = np.dot(self.weights_in_hidden, input_vector)
		output_vector = activation_function(output_vector)
		output_vector = np.dot(self.weights_hidden_out, output_vector)
		output_vector = activation_function(output_vector)
		
		return output_vector
		
if __name__ == "__main__":
	"""simple_network = NeuralNetwork(num_of_in_nodes = 2,
									num_of_out_nodes = 2,
									num_of_hidden_nodes = 10,
									learning_rate = 0.6)
	print(simple_network.run([3,4]))	
	print(simple_network.weights_in_hidden)
	print(simple_network.weights_hidden_out)
	"""
	#GRAPHING DATA
	import numpy as np
	from matplotlib import pyplot as plt
	data1 = [((3, 4), (0.99, 0.01)), ((4.2, 5.3), (0.99, 0.01)), 
			 ((4, 3), (0.99, 0.01)), ((6, 5), (0.99, 0.01)), 
			 ((4, 6), (0.99, 0.01)), ((3.7, 5.8), (0.99, 0.01)), 
			 ((3.2, 4.6), (0.99, 0.01)), ((5.2, 5.9), (0.99, 0.01)), 
			 ((5, 4), (0.99, 0.01)), ((7, 4), (0.99, 0.01)), 
			 ((3, 7), (0.99, 0.01)), ((4.3, 4.3), (0.99, 0.01))]
	data2 = [((-3, -4), (0.01, 0.99)), ((-2, -3.5), (0.01, 0.99)), 
			 ((-1, -6), (0.01, 0.99)), ((-3, -4.3), (0.01, 0.99)), 
			 ((-4, -5.6), (0.01, 0.99)), ((-3.2, -4.8), (0.01, 0.99)), 
			 ((-2.3, -4.3), (0.01, 0.99)), ((-2.7, -2.6), (0.01, 0.99)), 
			 ((-1.5, -3.6), (0.01, 0.99)), ((-3.6, -5.6), (0.01, 0.99)), 
			 ((-4.5, -4.6), (0.01, 0.99)), ((-3.7, -5.8), (0.01, 0.99))]
	data = data1 + data2
	np.random.shuffle(data)
	points1, labels1 = zip(*data1)
	X, Y = zip(*points1)
	plt.scatter(X, Y, c="r")
	points2, labels2 = zip(*data2)
	X, Y = zip(*points2)
	plt.scatter(X, Y, c="b")
	plt.show()
	
	#Create the network
	simple_network = NeuralNetwork(num_of_in_nodes=2, num_of_out_nodes=2, num_of_hidden_nodes=2, learning_rate=0.6)
    
	size_of_learn_sample = int(len(data)*0.9)
	learn_data = data[:size_of_learn_sample]
	test_data = data[-size_of_learn_sample:]
	print()
	for i in range(size_of_learn_sample):
		point, label = learn_data[i][0], learn_data[i][1]
		simple_network.train(point, label)
		
	for i in range(size_of_learn_sample):
		point, label = learn_data[i][0], learn_data[i][1]
		cls1, cls2 =simple_network.run(point)
		print(point, cls1, cls2, end=": ")
		if cls1 > cls2:
			if label == (0.99, 0.01):
				print("class1 correct", label)
			else:
				print("class2 incorrect", label)
		else:
			if label == (0.01, 0.99):
				print("class1 correct", label)
			else:
				print("class2 incorrect", label)