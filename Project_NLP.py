# https://towardsdatascience.com/text-processing-in-python-29e86ea4114c
#https://www.geeksforgeeks.org/implementing-apriori-algorithm-in-python/

import re
import pandas as pd
import nltk
from nltk.tokenize import WordPunctTokenizer
#nltk.download(’stopwords’)
from nltk.corpus import stopwords
# needed for nltk.pos_tag function nltk.download(’averaged_perceptron_tagger’)
#nltk.download(’wordnet’)
#from nltk.stem import WordNetLemmatizer
from apyori import apriori

stop_words = stopwords.words('english')

def tokenizing(text):
    word_punct_token = WordPunctTokenizer().tokenize(text)
    clean_token=[]
    for token in word_punct_token:
        token = token.lower()
        # remove any value that are not alphabetical
        new_token = re.sub(r'[^a-zA-Z]+', '', token) 
        # remove empty value and single character value
        if new_token != "" and len(new_token) >= 2: 
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
# =============================================================================
# def apriori_result(data,):
#     rules = apriori(data, min_support = 0.015,min_confidence = 0.015,min_length=5)
#     return rules
# =============================================================================
#%%
df = pd.read_csv(r'D:\PROJECT\NLP\metadata.csv',encoding='UTF-8')
not_needed=["publish_time","mag_id","who_covidence_id","arxiv_id","license","doi","pubmed_id","pmcid","source_x","sha","pdf_json_files","pmc_json_files","url","s2_id","cord_uid"]
for i in not_needed:
    del df[str(i)]

#print(df.info())
#abstract=list(df['abstract'])
#print(len(abstract))
#data_frame=df.values.tolist()
#%%
#df.drop_duplicates(inplace = True) # DROP DUPLICATES
#print(df.info())

#temp=df.drop(df[df['abstract'].str.len() > 5],axis=1)
df=df[df['abstract'].str.len() > 5]

#%%
#print(df.info())
title=list(df['title'])
abstract=list(df['abstract'])
#authors=list(df['authors'])
#journal=list(df['journal'])
#%%
output = []
# GROUPING OF DUPLICATE ELEMENTS
for a, b in zip([float('nan')] + title,title):
    if a != b:
        output.append([])
    output[-1].append(b)
#%%
count_list=[]
title_mull=[]
for i in output:
#    if (len(i) != 99) and (len(i)>3) :
    if len(i) == 5:
#        print(str(i)+"\n------------")
#        count_list.append(len(i))        
#        print(i[0])
        title_mull.append(i[0])
#%%
abstract_mull=[]
for i in range(len(abstract)):
    if title[i] == title_mull[0]:
        abstract_mull.append()
#%%
print(max(count_list))
#%%
print(len(title))
# ORIGINAL LENGTH : 503803
# Removing Nan and len()<5 : 390187
#%%
# =============================================================================
# for i in abstract:
#     if (len(str(i)) < 5):
#         print(i)
# =============================================================================
#%%
text = "The idea of giving computers the ability to process human language is as old as the idea of computers themselves. This book is about the implementation and implications of that exciting idea. We introduce a vibrant interdisciplinary field with many names corresponding to its many facets, names like speech and language processing, human language technology, natural language processing, computational linguistics, and speech recognition and synthesis. The goal of this new field is to get computers to perform useful tasks involving human language, tasks like enabling human-machine communication, improving human-human communication, or simply doing useful processing of text or speech."
word_punct_token = WordPunctTokenizer().tokenize(text)
#%%
new_abstract=[]
#abstract=list(set(abstract))
title=list(set(title))
for i in range(len(abstract)):
    new_abstract.append(tokenizing(str(title[i])))
    
print(len(new_abstract))
#%%
association_rules = apriori(new_abstract, min_support = 0.05,min_confidence = 0.05,min_length=10)
#results=list(rules)
#%%
for item in association_rules:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
#%%
for i in range(len(results)):
#    print(str(results[i][0])+"|n"+str(results[i][1])+"|n"+str(results[i][2])+"\n------------------------\n-----------------------")
    print(results[i][0])
#%%#print(word_punct_token)

# =============================================================================
# text = "The idea of giving computers the ability to process human language is as old as the idea of computers themselves. This book is about the implementation and implications of that exciting idea. We introduce a vibrant interdisciplinary field with many names corresponding to its many facets, names like speech and language processing, human language technology, natural language processing, computational linguistics, and speech recognition and synthesis. The goal of this new field is to get computers to perform useful tasks involving human language, tasks like enabling human-machine communication, improving human-human communication, or simply doing useful processing of text or speech."
# word_punct_token = WordPunctTokenizer().tokenize(text)
# clean_token=[]
# for token in word_punct_token:
#     token = token.lower()
#     # remove any value that are not alphabetical
#     new_token = re.sub(r'[^a-zA-Z]+', '', token) 
#     # remove empty value and single character value
#     if new_token != "" and len(new_token) >= 2: 
#         vowels=len([v for v in new_token if v in "aeiou"])
#         if vowels != 0: # remove line that only contains consonants
#             clean_token.append(new_token)
# 
# stop_words = stopwords.words('english')
# 
# # add new stopwords to the list
# stop_words.extend(["could","though","would","also","many",'much'])
# print(stop_words)
# 
# # Remove the stopwords from the list of tokens
# tokens = [x for x in clean_token if x not in stop_words]
# =============================================================================


