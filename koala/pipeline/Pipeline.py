'''
Concrete SettingModule class for a specific experimental SettingModule
'''

# (c) IFM Lab Copyright 2017-Present. All Rights Reserved.
# Author: Jiawei Zhang <jiawei@ifmlab.org>
# License: TBD

from koala.base.pipeline import pipeline
import numpy as np

class Pipeline(pipeline):
    '''
    Implementation of the regular pipeline with data, partition, method, metric, result components
    '''

    def flush(self):
        '''
        Run the involved components sequentially, save the learned results, and return the evaluation scores
        :return: evaluation scores (mean +/- std)
        '''

        loaded_data = self.data.load()

        fold_count = 0
        score_list = []

        partition_result = self.partition.split(loaded_data['X'])
        for train_index, test_index in partition_result:
            fold_count += 1

            X_train, X_test = np.array(loaded_data['X'])[train_index], np.array(loaded_data['X'])[test_index]
            y_train, y_test = np.array(loaded_data['y'])[train_index], np.array(loaded_data['y'])[test_index]

            trained_model = self.method.train(X_train, y_train.ravel())
            y_pred = self.method.test(trained_model, X_test)

            evaluation_score = self.metric.evaluate(y_test, y_pred)
            score_list.append(evaluation_score)

            self.result.update_content({'raw_result': {'y_pred': y_pred, 'y_true': y_test}, 'evaluation_result': {self.metric.show_name(): evaluation_score}})
            file_name = self.result.show_file_name()
            self.result.update_file_name(file_name + '_' + str(fold_count))
            self.result.save()
            self.result.update_file_name(file_name)

        return np.mean(score_list), np.std(score_list)

