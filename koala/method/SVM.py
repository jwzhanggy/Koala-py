'''
Concrete MethodModule class for a specific learning MethodModule
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD

from koala.base.method import method
from sklearn import svm


class SVM(method):
    '''
        SVM class for the support vector machine model
    '''
    c = 1.0


    def __init__(self, name=None, description=None, c=None):
        super().__init__(name, description)
        self.c = c


    def train(self, X, y):
        '''
        Training function of the SVM model
        :param X: features of training instances
        :param y: labels of training instances
        :return: learned model
        '''

        model = svm.SVC(C = self.c)
        model.fit(X, y)
        return model


    def validate(self, model, X):
        '''
        Validation function of the SVM model
        :param model: a trained model
        :param X: features of the validation instnaces
        :param y: labels of the validation instnaces
        :return: prediction y
        '''
        pred_y = model.predict(X)
        return pred_y

    
    def test(self, model, X):
        '''
        Testing function of the SVM model
        :param model: a trained model
        :param X: features of the testing instnaces
        :param y: labels of the testing instnaces
        :return: prediction y
        '''
        pred_y = model.predict(X)
        return pred_y
