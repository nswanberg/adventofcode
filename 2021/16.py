from itertools import islice
import sys
from operator import mul
from functools import reduce


arg = sys.argv[1]

if ".txt" in arg:
    with open("16.txt") as f:
        input = f.read().strip()
else:
    input = arg

def get_type(val):
    conv=int(val, 2)
    if conv == 4:
        return 'literal'
    return 'unknown'

def to_binary(st):
    res=""
    for c in st:
        res+=f"{int(c,16):04b}"
    return res

def get_packet_type(bin_st):
    ver = int(bin_st[:3],2)
    typ = int(bin_st[3:3+3],2)
    return (ver,typ)

def decode_packets(input_bits, input_end, i=0, packet_count=sys.maxsize):
    versions = []
    ret = []
    packets=0
    print(f"decoding from {i} to {input_end}")
    while i < input_end and packets < packet_count and (input_end - i) >= 11:
        six_bits=input_bits[i:i+6]
        i+=6
        ver, typ = get_packet_type(six_bits)
        versions.append(ver)
        if typ == 4:
            print(f"looking for number")
            i, num = decode_number(i, input_bits)
            print(f"got num {num}")
            ret.append(num)
            packets+=1
        else:
            print(f"decoding operator {typ}")
            i, decoded_versions, decoded_nums = decode_operator(i, input_bits)
            print(f"got {len(decoded_nums)} nums for type {typ}")
            packets+=1
            versions += decoded_versions
            if typ == 0:
                ret = [sum(decoded_nums)]
            elif typ == 1:
                ret = [reduce(mul, decoded_nums, 1)]
            elif typ == 2:
                ret = [min(decoded_nums)]
            elif typ == 3:
                ret = [max(decoded_nums)]
            elif typ == 5:
                ret = [1] if decoded_nums[0] > decoded_nums[1] else [0]
            elif typ == 6:
                ret = [1] if decoded_nums[0] < decoded_nums[1] else [0]
            elif typ == 7:
                ret = [1] if decoded_nums[0] == decoded_nums[1] else [0]
            else:
                raise Exception(f"Invalid type {typ}")
    return i, versions, ret
    


def decode_number(i, input_bits):
    done=False
    number=""
    while not done:
        next_bits=input_bits[i:i+5]
        i+=5
        number+=next_bits[1:]
        if next_bits[0] == '0':
            done=True
    return i, int(number,2)


def decode_operator(i, input_bits):
    I = input_bits[i]
    i+=1
    if I == '0':
        sub_packet_length = input_bits[i:i+15]
        i+=15
        bits_long = int(sub_packet_length,2)
        print(f"looking for packets in {bits_long} bits")
        i, versions, nums = decode_packets(input_bits, i+bits_long, i=i)
    else:
        sub_packet_length = input_bits[i:i+11]
        i+=11
        sub_packet_count = int(sub_packet_length,2)
        print(f"looking for {sub_packet_count} packets")
        i, versions, nums = decode_packets(input_bits,
                                len(input_bits),
                                i=i,
                                packet_count=sub_packet_count)
    return i, versions, nums

nums=[]
versions=[]

bin_input = to_binary(input)

_, versions, nums = decode_packets(bin_input, len(bin_input))
print(sum(versions))
print(nums)


