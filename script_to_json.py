import json


floors_json = {
    "apart_floor" : '',
    "apart_price" : '',
}
floors = []
specs_json = {
    "apart_spec" : '',
    "floors" : '',
}
specs = []
apartment_json = {
    "apart_name" : '',
    "specs" : '',
}
apartment = []
b_in_name = 0
b_in_spec = 0
i = 0

with open('output_250122.txt') as fh:
    for line in fh:
        i += 1
        if 'apart_floor' in line:
            floors_json['apart_floor'] = line[17: ]
        if 'apart_price' in line:
            floors_json['apart_price'] = line[17: ]
            floors.append(floors_json)
            floors_json = {
                "apart_floor" : '',
                "apart_price" : '',
            }
        if 'apart_spec' in line:
            if b_in_spec:
                specs_json['floors'] = list(floors)
                specs.append(specs_json)
                specs_json = {
                    "apart_spec" : '',
                    "floors" : '',
                }
                floors = []
            specs_json['apart_spec'] = line[14: ]
            b_in_spec += 1
        if 'apart_name' in line:
            # print(apartment_json)
            if b_in_spec:
                specs_json['floors'] = list(floors)
                if specs_json['apart_spec'] != "":
                    specs.append(dict(specs_json))
                specs_json = {
                    "apart_spec" : '',
                    "floors" : '',
                }
                floors = []
                b_in_spec = 0
            if b_in_name:
                apartment_json['specs'] = list(specs)
                apartment.append(apartment_json)
                apartment_json = {
                    "apart_name" : '',
                    "specs" : '',
                }
                specs = []

            apartment_json['apart_name'] = line[12:]
            b_in_name += 1


specs_json['floors'] = list(floors)
specs.append(specs_json)
apartment_json['specs'] = list(specs)
apartment.append(apartment_json)
floors = []
specs = []

print(i)
to_json = {
    'apartment' : apartment
}

with open('sw_templates.json', 'w') as f:
    json.dump(to_json,  f, indent=2, ensure_ascii=False,)
