import json
import pandas as pd


def load_docs():
    with open('./data/news.json', encoding='utf-8-sig') as document:
        for (i, _) in enumerate(document):
            try:
                yield i
            except:
                pass


def load_indices():
    with open('./data/posting_list.json', encoding='utf-8-sig') as document:
        return json.load(document)


indices = load_indices()
token_name_indices = [index['token_name'] for index in indices]

data_frame = pd.DataFrame(index=token_name_indices)

for doc_id in load_docs():
    for index in indices:
        if (doc_id in index['docs']):
            data_frame.at[index['token_name'], doc_id] = 1
        else:
            data_frame.at[index['token_name'], doc_id] = 0

if(__name__ == '__main__'):
    data_frame.to_excel('./data/boolean_model.xlsx')