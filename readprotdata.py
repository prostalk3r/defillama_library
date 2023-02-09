import json

#Open Procools Data - file handle
fh = open("protocols_data.json")

#Load Protocols data
prot_data = json.load(fh)

print("Protocols count:", len(prot_data))

for prot in prot_data:
    print("Name:", prot["name"])
    print("Name:", prot["url"])
    print("###################")


