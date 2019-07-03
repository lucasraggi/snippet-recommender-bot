# Code2Algo: Snippet Recommender Bot

## Code Identifier (Code2vec)
Identifies the name of the algorithm given the code, even if the code is incomplete
#### Preprocess files
> source preprocess.sh

#### Train Model
> source train.sh

#### Evaluate Trained Model
> python3 code2vec.py --load models/java14_model/saved_model_iter8 --test data/my_dataset/my_dataset.test.c2v

## Code Recommender
Given the algorithm name and the incomplete code it searches in pre-selected projects, the algorithm function that best fits the incomplete code given

## API
<center style="padding: 40px"><img width="70%" src="https://github.com/lucasraggi89/snippet-recommender-bot/blob/master/images/architecture.png" /></center>

After installing the dependencies in requirements.txt, to run the api, in the code_identifier/src/ run:
> python tool_api.py
### Routes
#### Route: /plugin Type: POST
* Get json in the format: 
>{"_class": ..., "method": ..., "code": ...}  

where "_class" is the class name and "method" is the method name
* Returns json in the format: 
>{'method_name': ..., 'method_code': ..., 'method_points': ..., 'num_codes': ...}
#### Route: /code Type: POST
* Get string with the incomplete code snippet
* Returns string with the best fitting algorithm code
#### Route: /identifier Type: POST
* Get string with the incomplete code snippet
* Returns string with the best fitting algorithm name
#### Route: /code_name Type: POST
* Get string with the algorithm name
* Returns string with the best fitting algorithm code

## Recommender Database
Some links from repositories that have been extracted methods to compose our database used for recommendation:

* https://github.com/TheAlgorithms/Java
* https://github.com/aryak93/GFG-Java-Implementations
* https://github.com/shivam-maharshi/algorithms
* https://github.com/rampatra/Algorithms-and-Data-Structures-in-Java
* https://github.com/scaffeinate/crack-the-code.git 
* https://github.com/bhavikambani/samplecodes
* https://github.com/neerajjain92/data-structures
* https://github.com/sunilmvn/algorithms-leetcode
* https://github.com/hashanp/algorithms-java
