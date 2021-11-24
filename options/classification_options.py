from options.options import Options


class ClassificationOptions(Options):
    def __init__(self):
        super().__init__()
        # dataset related
        self.batch_size_test = 128
        self.batch_size_train = 128

        # hyperparameters
        self.lr = 0.0001
        self.num_epochs = 10
        self.hidden_sizes = [784, 196, 49, 10]

#        self.hidden_sizes = [784, 526, 268, 10]
