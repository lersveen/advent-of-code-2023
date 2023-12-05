import re

bag_contains = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible_games = []
total = 0
total_power = 0

with open("day2/input.txt") as f:
    for (line_num, line) in enumerate(f):
        game_number = line_num + 1
        # Find every semicolon-separated part of line
        game = re.findall(r'((?:\d+ \w+,?\s?)+)(?>;|\n)', line)

        impossible = False
        
        fewest_needed = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for handful in game:
            handfull_total = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            color_list = handful.split(", ")
            for color in color_list:
                values = color.split(" ")
                color_name = values[1]
                color_count = int(values[0])

                handfull_total[color_name] = handfull_total[color_name] + color_count

                if color_count > fewest_needed[color_name]:
                    fewest_needed[color_name] = color_count

                if color_count > bag_contains[color_name]:
                    impossible = True
                    # print(f"{game_number}: {color_name} = {color_count}")
        
        game_power = fewest_needed["red"] * fewest_needed["green"] * fewest_needed["blue"]
        total_power = total_power + game_power


        if not impossible:
            total += game_number
            possible_games.append(game_number)

print(total_power)
print(total)
