import re
phone='9845678800'
patterns=r'^\d{3}-\d{3}-\d{4}$'

if re.fullmatch(patterns,phone):
    print("valid")
else:
    print("invalid")