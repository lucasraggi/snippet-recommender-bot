import tensorflow as tf

import PathContextReader
import numpy as np
import time
import pickle
from common import common, VocabType

class Model:
    topk = 10
    num_batches_to_log = 100

    def __init__(self, config):
        self.config = config
        self.sess = tf.Session()

        self.eval_data_lines = None
        self.eval_queue = None
        self.predict_queue = None

        self.eval_placeholder = None
        self.predict_placeholder = None
        self.eval_top_words_op, self.eval_top_values_op, self.eval_original_names_op, self.eval_code_vectors = None, None, None, None
        self.predict_top_words_op, self.predict_top_values_op, self.predict_original_names_op = None, None, None
