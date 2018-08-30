import numpy as np
import pandas as pd
data=pd.DataFrame(data=pd.read_csv('/home/weblab-sys-11/Documents/2nd.csv'))
concepts=np.array(data.iloc[:,0:-1])
target=np.array(data.iloc[:,-1])
def learn(concepts,target):
    specific_h=concepts[0].copy()
    print("initialization of specific_h and general_h")
    print(specific_h)
    general_h=[["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print(general_h)
    for i,h in enumerate(concepts):
        if(target[i]=="YES"):
            for x in range(len(specific_h)):
                if(h[x]!=specific_h[x]):
                    specific_h[x]='?'
                    general_h[x][x]='?'
        if(target[i]=="NO"):
             for x in range(len(specific_h)):
                if(h[x]!=specific_h[x]):
                    general_h[x][x]=specific_h[x]
        else:
             general_h[x][x]='?'
        print("steps of candidate eleminate algo",i+1)
        print(specific_h)
        print(general_h)
    indicies=[i for i,val in enumerate(general_h) if val==['?','?','?','?','?','?']]
    for i in indicies:
        general_h.remove(['?','?','?','?','?','?'])
    return specific_h,general_h
s_final,g_final=learn(concepts,target)
print("final specific_h",s_final)
print("final general_h",g_final)
                    