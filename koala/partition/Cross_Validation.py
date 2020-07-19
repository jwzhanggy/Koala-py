'''
Concrete SettingModule class for a specific experimental SettingModule
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD

from koala.base.partition import partition
from sklearn.model_selection import KFold

class Cross_Validation(partition):
    '''
    Cross Validation for data partition
    Attribute: k: number of folds
    '''
    k = 3
    shuffle = True

    def __init__(self, name=None, description=None, k=None, shuffle=None):
        '''
        Initialization function
        :param pName: partition method name
        :param pDescription: partition method descriptions
        :param k: int, number of split
        :param shuffle: boolean, shuffle the data instances or not
        '''
        super().__init__(name, description)
        if k is not None:
            self.k = k
        if shuffle is not None:
            self.shuffle = shuffle


    def split(self, X):
        '''
        Concrete implementation of the split function
        :param X: input data instances
        :return: split data instances
        '''
        cv_kfold = KFold(n_splits=self.k, shuffle=self.shuffle)
        return cv_kfold.split(X)

        