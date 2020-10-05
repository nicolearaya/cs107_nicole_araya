import numpy as np

def layer(shape, actv):
    #Check that shape is 2
	assert len(shape) == 2
    
    #Add closure
	def layer_closure(inputs, weights, bias):
		print(f'Layer shape {shape}')
		print(f'Shape of weights {weights.shape}')
		print(f'Shape of input {inputs.shape}')
		print(f'Shape of bias {bias.shape}')

		assert weights.shape == shape, f'{weights.shape} vs {shape}'
		assert bias.shape[0] == shape[1], f'{bias.shape} vs {shape[1]}'

		return actv(np.matmul(inputs,weights) + bias)   
        #actv(np.matmul(np.transpose(weights), np.transpose(inputs)) + bias)   
	return layer_closure
