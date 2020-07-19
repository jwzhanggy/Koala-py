'''
Base method class for all methods
'''

# Copyright (c) 2017-Present
# Jiawei Zhang, IFM Lab
# <jiawei@ifmlab.org>
# License: TBD


import abc


class method:
    '''
    method: Abstract Class
    Entries: name: name of method
             description: textual description of method

             start_time: start running time of method
             stop_time: stop running time of method
             running_time: total running time of method
             training_time: total time cost of method training
             testing_time: total time cost of method testing

             input: input data for method
             output: output learning result of method
    '''

    name = None
    description = None

    start_time = None
    stop_time = None

    running_time = None
    training_time = None
    validation_time = None
    testing_time = None

    input = None
    output = None


    # initialization function
    def __init__(self, name=None, description=None):
        '''
            Parameters: method name: mName, method description: mDescription
            Assign the parameters to the attributes of the base method class
        '''
        self.name = name
        self.description = description


    # method information print function
    def print_information(self, print_input_tag=False, print_output_tag=False):
        '''
            Print the basic information about method class
            inclduing the method name, method description, input data (optional) and output learning result (optional)
        '''
        print('Method Name: ', self.name)
        print('Method Description: ', self.description)
        if print_input_tag:
            self.input.print_information()
        if print_output_tag:
            self.output.print_information()


    # show base class
    def show_base_class(self):
        '''
            Show the base class information
        '''
        return 'method'


    # show name
    def show_name(self):
        '''
        Show the method name
        :return: method name
        '''
        return self.name

    # show discription
    def show_name(self):
        '''
        Show the method descriptions
        :return: method description
        '''
        return self.description

    # update name
    def update_name(self, new_name):
        '''
        Update the method name
        '''
        self.name = new_name

    # update discription
    def update_name(self, new_description):
        '''
        Update the method descriptions
        '''
        self.description = new_description


    # method train abstract function
    @abc.abstractmethod
    def train(self):
        return


    # method validate abstract function
    @abc.abstractmethod
    def validate(self):
        return


    # method test abstract function
    @abc.abstractmethod
    def test(self):
        return






