from git import Repo
import re 
import time

REPO_PATH = './skale/skale-manager'                  # Dirección del repo donde vas a buscar los commits
KEY_WORDS = ['credentials','password','key']         # Palabras que vas a buscar en los commits 


def extract(REPO_PATH):
    repo = Repo(REPO_PATH)                           # Accedes a la información del repo y la guardas para poder procesarla más tarde
    
    return repo

def transform(repo):
    res = []
    commits_list = list(repo.iter_commits())         # Sacas del repo los commits para poder procesarlos y filtrar
    for secuence in commits_list:
        for word in KEY_WORDS:
            if re.search(word, secuence.message, re.IGNORECASE):
                res.append('{} - {}'.format(secuence.hexsha, secuence.message))
                
    return res

def load(res): 
    counter = 1
    for commit in res:
        print('Commit',counter)
        print(commit)
        counter+=1
    time.sleep(1)
    

if __name__=='__main__':
    repo = extract(REPO_PATH)
    res = transform(repo)
    print('\nThere have been found',len(res),'commits:\n')
    load(res)
    