import re
import sys
import os

numwords = {
    "one": "1",
    "two": "2", 
    "three": "3", 
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def insert_substring(string, position, substring):
    string = string[:position] + substring + string[position:] 
    return string

def replace_outer_numwords(string):
    first_start = last_end = None
    first_word = last_word = None

    for word in numwords.keys():
        for match in re.finditer(word, string):
            if first_start is None or match.start() < first_start:
                first_start = match.start()
                first_word = match.group(0)

            if last_end is None or match.end() > last_end:
                last_end = match.end()
                last_word = match.group(0)

    if first_word:
        string = insert_substring(string, first_start, numwords[first_word])
        # string = str.replace(string, first_word, numwords[first_word])

    if last_word:
        string = insert_substring(string, last_end, numwords[last_word])
        # string = str.replace(string, last_word, numwords[last_word])

    return string


def sum_values(file: str, convert_numwords: bool):
    total = 0
    with open(file) as f:
        for line in f:
            if convert_numwords:
                # Convert first and last number word to digits
                line = replace_outer_numwords(line)

            # Strip anything else than numbers
            line_only_numbers = re.sub(r'[^0-9]+', '', line)

            # Find first digit
            first_match = re.search("^([0-9]?)", line_only_numbers)
            first = first_match.group(0) if first_match else 0

            # Find last digit
            last_match = re.search("([0-9]?)$", line_only_numbers)
            last = last_match.group(0) if last_match else 0

            # Combine first and last digits
            line_value = "".join([first, last])

            total += int(line_value)

    return total


if __name__ == "__main__":
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        print(f'Part one: {sum_values(sys.argv[1], False)}')
        print(f'Part two: {sum_values(sys.argv[1], True)}')
    else:
        print("Please supply a valid file path as argument")
        sys.exit(1)
