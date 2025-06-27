import time
import utils
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
    
    return utils.parse_input(FILENAME, method="raw_read")


def part1(data):

    running_sum = 0
    parts = data.split("\n\n")
    for part in parts:
        count = Counter(part)
        if "\n" in count:
            running_sum += len(count) - 1
        else:
            running_sum += len(count)

    return running_sum


def part2(data):
    running_sum = 0
    parts = data.split("\n\n")
    for part in parts:
        count = Counter(part)
        print(repr(part))
        print(count)
        if "\n" in count:
            for char in count:
                if char == "\n":
                    continue
                else:
                    if count[char] == count["\n"] + 1:
                        running_sum += 1
        else:
            running_sum += len(count)
        print(f"{running_sum=}")
        print()
        
    return running_sum


if __name__ == "__main__":
    main()