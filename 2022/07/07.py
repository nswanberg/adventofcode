from collections import defaultdict
import pprint

def cd(new_dir, state):
    if new_dir == "..":
        state["path"] = state["path"][:-1]
        return
    state["path"] = state["path"] + (new_dir,)

def ls(state):
    state["getting_ls"] = True

def is_command(line):
    return line[0] == "$"

def parse_command(line):
    if not is_command(line):
        return (None,None)
    return line[2:4], line[5:]

def parse_ls_out(line, state):
    if line[:4] == "dir ":
        return
    size, _ = line.split(' ')
    # Add the size to the current directory and parent directories
    state["dirs"][state["path"]] += int(size)
    for i in range(len(state["dirs"])):
        state["dirs"][state["path"][:-i]] += int(size)

with open("07.txt") as f:
    lines = f.readlines()

    state = {
        "path": tuple(),
        "getting_ls": False,
        "dirs": defaultdict(int),
    }

    for line in lines:
        line = line.strip()

        # line is either a command or output
        # if command, then execute the command and update the state
        # if output, retrieve the output until the next command

        cur_command, argv = parse_command(line)
        if cur_command:
            # If we had been getting ls output, that's now done
            if state["getting_ls"]:
                state["getting_ls"] = False
            if cur_command == "cd":
               cd(argv, state)
            elif cur_command == "ls":
               ls(state)
            else:
               raise Exception(f"Invalid command {cur_command}")
        elif state["getting_ls"]:
            parse_ls_out(line, state)
        else:
            raise Exception("invalid state")

    total = 0
    dirs = state["dirs"]
    for d in dirs.items():
        if d[1] < 100000:
            total += d[1]
    print(total)


    # Part 2

    TOTAL_FS_SIZE = 70000000
    NEEDED = 30000000

    TOTAL_USED = dirs[('/',)]
    TOTAL_FREE = TOTAL_FS_SIZE - TOTAL_USED
    NEEDED_TO_DELETE = NEEDED - TOTAL_FREE

    candidates = []
    for d in dirs.items():
        if d[1] > NEEDED_TO_DELETE:
            candidates.append(d[1])
            print(sorted(candidates))

