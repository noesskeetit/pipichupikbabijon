# with open("unserved_json_file.txt", "r", encoding="utf-8") as infile, open("output_json.txt", 'w', encoding = "utf-8") as outfile:
#     for line in infile:
#         if  "\\n" not in line.lower() and "утр" not in line.lower() and "👅" not in line.lower() and "👆" not in line.lower() and len(line.strip().split()) > 4:
#             outfile.write(line)


file = open("unserved_json_file.txt", 'r', encoding="utf-8")

lines = file.readlines()
lis = []
[lis.append(x) for x in lines if x not in lis]

f = open("bibichupik.txt", 'w', encoding="utf-8")
counter = 0
for item in lis:
    item = '"'+item+'"'
    f.write(item)
    counter += 1
print(counter)