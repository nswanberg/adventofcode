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
    valid_game_count = 0

    for line in f.readlines():
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
                if bag[draw_color] < draw_count:
                    valid_row = False
        print(f"Valid row: {valid_row}")
        if valid_row:
            valid_game_count += id

    print("Valid game count:")
    print(valid_game_count)