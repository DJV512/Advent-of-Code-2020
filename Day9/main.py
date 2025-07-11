import time
import utils
from itertools import combinations


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, codes = part1(data)
    part1_time = time.time()
    answer2 = part2(codes, answer1)
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time):.2f} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time):.2f} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time):.2f} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time):.2f} ms")
    print("---------------------------------------------------")


output = True  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    # FILENAME = "sample_input.txt"
    FILENAME = "input.txt"
    
    return utils.parse_input(FILENAME, method="raw_lines")


def part1(data):

    preamble = 25

    codes = [int(x.strip()) for x in data]
    length = len(codes)

    for i in range(preamble, length):
        possible_addends = codes[i-preamble:i]
        possible_sums = [sum(x) for x in combinations(possible_addends, 2)]
        if codes[i] not in possible_sums:
            break

    return codes[i], codes


def part2(codes, invalid):

    length = len(codes)
    found = False

    for i in range(length-2):
        for j in range(i+2, length):
            possible_addends = codes[i:j]
            possible_sum = sum(possible_addends)
            if possible_sum == invalid:
                found = True
                break

            if possible_sum > invalid:
                break
        
        if found:
            break

    min_val = min(possible_addends)
    max_val = max(possible_addends)
    weakness = min_val + max_val

    return weakness


if __name__ == "__main__":
    main()