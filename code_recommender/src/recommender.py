from sqlconnector import MySqlOperator


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
        points = 0
        
    return recommendation_method_list


def recommender(method_name, number_parameters, parameter_types, return_type):
    user_method = UserMethod(method_name, number_parameters, parameter_types, return_type)
    mysql_operator = MySqlOperator()
    similar_methods = mysql_operator.select_name_from_table(user_method.method_name)
    recommendation_method_list = []
    for similar_method in range(similar_methods):
        method = RecommendationMethod(similar_method, 0)
        recommendation_method_list.append(method)
    recommendation_method_list = rank_methods(user_method, recommendation_method_list)


