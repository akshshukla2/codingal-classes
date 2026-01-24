# imp : read_csv , head ,  tail , info
# replacing specific columns :-
# df["Name"].fillna(130, inplace="True")

import numpy as np
import pandas as pd 

examdata = { 
    "Name" : ["Akshita","Rudraksh","Prashant","Avni","Ritika","Kaavya","Navya","Nabhay","Naman","Neeraj"],
    "Score" : [20,-1,20,18,12,np.nan,15,18,np.nan,7],
    "Attempts" : [1,7,2,1,3,1,2,2,3,2],
    "Qualify" : ["Hell yes", "Unfortunately yes.", "Yes","Yes","Yes","Yes","No","No","No","Yes"]
}

label= ["a","b","c","d","e","f","g","h","i","j"]

df = pd.DataFrame(examdata, index=label)

print(df.info())
print(df)
