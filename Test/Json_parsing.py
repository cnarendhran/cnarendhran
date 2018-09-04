import json
import pandas as PD
from pandas.io.json import json_normalize
FILE1 = open(r"D:\BI\Doc\Json\ASP_Req_Res_log20180831.json", "r")
F=PD.DataFrame()
# alldata = json.loads(open(qbfile))
# type(alldata)
for ALINE in FILE1:
    D=json.loads(ALINE)
    E=json_normalize(D)
    F=PD.concat([F,E], axis=0, join='outer', ignore_index=True,sort=False)
FILE1.close()
print('Result is printed as follows ',end='\n\n\n')
print(F.shape)
print(F.columns)
print(F.head())
F=F.drop(['tvService.gracenote.searchResult.errors'],axis=1)
for C in F.columns:
    NEW=''
    NEW = C.replace('.','_')
    F.rename(columns= {C:NEW},inplace=True)

F.to_csv(r'D:\BI\Doc\Json\JSON2CSV1.csv')
# F.to_json(orient='table', date_format="iso")
