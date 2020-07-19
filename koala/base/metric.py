'''
Base class for all evaluation metrics
'''

# Copyright (c) 2017-Present
# Jiawei Zhang, IFM Lab
# <jiawei@ifmlab.org>
# License: TBD


import abc


class metric:
    """ 
    metric: Abstract Class
    Attributes: name: name of evaluation metric
                description: textual description of evaluation metric
    """
    
    name = None
    description = None


    # initialization function
    def __init__(self, name=None, description=None):
        '''
            Parameters: metric name: name, metric description: description
            Assign the parameters to the attributes of the base metric class
        '''
        self.name = name
        self.description = description


    # metric information print function
    def print_information(self):
        '''
            Print the basic information about the metric class
            inclduing the metric name, metric description
        '''
        print('Metric Name: ', self.name)
        print('Metric Description: ', self.description)


    # show base class
    def show_base_class(self):
        '''
            Show the base class information
        '''
        return 'metric'

    # show name
    def show_name(self):
        '''
        Show the metric name
        :return: metric name
        '''
        return self.name

    # show discription
    def show_name(self):
        '''
        Show the metric descriptions
        :return: metric description
        '''
        return self.description

    # update name
    def update_name(self, new_name):
        '''
        Update the metric name
        '''
        self.name = new_name

    # update discription
    def update_name(self, new_description):
        '''
        Update the metric descriptions
        '''
        self.description = new_description


    # metric evaluate abstract function
    @abc.abstractmethod
    def evaluate(self):
        return
