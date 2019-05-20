from code_identifier.src.common import common
from code_identifier.src.extractor import Extractor

SHOW_TOP_CONTEXTS = 10
MAX_PATH_LENGTH = 8
MAX_PATH_WIDTH = 2
JAR_PATH = 'JavaExtractor/JPredict/target/JavaExtractor-0.0.1-SNAPSHOT.jar'


class InteractivePredictor:
    exit_keywords = ['exit', 'quit', 'q']

    def __init__(self, config, model):
        model.predict([])
        self.model = model
        self.config = config
        self.path_extractor = Extractor(config,
                                        jar_path=JAR_PATH,
                                        max_path_length=MAX_PATH_LENGTH,
                                        max_path_width=MAX_PATH_WIDTH)

    def read_file(self, input_filename):
        with open(input_filename, 'r') as file:
            return file.readlines()

    def predict(self):
        input_filename = 'Input.java'
        list_return = []
        predict_lines, hash_to_string_dict = self.path_extractor.extract_paths(input_filename)
        results, code_vectors = self.model.predict(predict_lines)
        prediction_results = common.parse_results(results, hash_to_string_dict, topk=SHOW_TOP_CONTEXTS)
        for i, method_prediction in enumerate(prediction_results):
            # print('Original name:\t' + method_prediction.original_name)
            list_return = method_prediction.predictions[0:3]
            print(list_return)
        return list_return
