from collections import defaultdict
from os import umask

with open('12.txt') as f:
    maplines = f.readlines()

nodes=defaultdict(list)
for line in maplines:
    a,b = line.split('-')
    a=a.strip()
    b=b.strip()
    nodes[a]+=[b]
    nodes[b]+=[a]

def is_bigcave(c):
    return c.isupper()

paths=()

def find_paths(current_node, nodes, path):
    paths = []
    path = path + (current_node,)

    if current_node == 'end':
        return paths + [path]

    path_counts = defaultdict(int)
    for node in path:
        if not is_bigcave(node):
            path_counts[node] += 1
    
    if current_node == 'start' and path_counts[current_node] == 2:
        return paths

    if path_counts[current_node] == 3:
        return paths

    if not is_bigcave(current_node):
        other_nodes_in_path = [n for n in path if n != current_node]
        other_path_counts = defaultdict(int)
        for node in other_nodes_in_path:
            if not is_bigcave(node):
                other_path_counts[node] += 1

        if  2 in other_path_counts.values() and path_counts[current_node] == 2:
            return paths

    for node in nodes[current_node]:
        paths += find_paths(node, nodes, path)
    return paths

print(len(find_paths('start', nodes, ())))

good_paths = """
start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end"""

# good_paths = set(good_paths.strip().split('\n'))

# all_paths = find_paths('start', nodes, ())

# joined_paths = []
# for path in all_paths:
#     joined_paths.append(','.join(path))

# print("extra paths")
# for path in joined_paths:
#     if path not in good_paths:
#         print(path)

# print("not discovered paths")
# for path in good_paths:
#     if path not in joined_paths:
#         print(path)
# print("end not discovered")

# print(len(all_paths))