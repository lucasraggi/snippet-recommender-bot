from common import common, VocabType
import pandas as pd


class Algorithm:
    def __init__(self, alg_name, true_positive, false_negative):
        self.alg_name = alg_name
        self.true_positive = true_positive
        self.false_negative = false_negative
        self.total = true_positive + false_negative
        self.accuracy = 0

    def as_dict(self):
        return {'alg_name': self.alg_name,
                'true_positive': self.true_positive,
                'false_negative': self.false_negative,
                'total': self.total,
                'accuracy': self.accuracy}


def update_algorithm_dict(results, algorithm_dict):
    for original_name, top_words in results:
        prediction = common.filter_impossible_names(top_words)[0]
        original_subtokens = common.get_subtokens(original_name)
        predicted_subtokens = common.get_subtokens(prediction)
        original_main = original_subtokens[0]
        predicted_main = predicted_subtokens[0]
        # print('original_subtokens: ', original_subtokens)
        # print('predicted_subtokens: ', predicted_subtokens)
        # print('')
        if predicted_main not in algorithm_dict:
            algorithm_dict[predicted_main] = Algorithm(predicted_main, 0, 0)
        else:
            if predicted_main == original_main:
                algorithm_dict[predicted_main].true_positive += 1
            else:
                algorithm_dict[predicted_main].false_negative += 1

    return algorithm_dict


def export_algorithm_dict(algorithm_dict):
    algorithm_list = []
    for alg_name, alg in algorithm_dict.items():
        alg.total = alg.true_positive + alg.false_negative
        if alg.total > 0:
            alg.accuracy = alg.true_positive/alg.total
        else:
            alg.total = 0
        algorithm_list.append(alg)
    df = pd.DataFrame([x.as_dict() for x in algorithm_list])
    df.to_csv('test.csv', index=False)

