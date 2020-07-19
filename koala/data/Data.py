'''
Concrete IO class for feature-label vector dataset
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD

from koala.base.data import data


class Data(data):
    '''
        Data class for regular feature-vector vector datasets
    '''

    # concrete implementation of load function
    def load(self, num_label=1):
        '''
        Load feature-label vector datasets from file
        :param num_label: number of label in the data vectors
        :return: loaded data in a dict
        '''

        X = []
        y = []
        f = open(self.folder_path + self.file_name)
        for line in f:
            line = line.strip('\n')
            elements = [float(i) for i in line.split(' ')]
            X.append(elements[:-num_label])
            y.append(elements[-num_label:])
        return {'X': X, 'y': y}