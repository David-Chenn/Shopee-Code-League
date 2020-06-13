import pandas as pd


id = list()
newnumber = list()

for i in range(101):
    id.append(i)
    newnumber.append(i+2)



df = pd.DataFrame({'id':id,'new_number':newnumber})
df.to_csv('./test.csv',index=False)












