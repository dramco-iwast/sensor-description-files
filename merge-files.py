import yaml
import json
from yamlinclude import YamlIncludeConstructor # https://pypi.org/project/pyyaml-include/


YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.BaseLoader)

with open('sensors.yaml') as f:
    data = yaml.load(f, Loader=yaml.BaseLoader)

print(data)

with open('./dist/sensors-merged.json', 'w') as outfile:
    json.dump(data, outfile)