from common import common, VocabType


class algorithm:
    def __init__(self, alg_name, true_positive, false_negative):
        self.alg_name = alg_name
        self.true_positive = true_positive
        self.false_negative = false_negative


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
            algorithm_dict[predicted_main] = algorithm(predicted_main, 0, 0)
        else:
            if predicted_main == original_main:
                algorithm_dict[predicted_main].true_positive += 1
            else:
                algorithm_dict[predicted_main].false_negative += 1

    return algorithm_dict
