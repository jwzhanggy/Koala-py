'''
Base class for all data
'''

# Copyright (c) 2017-Present
# Jiawei Zhang, IFM Lab
# <jiawei@ifmlab.org>
# License: TBD


import abc


class data:
    """ 
    data: Abstract Class 
    Attributes: name: name of data
                description: textual description of data
                folder_path: folder path of data
                file_name: file name of data
                content: content of data
    """
    
    name = None
    description = None
    
    folder_path = None
    file_name = None
    
    content = None


    # initialization function
    def __init__(self, name=None, description=None, folder_path = None, file_name = None):
        '''
            Parameters: data name: name, data description: description, data folder path: folder_path, data file name: file_name
            Assign the parameters to the attributes of the base data class
            For the data with multiple files, the file names can be provided as a list/dict
        '''
        self.name = name
        self.description = description
        self.folder_path = folder_path
        self.file_name = file_name


    # data information print function
    def print_information(self, print_data_content_tag=False):
        '''
            Print the basic information about the data class
            inclduing the data name, data description, data folder path, data file name, and data content (optional)
        '''
        print('Data Name: ', self.name)
        print('Data Description: ', self.description)
        print('Data Folder Path: ', self.folder_path)
        print('Data File Name: ', self.file_name)
        if print_data_content_tag:
            print('Data Content: ', self.content)


    # show base class
    def show_base_class(self):
        '''
            Show the base class information
        '''
        return 'data'

    # show name
    def show_name(self):
        '''
        Show the data name
        :return: data name
        '''
        return self.name

    # show discription
    def show_name(self):
        '''
        Show the data descriptions
        :return: data description
        '''
        return self.description

    # show folder path
    def show_folder_path(self):
        '''
        Show the data folder path
        :return: data folder path
        '''
        return self.folder_path

    # show file name
    def show_file_name(self):
        '''
        Show the data file name
        :return: data folder path
        '''
        return self.file_name

    # show file name
    def show_content(self):
        '''
        Show the data content
        :return: data content
        '''
        return self.content

    # update name
    def update_name(self, new_name):
        '''
        Update the data name
        '''
        self.name = new_name

    # update discription
    def update_name(self, new_description):
        '''
        Update the data descriptions
        '''
        self.description = new_description

    # update folder path
    def update_folder_path(self, new_folder_path):
        '''
        Update the data folder path
        '''
        self.folder_path = new_folder_path

    # update file name
    def update_file_name(self, new_file_name):
        '''
        Update the data file name
        '''
        self.file_name = new_file_name

    # update content
    def update_content(self, new_content):
        '''
        Update the data content
        '''
        self.content = new_content

    # data load abstract function
    @abc.abstractmethod
    def load(self):
        return


    # data save abstract function
    @abc.abstractmethod
    def save(self):
        return

    