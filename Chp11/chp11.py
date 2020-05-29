import re

file_input = input("")
if len(file_input) < 1: file_input = "regex_sum_42.txt"
file_handle = open(file_input)
result = 0
for lines in file_handle:
    lines_rstrip = lines.rstrip()
    number = re.findall('[0-9]+', lines_rstrip)
    number = list(map(int, number))
    if len(number) < 1: continue
    for i in number:
        result += i
print(result)