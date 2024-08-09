""" SVMModel: Component that trains and makes predictions. """
from sklearn.svm import SVR
from . model import Model
class SVMModel(Model):
    """ SVMModel: Component that trains and makes predictions. """
    def __init__(self, kernel):
        super().__init__()
        self.model = SVR(
            kernel = kernel
        )
    def train(self, features = None, truth = None):
        """ Train the model. """
        self.model.fit(features, truth)
    def predict(self, features = None):
        """ Make predictions. """
        return self.model.predict(features)
    def score(self, x_test = None, y_test = None):
        """ Score the model. """
        return self.model.score(x_test, y_test)
    