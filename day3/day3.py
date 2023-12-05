import re

lines = []
with open("day3/input.txt") as f:
    for line in f:
        lines.append(line)

matches = []
actual_part_numbers = []
part_number_sum = 0

for (line_num, line) in enumerate(lines):
    line_num = line_num + 1
    for match in re.finditer(r'\d+', line):
        matches.append({
            "number": int(match.group(0)),
            "line": line_num,
            "start": int(match.start()),
            "end": int(match.end())
        })
#print(matches)

for match in matches:
    found = False
    for (line_num, line) in enumerate(lines):
        line_num = line_num + 1
        if line_num in range(max(match['line']-1, 1), match['line']+2):
            start = max(match['start']-1, 0)
            end = min(match['end']+1, len(line)-1)
            if match['number'] == 511:
                print(f'{line_num}: {start} to {end}')
                print(line[start:end])
            if re.search(r'[^0-9.]', line[start:end]):
                found = True
    if found:
        #if match['number'] not in actual_part_numbers:
        actual_part_numbers.append(match['number'])
        part_number_sum += match['number']

print("---")
print(len(actual_part_numbers))
print(len(matches))
print(part_number_sum)