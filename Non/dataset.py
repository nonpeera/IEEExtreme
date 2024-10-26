import csv
from collections import defaultdict

# Sample input data as list of strings
data = [
    "Event ID,Event Title,Acronym,Project Code,3 Digit Project Code,Record Type",
    "a094x00000EXYC2,\"IEEE Nanotechnology Symposium (ANTS)\",\"ANTS\",,,\"Parent Event\"",
    "a094x00000Bm0iK,\"2020 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)\",\"ANTS\",2069D,69D,\"IEEE Event\"",
    "a094x00000Bm0uC,\"2021 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)\",\"ANTS\",2169D,69D,\"IEEE Event\"",
    "a094x00001IYXBs,\"2022 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)\",\"ANTS\",2269D,69D,\"IEEE Event\"",
    "a094x00000Bm0Hb,\"2018 IEEE Nanotechnology Symposium (ANTS)\",\"ANTS\",18M86,M86,\"IEEE Event\"",
    "a094x00000BlzyU,\"2017 IEEE Nanotechnology Symposium (ANTS)\",\"ANTS\",17M86,M86,\"IEEE Event\"",
    "a094x00000Bm01T,\"2017 IEEE Australia New Zealand Student and Young Professional Congress (ANZSCON)\",\"ANZSCON\",17M74,M74,\"IEEE Event\"",
    "a094x00000EXXtT,\"IEEE Arctic and Northern Oceans Forum (ANOF)\",\"ANOF\",,,\"Parent Event\"",
    "a094x00000Bm0U3,\"2019 IEEE Arctic and Northern Oceans Forum (ANOF)\",\"ANOF\",19U27,U27,\"IEEE Event\"",
    "a094x00000EXYG4,\"IEEE Workshop on Animation in Virtual and Augmented Environments (ANIVAE)\",\"ANIVAE\",,,\"Parent Event\"",
    "a094x00000Bm0CS,\"2018 IEEE 1st Workshop on Animation in Virtual and Augmented Environments (ANIVAE)\",\"ANIVAE\",18P57,P57,\"IEEE Event\"",
    "a094x00000Bm0TB,\"2019 IEEE 2nd Workshop on Animation in Virtual and Augmented Environments (ANIVAE)\",\"ANIVAE\",19P57,P57,\"IEEE Event\"",
    "a094x00000EXYG1,\"IEEE Workshop on Advanced NeuroTechnologies for Brain Initiatives (ANTBI)\",\"ANTBI\",,,\"Parent Event\"",
    "a094x00000EXXu2,\"IEEE Brain Initiative Workshop on Advanced NeuroTechnologies for BRAIN Initiatives (ANTBI)\",\"ANTBI\",,,\"Parent Event\"",
    "a094x00000Blzml,\"2016 IEEE Workshop on Advanced NeuroTechnologies for Brain Initiatives (ANTBI)\",\"ANTBI\",16H29,H29,\"IEEE Event\"",
]

# Parsing CSV input
reader = csv.DictReader(data)

# Organize records by Acronym and Event Type
children_by_acronym = defaultdict(list)
parent_by_acronym = {}
for record in reader:
    acronym = record["Acronym"]
    record_type = record["Record Type"]

    if record_type == "Parent Event":
        parent_by_acronym[acronym] = record
    elif record_type == "IEEE Event":
        children_by_acronym[acronym].append(record)

# Filtering and setting the 3 Digit Project Code
output = []
for acronym, parent in sorted(parent_by_acronym.items()):
    children = children_by_acronym.get(acronym, [])

    # Exclude parents without children and standalone children
    if not children:
        continue

    # Check if all children have the same 3 Digit Project Code
    child_codes = {child["3 Digit Project Code"] for child in children}
    if len(child_codes) == 1:
        parent["3 Digit Project Code"] = child_codes.pop()
    else:
        parent["3 Digit Project Code"] = "???"

    # Add parent to output
    output.append(parent)
    
    # Sort children by title, and if titles are the same, by Event ID
    sorted_children = sorted(children, key=lambda x: (x["Event Title"], x["Event ID"]))
    for child in sorted_children:
        child["Parent ID"] = parent["Event ID"]
        output.append(child)

# Print output in the specified format
for record in output:
    if "Parent ID" in record:
        print(f'{record["Event ID"]},"{record["Event Title"]}","{record["Acronym"]}",{record["Project Code"]},{record["3 Digit Project Code"]},"{record["Record Type"]}",{record["Parent ID"]}')
    else:
        print(f'{record["Event ID"]},"{record["Event Title"]}","{record["Acronym"]}",{record["Project Code"]},{record["3 Digit Project Code"]},"{record["Record Type"]}"')
