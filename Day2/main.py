import time
import utils
import re
from collections import Counter


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data)
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
    
    return utils.parse_input(FILENAME, method="raw")


def part1(data):
    valid = 0
    for line in data:
        parts = line.strip().split()
        matches = re.findall(r"\d+", parts[0])
        low = int(matches[0])
        high = int(matches[1])
        letter_to_match = parts[1][0]
        count = Counter(parts[2])
        if low <= count[letter_to_match] <= high:
            valid += 1
        
    return valid


def part2(data):
    valid = 0
    for line in data:
        parts = line.strip().split()
        matches = re.findall(r"\d+", parts[0])
        first = int(matches[0])
        second = int(matches[1])
        letter_to_match = parts[1][0]
        if parts[2][first-1] == letter_to_match and parts[2][second-1] != letter_to_match or parts[2][first-1] != letter_to_match and parts[2][second-1] == letter_to_match:
            valid += 1

    return valid


if __name__ == "__main__":
    main()