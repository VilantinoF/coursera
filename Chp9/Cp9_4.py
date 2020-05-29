name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
dic = dict()
for lines in handle:
    if lines.startswith('From'):
        if lines.startswith('From:'):
            continue
        lines_rstrip = lines.rstrip()
        split_lines = lines_rstrip.split()
        dic[split_lines[1]] = dic.get(split_lines[1], 0) + 1

bigvalue = None
bigkey = None
for key,value in dic.items():
    if bigvalue is None or value > bigvalue:
        bigkey = key
        bigvalue = value
print(bigkey, bigvalue)