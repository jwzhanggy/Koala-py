from koala.data.Data import Data
from koala.partition.Cross_Validation import Cross_Validation
from koala.method.SVM import SVM
from koala.metric.Accuracy import Accuracy
from koala.result.Result import Result
from koala.pipeline.Pipeline import Pipeline

# ---- SVM baseline method ----
if 1:
    # ---- parameter section -------------------------------
    c = 1.0
    k = 3
    # ------------------------------------------------------

    # ---- objection initialization setction ---------------
    data_obj = Data(name='local', folder_path='./data_samples/', file_name='test_data_file.txt')

    partition_obj = Cross_Validation(name='CV', k=k)

    method_obj = SVM(name='SVM', c=c)

    result_obj = Result(name='local', folder_path='./result_samples/SVM_', file_name='prediction_result_' + str(c))

    metric_obj = Accuracy(name='Accuracy')

    pipeline_obj = Pipeline(name='regular')
    # ------------------------------------------------------

    # ---- running section ---------------------------------
    pipeline_obj.assemble(data=data_obj, partition=partition_obj, method=method_obj, metric=metric_obj, result=result_obj)
    mean_score, std_score = pipeline_obj.flush()
    pipeline_obj.print_information()
    print('SVM Accuracy: ' + str(mean_score) + ' +/- ' + str(std_score))
    # ------------------------------------------------------