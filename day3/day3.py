import re

matches = []
actual_part_numbers = []
part_number_sum = 0
gears = {}

lines = []
with open("day3/input.txt") as f:
    for line in f:
        lines.append(line)

for (line_num, line) in enumerate(lines):
    line_num = line_num + 1
    for match in re.finditer(r'\d+', line):
        matches.append({
            "number": int(match.group(0)),
            "line": line_num,
            "start": int(match.start()),
            "end": int(match.end())
        })

for match in matches:
    found = False
    for (line_num, line) in enumerate(lines):
        line_num = line_num + 1
        if line_num in range(max(match['line']-1, 1), match['line']+2):
            start = max(match['start']-1, 0)
            end = min(match['end']+1, len(line)-1)

            for part_match in re.finditer(r'[^0-9.]', line[start:end]):
                found = True
                if part_match.group(0) == "*":
                    part_start = start + part_match.start()
                    part_end = start + part_match.end()
                    gear = f'{line_num}-{part_start}'

                    if gears.get(gear):
                        gears[gear].append(match['number'])
                    else:
                        gears.update({
                            gear: [match['number']]
                        })

    if found:
        actual_part_numbers.append(match['number'])
        part_number_sum += match['number']

gear_sum = 0

for gear, numbers in gears.items():
    if len(numbers) == 2:
        gear_ratio = numbers[0] * numbers[1]
        gear_sum = gear_sum + gear_ratio

print(gear_sum)
print(part_number_sum)
