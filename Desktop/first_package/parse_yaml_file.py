# import pyyaml module
import yaml
from yaml.loader import SafeLoader
def parse_yaml(yaml_file):
    methods = dict()
    # Open the file and load the file
    with open(yaml_file) as f:
        data = yaml.load(f, Loader=SafeLoader)
        for endpoint in data['paths']:
            methods[endpoint] = []
            for method in data['paths'][endpoint]:
                methods[endpoint].append(method)
    return methods
required_data=parse_yaml('swagger.yaml')
print(required_data)
