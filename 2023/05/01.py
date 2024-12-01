class Mapping:
    def __init__(self, range_text):
        lines = range_text.splitlines()
        #print(lines)
        self.name = lines[0].replace(" map:", "")
        #print(f"Making mapping: {self.name}")
        from_name, to_name = self.name.split("-to-")
        self.from_name = from_name
        self.to_name = to_name
        self.source_ranges = []
        for line in lines[1:]:
            destination_n, source_n, length = [int(n) for n in line.split(" ") if n]
            #print(f"mapping {self.name}")
            #print(f"source_n: {source_n}, destination_n: {destination_n}, length: {length}")
            self.source_ranges.append((source_n, source_n + length, source_n - destination_n))

    def __repr__(self):
        return str((self.from_name,self.to_name))
    
    def get_from_to(self):
        return self.from_name, self.to_name

    def get_mapping(self,n):
        ret = None
        for source_start, source_end, offset in self.source_ranges:
            if source_start <= n < source_end:
                ret = n - offset
                break
        if ret == None:
            ret = n
        #print(f"{self.from_name} {n} -> {self.to_name} {ret}")
        return ret

def make_mapping(range_text):
    mapping = Mapping(range_text)
    return mapping, mapping.get_from_to() 

def find_location(seed_number, mappings):
    order_of_operations = ['seed','soil','fertilizer','water','light','temperature','humidity','location']
    order_of_operations_pairs = [(order_of_operations[i], order_of_operations[i+1]) for i in range(len(order_of_operations)-1)]
    next_n = seed_number
    for ooop in order_of_operations_pairs:
        mapping = mappings[ooop]
        next_n = mapping.get_mapping(next_n)
    return next_n

with open("05.txt") as f:
    sections = f.read().split("\n\n")
    seeds = [int(n) for n in sections[0].replace("seeds: ","").split(" ") if n]
    #print(seeds)
    mappings = {}
    for section in sections[1:]:
        mapping, name = make_mapping(section)
        mappings[name] = mapping
    #print(mappings)
    seed_locations = []
    for seed in seeds:
        seed_locations.append(find_location(seed, mappings))
    print(min(seed_locations))
