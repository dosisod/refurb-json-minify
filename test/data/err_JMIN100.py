import json
from json import dump, dumps

# these should match

with open("file.json", "w+") as f:
    json.dump([], f)
    json.dump([], f, sort_keys=True)
    dump([], f)

json.dumps([])
json.dumps([], sort_keys=True)
json.dumps([], indent=None)
json.dumps([], sort_keys=True, indent=None)
dumps([])


# these should not

with open("file.json", "w+") as f:
    json.dump([], f, separators=(", ", ": "))
    json.dump([], f, separators=(",", ": "))
    json.dump([], f, separators=(", ", ":"))
    json.dump([], f, separators=(",", ":"))

json.dumps([], separators=(",", ":"))

json.dumps([], indent=1)

json.dump([])  # type: ignore
json.dumps()  # type: ignore
