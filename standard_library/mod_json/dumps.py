import json
from pprint import pprint
import requests

# The dump and dumps methods serialise or pickle data into a JSON format
test_dumps = json.dumps(True)
print(test_dumps)
