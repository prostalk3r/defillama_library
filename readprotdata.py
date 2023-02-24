import json

#Open Procools Data - file handle
fh = open("protocols_data.json")

#Load Protocols data
prot_data = json.load(fh)

print("Protocols count:", len(prot_data))

count = 0
for prot in prot_data:
    count = count + 1
    if count < 10:
        print("Name:", prot["name"])
        print("Name:", prot["url"])
        print("###################")
    else:
        print("#### END ####")
        break



