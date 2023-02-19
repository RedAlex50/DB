import json

with open('pre_final.json') as f:
    jsonObj = json.load(f)

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
    
apart_json = {
    "apart_name" : '',
    "specs" : []
}
spec_json = {
    "apart_spec" : '',
    "floors" : []
}
floors = []
floor_json = {
    "apart_floor" : '',
    "apart_price" : 0,
    "apart_profit": 0,
}

o_json = {
    "apartment" : [],
    "cottege" : [],
    "parking" : [],
    "commercial" : []        
}

index = 0
for section in jsonObj.items():
    apart_name = ''
    n = 0
    first = 1
    for apart in section[1]:
        # print(apart)
        
        spec_ind = 0
        floor_ind = 0
            
        if first:
            apart_json = apart
            first = 0
        elif (apart_json['apart_name'] == apart['apart_name']):
            n += 1
            spec_ind = 0
            apart_json['specs'] = apart['specs']

            # добавить к среднем
        else:
            if n == 0:
                n = 1
            for spec in apart_json['specs']:
                spec_ind += 1
                floor_ind = 0
                for floor in spec['floors']:
                    floor_ind += 1
                    floor['apart_price'] = getNum(floor['apart_price'])
            if index == 0:
                o_json['apartment'].append(apart_json)
            if index == 1:
                o_json['cottege'].append(apart_json)
            if index == 2:
                o_json['parking'].append(apart_json)
            if index == 3:
                o_json['commercial'].append(apart_json)
            apart_json = apart
            n = 0
            # посчитать среднее
    
    
    index += 1
            
with open('sw_templates.json', 'w') as f:
   json.dump(o_json,  f, indent=2, ensure_ascii=False,)
