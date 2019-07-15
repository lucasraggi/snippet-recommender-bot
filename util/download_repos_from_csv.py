import pandas as pd
from git import Repo
import os, shutil


# clones all the repo of a csv with a collum named 'links' with the github url to a folder called "java_files"
def download_repos():
    df = pd.read_csv('repos.csv')

    if not os.path.exists('java_files'):
        os.makedirs('java_files')
    else:
        shutil.rmtree('java_files')
        os.makedirs('java_files')

    for index, row in df.iterrows():
        try:
            print(row['links'])
            repo_name = row['links'].split('/')
            repo_name = repo_name[3] + '-' + repo_name[-1] # get user and repo name in the form: 'user/repo_name'
            print(repo_name)
            Repo.clone_from(row['links'], 'java_files/' + repo_name)
        except:
            pass


download_repos()