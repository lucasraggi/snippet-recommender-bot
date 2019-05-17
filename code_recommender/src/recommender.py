from code_recommender.src.sqlconnector import MySqlOperator
import json

class UserMethod:
    def __init__(self, method_name, number_parameters, parameter_types, return_type):
        self.method_name = method_name
        self.number_parameters = number_parameters
        self.parameter_types = parameter_types
        self.return_type = return_type

class RecommendationMethod:
    def __init__(self, code, number_parameters, parameter_types, return_type):
        self.code = code
        self.number_parameters = number_parameters
        self.parameter_types = parameter_types
        self.return_type = return_type
        self.points = 0

def rank_methods(user_method, recommendation_method_list):
    for method in recommendation_method_list:
        # Return types points
        return_type_points = 0
        if user_method.return_type == method.return_type:
            return_type_points = 1
        # Number parameters points
        if user_method.number_parameters >= method.number_parameters:
            number_parameters_points = user_method.number_parameters / method.number_parameters
        else:
            number_parameters_points = method.number_parameters / user_method.number_parameters

        # Parameter types points
        if len(user_method.parameter_types) > len(method.parameter_types):
            bigger = user_method
            smaller = method.parameter_types
        else:
            bigger = method.parameter_types
            smaller = user_method
        can_match = []
        match = 0
        for i in bigger:
            for j in smaller:
                if i == j and can_match[j] is not False:
                    match += 1
                    can_match[j] = False
        parameter_type_points = match/len(bigger) * 2
        method.points = return_type_points + number_parameters_points + parameter_type_points
    return recommendation_method_list

def generate_methods_to_recommender(method_name):
    similar_methods = list()
    get = MySqlOperator().select_method(method_name)
    for data in get:
        object = RecommendationMethod(data[2], data[3], data[4], data[5])
        similar_methods.append(object)
    return similar_methods

def recommender(method_name, number_parameters, parameter_types, return_type):
    user_method = UserMethod(method_name, number_parameters, parameter_types, return_type)
    recommendation_method_list = generate_methods_to_recommender(method_name)

    recommendation_method_list = rank_methods(user_method, recommendation_method_list)
    recommendation_method_list.sort(key=lambda x: x.points, reverse=True)
    dict_list = []
    for i in recommendation_method_list:
        method_dict = {'code': str(i.code), 'points': str(i.points)}
        dict_list.append(method_dict)
    return json.dumps(dict_list)


    """recommendation_method_list = []
    for similar_method in range(similar_methods):
        method = RecommendationMethod(similar_method, 0)
        recommendation_method_list.append(method)
    recommendation_method_list = rank_methods(user_method, recommendation_method_list)
    recommendation_method_list.sort(key=lambda x: x.points, reverse=True)
    dict_list = []
    for i in recommendation_method_list:
        method_dict = {'code': str(i.code), 'points': str(i.points)}
        dict_list.append(method_dict)
    return json.dumps(dict_list)"""


