import json

def getNum(s):
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

obj = {
    "apart_name": '',
    "apart_img": '',
    "spec" : ''
}

spec_j = {
    "apart_spec": '',
    "apart_floor": '',
    "apart_price": '',
    "apart_profit": ''
}

to_json = {
     "apartment": [],
     "cottege": [],
     "parking": [],
     "commercial": []
}

to_json_struct = {
    "category": '',
    "apartment_info": ''
}

to_json = []

with open('profit.json') as f:
    jsonObj = json.load(f)

for section in jsonObj.items():
    for apart in section[1]:
        for spec in apart['specs']:
            for floor in spec['floors']:
                spec_j['apart_spec'] = spec['apart_spec']
                spec_j['apart_floor'] = floor['apart_floor']
                spec_j['apart_price'] = getNum(floor['apart_price'])
                spec_j['apart_profit'] = floor['apart_profit']
                obj['apart_name'] = apart['apart_name']
                obj['apart_img'] = apart['apart_img']
                obj['spec'] = spec_j


                to_json_struct["category"] = section[0]
                to_json_struct['apartment_info'] = obj

                obj = {
                    "apart_name": '',
                    "apart_img": '',
                    "spec" : ''
                }

                spec_j = {
                    "apart_spec": '',
                    "apart_floor": '',
                    "apart_price": '',
                    "apart_profit": ''
                }
                to_json.append(to_json_struct)

                to_json_struct = {
                    "category": '',
                    "apartment_info": ''
                }

with open('sw_templates.json', 'w') as f:
   json.dump(to_json,  f, indent=2, ensure_ascii=False,)
