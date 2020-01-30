import json
import csv

json_file = 'swagger.json'
csv_file = 'apilist.csv'
headers = ["Path", "Action", "Response", "Params", "Description", "Summary", "Tags"]
row = []
param_list = []
PATHS = 'paths'
RESPONSE = 'responses'
PARAMETERS = 'parameters'
PARAM_KEY = 'name'
DESCRIPTION = 'description'
SUMMARY = 'summary'
TAG = 'tags'


def get_params(param_list):
    out_str = ''
    for item in param_list:
        if PARAM_KEY in item:
            out_str += '-{}-'.format(item[PARAM_KEY])
    return out_str


def get_response(responses):
    for (number, description) in responses.items():
        return number


def get_tags(tags):
    out_str = ''
    for tag in tags:
        out_str += '-{}-'.format(tag)
    return out_str


def handle_cases(api_definition):
    if RESPONSE in api_definition:
        row.append(get_response(api_definition[RESPONSE]))
    else:
        row.append('')
    if PARAMETERS in api_definition:
        row.append(get_params(api_definition[PARAMETERS]))
    else:
        row.append('')
    if DESCRIPTION in api_definition:
        row.append(api_definition[DESCRIPTION])
    else:
        row.append('')
    if SUMMARY in api_definition:
        row.append(api_definition[SUMMARY])
    else:
        row.append('')
    if TAG in api_definition:
        row.append(get_tags(api_definition[TAG]))


def write_row_to_csv(row, file):
    with open(file, 'a') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(r for r in row)


def write_to_csv(headers, file):
    with open(file, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(h for h in headers)


def parse(file):
    with open(file) as json_file:
        data = json.load(json_file)
        for (key, value) in data.items():
            if isinstance(value, dict) and key == PATHS:
                for (path, api) in value.items():
                    for (action, definition) in api.items():
                        row.append(path)
                        row.append(action)
                        handle_cases(definition)
                        write_row_to_csv(row, csv_file)
                        row.clear()


write_to_csv(headers, csv_file)
parse(json_file)






