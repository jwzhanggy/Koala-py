'''
Base class for all partition approaches
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD


import abc


class partition:
    '''
    partition: Abstract Class
    Attributes: name: name of partition approach
                description: textual description of partition approach
    '''
    
    name = None
    description = None


    def __init__(self, name=None, description=None):
        '''
            Parameters: partition name: name, partition description: description
            Assign the parameters to the attributes of the base partition class
        '''
        self.name = name
        self.description = description


    # partition information print function
    def print_information(self):
        '''
            Print the basic information about partition class
            inclduing the partition name, partition description
        '''
        print('partition Name: ', self.name)
        print('partition Description: ', self.description)


    # show base class
    def show_base_class(self):
        '''
            Show the base class information
        '''
        return 'partition'


    # show name
    def show_name(self):
        '''
        Show the partition name
        :return: partition name
        '''
        return self.name

    # show discription
    def show_name(self):
        '''
        Show the partition descriptions
        :return: partition description
        '''
        return self.description

    # update name
    def update_name(self, new_name):
        '''
        Update the partition name
        '''
        self.name = new_name

    # update discription
    def update_name(self, new_description):
        '''
        Update the partition descriptions
        '''
        self.description = new_description


    # partition split abstract function
    @abc.abstractmethod
    def split(self):
        return
