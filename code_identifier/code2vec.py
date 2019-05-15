from argparse import ArgumentParser
import sys

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-d", "--data", dest="data_path",
                        help="path to preprocessed dataset", required=False)
    parser.add_argument("-te", "--test", dest="test_path",
                        help="path to test file", metavar="FILE", required=False)

    is_training = '--train' in sys.argv or '-tr' in sys.argv
    parser.add_argument("-s", "--save", dest="save_path",
                        help="path to save file", metavar="FILE", required=False)
    parser.add_argument("-w2v", "--save_word2v", dest="save_w2v",
                        help="path to save file", metavar="FILE", required=False)
    parser.add_argument("-t2v", "--save_target2v", dest="save_t2v",
                        help="path to save file", metavar="FILE", required=False)
    parser.add_argument("-l", "--load", dest="load_path",
                        help="path to save file", metavar="FILE", required=False)
    parser.add_argument('--save_w2v', dest='save_w2v', required=False,
                        help="save word (token) vectors in word2vec format")
    parser.add_argument('--save_t2v', dest='save_t2v', required=False,
                        help="save target vectors in word2vec format")
    parser.add_argument('--export_code_vectors', action='store_true', required=False,
                        help="export code vectors for the given examples")
    parser.add_argument('--release', action='store_true',
                        help='if specified and loading a trained model, release the loaded model for a lower model '
                             'size.')
    parser.add_argument('--predict', action='store_true')
    args = parser.parse_args()

