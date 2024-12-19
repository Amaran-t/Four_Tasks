import json
import sys

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def fill_values(tests, values_dict):
    for test in tests:
        if "id" in test and test["id"] in values_dict:
            test["value"] = values_dict[test["id"]]
        if "values" in test:
            fill_values(test["values"], values_dict)

def create_values_dict(values):
    values_dict = {}
    for item in values:
        key = item["id"]
        value = item["value"]
        values_dict[key] = value
    return values_dict

tests_file = sys.argv[1]
values_file = sys.argv[2]
report_file = sys.argv[3]

tests = read_json(tests_file)
values = read_json(values_file)

if isinstance(values, dict) and "values" in values:
    values = values["values"]

values_dict = create_values_dict(values)
fill_values(tests["tests"], values_dict)

with open(report_file, 'w', encoding='utf-8') as file:
    json.dump(tests, file, indent=4, ensure_ascii=False)
