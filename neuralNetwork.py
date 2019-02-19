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

def truncated_normal(mean, sd, low, upp):
	return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

def sigma(x):
    return 1 / (1 + np.exp(-x))

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
		
	def train(self):
		pass
		
	def run(self):
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
	simple_network = NeuralNetwork(num_of_in_nodes = 3,
									num_of_out_nodes = 2,
									num_of_hidden_nodes = 4,
									learning_rate = 0.1)
	print(simple_network.weights_in_hidden)
	print(simple_network.weights_hidden_out)