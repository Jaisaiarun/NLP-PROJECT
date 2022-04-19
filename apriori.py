import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import simplejson as json
from apyori import apriori
import apyori
import csv

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

#dataset = pd.read_csv('H://tocsvdata.csv',error_bad_lines = False)
#row_count = sum(1 for row in dataset)
#col_count = sum(1 for column in dataset)
#print(row_count,col_count)
#row_count=row_count-1;
#col_count=col_count-1;
data1 = []
data=[]



# f1=open(r"C:\Users\jaisa\Desktop\node.csv",'a',encoding='UTF-8')
# f2=open(r"C:\Users\jaisa\Desktop\edge.csv",'a',encoding='UTF-8')


# =============================================================================
# with open(r"metadata.csv",'r',encoding='UTF-8') as f:
#      rdr = csv.reader(f)
#      data1 = list(rdr)
# =============================================================================

# =============================================================================
# with open(r"C:\Users\jaisa\Desktop\RUNS\RUN-62\cluster2.csv",'r',encoding='UTF-8') as f:
# #with open(r"C:\Users\jaisa\Desktop\TEXT.csv",'r') as f:
#     rdr = csv.reader(f)
#     data1 = list(rdr)
# print(len(data1))
# no=int(len(data1))
# =============================================================================
#%%
df = pd.read_csv(r'D:\PROJECT\NLP\metadata.csv',encoding='UTF-8')
not_needed=["publish_time","mag_id","who_covidence_id","arxiv_id","license","doi","pubmed_id","pmcid","source_x","sha","pdf_json_files","pmc_json_files","url","s2_id","cord_uid"]
for i in not_needed:
    del df[str(i)]

#print(df.info())
#abstract=list(df['abstract'])
#print(len(abstract))
data_frame=df.values.tolist()
#%%
#df.drop_duplicates(inplace = True) # DROP DUPLICATES
#print(df.info())

#temp=df.drop(df[df['abstract'].str.len() > 5],axis=1)
df=df[df['abstract'].str.len() > 5]

#%%
print(df.info())
title=list(df['title'])
abstract=list(df['abstract'])
authors=list(df['authors'])
journal=list(df['journal'])
#%%
print(len(title))
# ORIGINAL LENGTH : 503803
# Removing Nan and len()<5 : 390187
#%%
for i in abstract:
    if (len(str(i)) < 5):
        print(i)
#%%

for i in range(len(abstract)):
    
#%%
deletelist=[]
deletelist=['looks', 'outta', 'phone','costume', 'easter','require','day','ago','urgent', 'voice', 'yesterday','fine','drivers', 'driving', 'facing','reaches', 'sample', 'school', 'sluts','called','weekend','upon','sunday', 'team', 'pick', 'reached', 'rolling', 'running', 'sale', 'select', 'holiday', 'husband', 'movement', 'movies','group','five','fart', 'favorite','actually', 'bit',  'break', 'came', 'caught', 'coming', 'concern', 'cute', 'damn', 'dance', 'else', 'end', 'enough', 'eyes', 'feels', 'forever', 'friday', 'fuck', 'gave', 'gets', 'gives', 'goes', 'gotta', 'happy', 'hard', 'hate', 'hit', 'honestly', 'hope', 'hoping', 'hot', 'hours', 'jungle', 'kid', 'kids', 'lately', 'let', 'liked', 'makes', 'making', 'miss', 'mom', 'music', 'needs', 'nothing','parents', 'people', 'pitch', 'playing', 'pollen', 'puppy', 'put', 'radio', 'ray', 'ready', 'remember', 'rocket', 'saying', 'says', 'season', 'set', 'song', 'soon', 'sore', 'started', 'starts', 'state', 'summer', 'swear', 'taking', 'teenage', 'things', 'tho', 'thought', 'told', 'tryna', 'twitter', 'wait', 'wanna', 'watching', 'went', 'whole', 'working', 'world', 'yeah', 'yet','let','degree','damn','cute','coming', 'concern', 'break', 'came','bit','institute', 'interests', 'johnson', 'leader' ,'annual', 'combining', 'conversation','physicianlocation', 'pipfellow', 'prof', 'program', 'research', 'san', 'talks', 'turn','paincan','get', 'within','stage','prevalance','got','know', 'like', 'new', 'one','almost', 'already', 'also', 'always', 'another', 'around', 'ass', 'away','back','best', 'better', 'big','cabin', 'catch','come', 'could','dog','check','dream', 'due','early','even', 'ever', 'every', 'everyone','feel', 'feeling','find', 'first', 'found', 'free', 'fucking', 'full', 'getting','give', 'giving', 'going', 'gonna', 'good', 'great', 'green', 'hay','help','home','join', 'keep','last', 'lead','listen','linked','lol','look','looking','love','made','make','may','might','major','many','must' ,'need', 'never', 'news', 'night', 'nowplaying', 'null','often', 'play', 'please','read', 'real', 'really', 'right','said', 'saturday', 'say', 'scarlet', 'see','shit', 'show','signs', 'since','someone', 'something', 'spring', 'start', 'still', 'stop', 'study', 'little', 'live','man','million', 'much','sure','take', 'talk','tell', 'thanks', 'thing', 'think','time', 'today', 'two','use','via','want','watch','way','week','well','without','work','would','year','years','yellow','video']

for d in data1:
    tempdata = []
    for dd in d:
        if dd.isupper():
            dd=dd.lower()
        if dd == 'diseases':
            dd='disease'
        if dd not in deletelist and dd.find('id'):
            tempdata.append(dd)
    #if d not in deletelist:
    data.append(list(set(tempdata)- {''}))
#print(data[0])
#for row in range(0,):
 #   print(data)
  #  data.append([str(dataset.values[row,col]) for col in range(0,1555)])
    

rules = apriori(data, min_support = 0.015,min_confidence = 0.015,min_length=5)
#print(rules)
results = list(rules)
#listRules = [list(results[i][0]) for i in range(0,len(results))]

#print(listRules)
#print(results[1][1])
#%%
size=[]
key=[]
con=[]
edge=[]
target=[]
source=[]
k=[]
edge=[]
for i in range(len(results)):
    if len(k)==3:
        continue
    k=list(results[i][0])
    if len(k)==1:
        key.append(k[0])
        size.append(results[i][1])
    if len(k)==2:
        source.append(k[0])
        target.append(k[1])
        edge.append(results[i][1])

print(key)
print(size)
print(source)
print(target)
print(edge)
for i in range(len(key)):
    f1.write(key[i]+',')
    f1.write(str(no)+'\n')

for i in range(len(source)):
    f2.write(source[i]+',')
    f2.write(target[i]+',')
    f2.write(str(edge[i]*100)+',')
    f2.write(str(no)+'\n')
        
f1.close()
f2.close()
#%%
output=[]
ou=int(0)
f1=open(r"C:\Users\jaisa\Desktop\API-"+str(no)+".txt","w")
f = open(r"C:\Users\jaisa\Desktop\API.txt","a")
for RelationRecord in results:
        #o=StringIO()
#    print("in")
    ou=ou+1
#    print(RelationRecord)
    apyori.dump_as_json(RelationRecord,f)
    apyori.dump_as_json(RelationRecord,f1)
    #output.append(json.loads(f.getvalue()))
#data_df = pd.DataFrame(output)

f.close()
f1.close()
#print(output)
print(ou)
#print(results)

"""f = open("results.txt",'w',encoding='utf-8')
for i in results:
    f.write(str(i))
    f.write("\n")
    #print(str(i))
f.close()"""
