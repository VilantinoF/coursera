name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for lines in handle:
    lines_rstrip = lines.rstrip()
    if lines_rstrip.startswith('From'):
        if lines_rstrip.startswith('From:'):
            continue
        lines_slice = lines_rstrip.split()
        clock_slice = lines_slice[5].split(':')
        dic[clock_slice[0]] = dic.get(clock_slice[0], 0) + 1
for key,value in sorted(dic.items()):
    print(key, value)