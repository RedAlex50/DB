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

with open('out_250122.json') as f:
    jsonObj = json.load(f)

with open('out_110622.json') as f1:
    jsonObj1 = json.load(f1)

a = []
for section in jsonObj1.items():
    a.append(section)
    # print(section)

i = -1
for section in jsonObj.items():
    i += 1
    #print(section[0])
    for apart in section[1]:
        s = apart['apart_name'][:-1]
        s = s[:s.find(',')]
        # print('  ' + s)
        apart['apart_name'] = s
        #print('  ' + apart['apart_name'])
        ind_sp = -1
        for spec in apart['specs']:
            ind_sp += 1
            s1 = spec['apart_spec'][:-1]
            if (s1.find('кв. (')) + 1:
                s2 = s1[:s1.find('кв. (') + 3]
            elif (s1.find('комн.')) + 1:
                s2 = s1[:s1.find('комн.') + 5]
            elif (s1.find('.,')) + 1:
                s2 = s1[:s1.find('.,') + 1]
            elif (s1.find('омещени')) + 1:
                s2 = s1[:s1.find('омещени') + 8]
            else:
                s2 = s1
            # print('    ' + s2)
            spec['apart_spec'] = s2
            #print('    ' + spec['apart_spec'])
            ind_fl = -1
            for floor in spec['floors']:
                ind_fl += 1
                if ind_sp < len(a[i][1]):
                    if ind_fl < len(a[i][1][ind_sp]['specs']):
                        print(a[i][1][ind_sp]['specs'][ind_fl]['floors'])
                floor['apart_profit'] = getNum(floor['apart_price'])# - getNum(a[i][1]['specs'][ind_sp]['floors'][ind_fl]['apart_price'])
                # print('      ' + floor['apart_floor'][:-1])
                # print('      ' + floor['apart_price'][:-1])
    #print(section)

with open('sw_templates_2.json', 'w') as f:
   json.dump(jsonObj,  f, indent=2, ensure_ascii=False,)
