import json
import random

def getNum(s):
    #print(type(s))
    if (isinstance(s, int)):
        return s
    l = len(s)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))
    if (len(integ)):
        integ[0] *= 1000
        return integ[0]
    return 0

with open('pre_final.json') as f:
    jsonObj = json.load(f)


for section in jsonObj.items():
    for apart in section[1]:
            for spec in apart['specs']:
                for floor in spec['floors']:
                     floor['apart_profit'] = int(getNum(floor['apart_price'])/10000+random.randint(-5, 5))*1000 

with open('sw_templates.json', 'w') as f:
   json.dump(jsonObj,  f, indent=2, ensure_ascii=False,)
