from code2vec import main



def main():
    json = '{\"method\":[\"test_0\",\"test_1\"]," + "\"code\":[\"public static void method_test_0()\\n{\\n\\t" + "System.out.println(\\\"Clara Maria\\\");\\n}\",\"public static " + "void method_test_1()\\n{\\n\\tSystem.out.println(\\\"João Messias\\\"" + ");\\n}\"], \"num_codes\":2}'
    list_return = main(['--load', '../models/incomplete_dataset2/saved_model_iter30', '--predict'])
    print(list_return[0]['name'])
