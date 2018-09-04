import json
import pandas as PD
from pandas.io.json import json_normalize

FILE1 = open (r"D:\Programing\python\vscode_python_git\Firebase\FireBasesep01.json","r")
JA = json.load(FILE1)
FIREBASE=PD.DataFrame()

'''
                        In the below sample dataset I have taken the last not null value
"value": {
    "string_value": null,
    "int_value": "1534986000000",  
    "float_value": null,
    "double_value": null,
    "set_timestamp_micros": "1534982472692000"
    }
'''

for I in JA:
    FIREBASE_DICT={}
    EVENT_PARAM={}
    USER_PROPERTIES={}
    for K,V in I.items():
        if K == 'event_params':
            for EPI in V:
                EPK=EPI['key']
                for EPVV in EPI['value'].values():
                    if EPVV is not None:
                        EPV=EPVV
                EVENT_PARAM[EPK] = EPV
        elif K== 'user_properties':
            for UPI in V:
                UPK=UPI['key']
                for UPDV in UPI['value'].values():
                    if UPDV is not None:
                        UPV=UPDV
                USER_PROPERTIES[UPK] = UPV
        else:
            FIREBASE_DICT[K]=V
        FIREBASE_DICT['EVENT_PARAM']=EVENT_PARAM
        FIREBASE_DICT['USER_PROPERTIES']=USER_PROPERTIES
    LOOPDF=json_normalize(FIREBASE_DICT)
    FIREBASE=PD.concat([FIREBASE,LOOPDF], axis=0, join='outer', ignore_index=True,sort=False)

FILE1.close()
print(FIREBASE.info(verbose=True),end='\n')
print(FIREBASE.shape,end='\n')
print(FIREBASE.columns,end='\n')
print(FIREBASE.head())

# for C in FIREBASE.columns:
#     NEW=''
#     NEW = C.replace('.','_')
#     FIREBASE.rename(columns= {C:NEW},inplace=True)

FIREBASE.to_csv(r"D:\Programing\python\vscode_python_git\Firebase\Firebase_Data.csv")
    # F.to_json(orient='table', date_format="iso")
