'''
Concrete ResultModule class for a specific experiment ResultModule output
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD

from koala.base.result import result
import pickle


class Result(result):

    # concrete implementation of the save function
    def save(self):
        f = open(self.folder_path + self.file_name, 'wb')
        pickle.dump(self.content, f)
        f.close()