'''
Concrete Evaluate class for a specific evaluation metrics
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD

from koala.base.metric import metric
from sklearn.metrics import accuracy_score


class Accuracy(metric):
    '''
    Accuracy evaluation metric
    '''

    # initialization function
    def __init__(self, name=None, description=None):
        super().__init__(name, description)


    # concrete implementation of the evaluate function
    def evaluate(self, y_pred, y_true):
        '''
        The evaluate function for calculating the accuracy score
        :param y_pred: prediction label vector
        :param y_true: true label vector
        :return: accuracy score
        '''
        return accuracy_score(y_true, y_pred)
        