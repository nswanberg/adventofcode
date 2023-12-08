# Input numbers
bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def get_id_from_raw(raw):
    id_str = raw.replace("Game ", "").replace(":", "")
    return int(id_str)

def get_draw_count_color(draw_string):
    draw_string = draw_string.strip()
    count, color = draw_string.split(" ")
    return int(count), color

with open("02.txt") as f:
    power_total = 0

    for line in f.readlines():
        red_count = 0
        green_count = 0
        blue_count = 0
        valid_row = True
        line = line.strip()
        print(line)
        id_raw, draw_groups = line.split(":")
        id = get_id_from_raw(id_raw)
        draw_strings = draw_groups.split("; ")
        for draw_string in draw_strings:
            # Split by commas
            for draw_string_color in draw_string.split(", "):
                draw_count, draw_color = get_draw_count_color(draw_string_color)
                if draw_color == "red" and draw_count > red_count:
                    red_count = draw_count
                elif draw_color == "green" and draw_count > green_count:
                    green_count = draw_count
                elif draw_color == "blue" and draw_count > blue_count:
                    blue_count = draw_count
        print(f"red count: {red_count}")
        print(f"green count: {green_count}")
        print(f"blue count: {blue_count}")
        power = red_count*green_count*blue_count
        power_total += power

    print(power_total)