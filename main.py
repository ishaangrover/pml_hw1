from neural_net import NeuralNetwork
nn = NeuralNetwork("parkinsons_supervised.csv", "initial_model", model_type='regression')
nn.train()