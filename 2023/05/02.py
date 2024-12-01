class Mapping:
    def __init__(self, range_text):
        lines = range_text.splitlines()
        self.name = lines[0].replace(" map:", "")
        from_name, to_name = self.name.split("-to-")
        self.from_name = from_name
        self.to_name = to_name
        self.source_ranges = []
        for line in lines[1:]:
            destination_n, source_n, length = [int(n) for n in line.split(" ") if n]
            self.source_ranges.append((source_n, source_n + length - 1, source_n - destination_n))

    def __repr__(self):
        name = ""
        for range in sorted(self.source_ranges, key=lambda x: x[0]):
            name += f"({range[0]},{range[1]}),{range[2]} "
        return name
    
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

with open("test.txt") as f:
    sections = f.read().split("\n\n")
    mappings = {}
    for section in sections[1:]:
        #mapping, name = make_mapping(section)
        mapping = Mapping(section)
        mappings[mapping.get_from_to()] = mapping
    seeds = [int(n) for n in sections[0].replace("seeds: ","").split(" ") if n]
    seeds_to_check = []
    seed_locations = []
    totals_to_check=0
    # Find the smallest seed number
    seed_starts = seeds[::2]
    print(f"seed_starts: {seed_starts}")
    smallest_seed = min([seed for seed in seeds[::2]])
    for i in range(0, len(seeds)-1,2):
        totals_to_check += seeds[i+1]
        for i, seed in enumerate(range(seeds[i], seeds[i]+seeds[i+1])):
            if i % 1000 == 0:
                print(i)
            seeds_to_check.append(seed)
            seed_locations.append(find_location(seed, mappings))
    print(f"totals_to_check: {totals_to_check}")
    print(f"seeds_to_check: {seeds_to_check}")
    print(f"seed_locations: {seed_locations}")
    print([seed_locations[i] - seeds_to_check[i] for i in range(len(seeds_to_check))])
    for mapping in mappings.values():
        print(mapping)
    # Let's start accumulating the source ranges. For every list of ranges, we'll
    # read the start, finish, and offset, find the intersection with existing ranges,
    # and add the offset to the intersection.
    # For the first iteration, there are no existing ranges, so we'll just add the
    # new ranges.
    # For subsequent iterations, we'll find the intersection of the new ranges with
    # the existing ranges. For every intersection, create a new range with the
    # sum of the offsets, and remove the intersection from the existing ranges.

    offset_ranges = []
    # if there are no intersections, add the new ranges
    # if there are intersections, add the new ranges, and remove the intersections
    for mapping in mappings.values():
        for source_start, source_end, offset in mapping.source_ranges:
            new_ranges = []
            for offset_start, offset_end, offset_offset in offset_ranges:
                if source_start > offset_end or source_end < offset_start:
                    # no intersection
                    new_ranges.append((offset_start, offset_end, offset_offset))
                else:
                    # intersection, so 

    print(min(seed_locations))
