import json
import re

ruby_line = ''
try:
    with open('datas/task1_d.json', 'r') as f:
        ruby_line = f.read()
except Exception as e:
    print(e)


cleaned_string = ruby_line.strip()

if cleaned_string.startswith('['):
    cleaned_string = cleaned_string[1:]
if cleaned_string.endswith(']'):
    cleaned_string = cleaned_string[:-1]

json_string = re.sub(r':(\w+)\s*=>', r'"\1":', cleaned_string)
final_json_string = f'[{json_string}]'
print(final_json_string)

data = json.loads(final_json_string)
print(json.dumps(data, indent=4))

try:
    with open('datas/task1_cleaned.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data successfully saved")
except IOError as e:
    print(f"Error saving file: {e}")

