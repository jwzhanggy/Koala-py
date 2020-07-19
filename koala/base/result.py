'''
Base class for all result
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD


import abc


class result:
    """
    result: Abstract Class
    Attributes: name: name of result
                description: textual descriptions of result
                folder_path: folder path for result
                file_name: filename of result

                content: content of result
    """
    
    name = None
    description = None
    
    folder_path = None
    file_name = None

    content = None


    # initialization function
    def __init__(self, name=None, description=None, folder_path = None, file_name = None):
        '''
            Parameters: result name: name, result description: description, folder path, and file names
            Assign the parameters to the attributes of the base result class
            For the result with multiple files, the filenames can be given with values as a list/dict
        '''
        self.name = name
        self.description = description
        self.folder_path = folder_path
        self.file_name = file_name


    # result information print function
    def print_information(self, print_result_content_tag=False):
        '''
            Print the basic information about the result class
            inclduing the result name, result description, result folder path, result filename, and result content (optional)
        '''
        print('Result Name: ', self.name)
        print('Result Description: ', self.description)
        print('Result File Path: ', self.folder_path)
        print('Result File Name: ', self.file_name)
        if print_result_content_tag:
            print('Result Content: ', self.content)


    # show base class
    def show_base_class(self):
        '''
            Show the base class information
        '''
        return 'result'


    # show name
    def show_name(self):
        '''
        Show the result name
        :return: result name
        '''
        return self.name

    # show discription
    def show_name(self):
        '''
        Show the result descriptions
        :return: result description
        '''
        return self.description

    # show folder path
    def show_folder_path(self):
        '''
        Show the result folder path
        :return: result folder path
        '''
        return self.folder_path

    # show file name
    def show_file_name(self):
        '''
        Show the result file name
        :return: result folder path
        '''
        return self.file_name

    # show file name
    def show_content(self):
        '''
        Show the result content
        :return: result content
        '''
        return self.content

    # update name
    def update_name(self, new_name):
        '''
        Update the result name
        '''
        self.name = new_name

    # update discription
    def update_name(self, new_description):
        '''
        Update the result descriptions
        '''
        self.description = new_description

    # update folder path
    def update_folder_path(self, new_folder_path):
        '''
        Update the result folder path
        '''
        self.folder_path = new_folder_path

    # update file name
    def update_file_name(self, new_file_name):
        '''
        Update the result file name
        '''
        self.file_name = new_file_name

    # update content
    def update_content(self, new_content):
        '''
        Update the result content
        '''
        self.content = new_content

    # result load abstract function
    @abc.abstractmethod
    def load(self):
        return


    # result save abstract function
    @abc.abstractmethod
    def save(self):
        return


