import json

data = []
data_dic = {
    "CategoryEn1": [],
    "CategoryFa1": [],
    "CategoryEn2": [],
    "CategoryFa2": [],
    "NewsDate": [],
    "NewsTitle": [],
    "NewsBody": [],
    "GetComments": [],
}
i = 0
j = 0
max_len = 0
x = None
counter = 0
with open('./data/news.json', encoding='utf-8-sig') as f:
    for line in f:
        read_json = json.loads(line)
        try:
            catPJ = read_json['GetComments']['CommentsJsonArray']
            if(len(catPJ) > max_len):
                max_len = len(catPJ)
                x = catPJ
                j = i
            i+=1
        except:
            counter += 1
            pass
        # if(i==10):
            # print("CategoryPanel : ", read_json['CategoryPanel'])
            # print("NewsDate : ", read_json['NewsDate'])
            # print("NewsTitle : ", read_json['NewsTitle'])
            # print("NewsSummary : ", read_json['NewsSummary'])
            # print("NewsBody : ", read_json['NewsBody'])
            # print("GetComments : ", read_json['GetComments'])
            # print("-----------------------------------------------")
            # print(read_json)
        # i = i +1
        # if i == :
        #     break
print(max_len)
print(j)
# print(x)
print(counter)
