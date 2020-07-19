'''
Base class for all pipelines
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD


import abc


class pipeline:
    """
    pipeline: Abstract Class
    Attributes: name: name of pipeline
                description: textual descriptions of pipeline

                pipeline components: data, partition, method, metric, result
    """

    name = None
    description = None

    data = None
    partition = None
    method = None
    metric = None
    result = None


    # initialization function
    def __init__(self, name=None, description=None, data=None, partition=None, method=None, metric=None, result=None):
        '''
            Parameters: pipeline name: name, pipeline description: description, pipeline components: data, partition, method, metric, result
            Assign the parameters to the attributes of the base pipeline class
        '''
        self.name = name
        self.description = description

        self.data = data
        self.partition = partition
        self.method = method
        self.metric = metric
        self.result = result


    # pipeline information print function
    def print_information(self, print_component_tag=True):
        '''
            Print the basic information about the pipeline class
            inclduing the pipeline name, pipeline description, and pipeline components
        '''
        print('++++++++++++++++++++++++++++++++++++')
        print('Pipeline Name: ', self.name)
        print('Pipeline Description: ', self.description)
        if print_component_tag:
            print('------------------------------------')
            self.data.print_information()
            print('------------------------------------')
            self.partition.print_information()
            print('------------------------------------')
            self.method.print_information()
            print('------------------------------------')
            self.metric.print_information()
            print('------------------------------------')
            self.result.print_information()
        print('++++++++++++++++++++++++++++++++++++')


    # pipeline assemble function
    def assemble(self, data=None, partition=None, method=None, metric=None, result=None):
        '''
            Assemble the pipeline with the provided components
        '''
        self.data = data
        self.partition = partition
        self.method = method
        self.metric = metric
        self.result = result


    # show base class information
    def show_base_class(self):
        '''
            Show the base class information
        '''
        return 'pipeline'


    # show name
    def show_name(self):
        '''
        Show the pipeline name
        :return: pipeline name
        '''
        return self.name

    # show discription
    def show_name(self):
        '''
        Show the pipeline descriptions
        :return: pipeline description
        '''
        return self.description

    # update name
    def update_name(self, new_name):
        '''
        Update the pipeline name
        '''
        self.name = new_name

    # update discription
    def update_name(self, new_description):
        '''
        Update the pipeline descriptions
        '''
        self.description = new_description


    # pipeline flush abstract function
    @abc.abstractmethod
    def flush(self):
        return
