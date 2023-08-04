#Importing required module
import json
import pandas as pd
import numpy as np

#Loading Documents
def load_docs():
    with open('./data/news.json', encoding='utf-8-sig') as document:
        for (i, _) in enumerate(document):
            try:
                yield i
            except:
                pass

#Loading the indices
def load_indices():
    with open('./data/posting_list.json', encoding='utf-8-sig') as document:
        return json.load(document)


#Inverse Document Frequency
 
# def inverse_doc_freq(term):

    # return np.log(total_documents/term['ferquency'])

def term_Frequency(term, doc_id):
    """
    Calculates the term frequency for a term in a document.
    """
    counter = 0
    if doc_id in term['docs']:
        
    else:
        return 0

def tf_idf(term, doc_id):
    """
    Calculates the tf-idf score for a term in a document.
    """
    tf = (1 + np.log(term_Frequency(term, doc_id)))
    idf = (np.log10(total_documents/term['frequency']))

    return tf * idf

indices = load_indices()
token_name_indices = [index['token_name'] for index in indices]

data_frame = pd.DataFrame(index=token_name_indices)

 

if(__name__ == '__main__'):
    data_frame.to_excel('./data/TF-IDF_Vectors.xlsx')
