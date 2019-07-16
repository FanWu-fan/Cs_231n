class Neuron(object):
    #...
    def forward(inputs):
        """" 假设输入和权重是1-D的numpy数组，偏差是一个数字"""
        cell_body_sum = np.sum(inputs* self.weights) + self.bias
        firing_rate = 1.0/(1.0 + math.exp(-cell_body_sum))  #sigmoid激活函数
        return firing_rate