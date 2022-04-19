#%%
import re
import pandas as pd
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from apyori import apriori

stop_words = stopwords.words('english')
stop_words = stop_words + ['conclusions', 'conclusion']

def tokenizing(text):
    word_punct_token = WordPunctTokenizer().tokenize(text)
    clean_token=[]
    for token in word_punct_token:
        token = token.lower()
        if token in ["coronavirus","cov"]:
            token="covid"
        # remove any value that are not alphabetical
        new_token = re.sub(r'[^a-zA-Z]+', '', token) 
        # remove empty value and single character value
        if new_token != "" and len(new_token) > 2: 
            vowels=len([v for v in new_token if v in "aeiou"])
            if vowels != 0: # remove line that only contains consonants
                clean_token.append(new_token)
    tokens = [x for x in clean_token if x not in stop_words]
    tokens = list(set(tokens))
#    print(tokens)
#    text=""
#    for i in tokens:
#        text=text+" "+i
    return tokens
#%%
df = pd.read_csv(r'D:\PROJECT\NLP\metadata.csv',encoding='UTF-8')
#df.columns
#title=list(df["title"])
title=list(df["abstract"])

print(len(title))
#%%
clean=[]
for i in range(len(title)):
    clean.append(tokenizing(str(title[i])))
print(len(clean))    
#%%
#association_rules = apriori(clean, min_support = 0.05,min_confidence = 0.05,min_length=4)
association_rules = apriori(clean, min_support=0.05, min_confidence=0.05, min_lift=3, min_length=2)
#association_rules = apriori(clean, min_support=0.05, min_confidence=0.05, min_length=2)
association_rules=list(association_rules)
#%%
x=[]
for item in association_rules:
    
    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    x.append(items[0])
#    print(items)
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

print("Length : "+str(len(association_rules)))
