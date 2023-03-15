import json
from json import dump, dumps

# these should match

_ = json.dumps(1234)  # noqa: JMIN100
_ = json.dumps(1234, indent=None)  # noqa: JMIN100
_ = dumps(0)  # noqa: JMIN100

num = 999
_ = json.dumps(num)  # noqa: JMIN100

with open("file.json", "w+") as f:
    json.dump(1234, f)  # noqa: JMIN100
    dump(1234, f)  # noqa: JMIN100


# these should not

_ = json.dumps("hello world")  # noqa: JMIN100
_ = json.dumps([1, 2, 3])  # noqa: JMIN100
_ = json.dumps({})  # noqa: JMIN100
