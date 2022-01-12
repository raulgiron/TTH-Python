import re


with open ("basics.txt", "r") as file_object:
    data = file_object.read()
    
    first = re.match(r"Four", data)
    liberty = re.search(r"Liberty", data)

