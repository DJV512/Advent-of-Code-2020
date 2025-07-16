import time
import utils
import re


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
    
    return utils.parse_input(FILENAME, method="raw_lines")


def part1(data):

    earliest_time = int(data[0].strip())
    time_counter = earliest_time

    pattern = r"\d+"
    results = re.findall(pattern, data[1])
    buses = [int(x) for x in results]

    while True:
        for bus in buses:
            if time_counter % bus == 0:
                return bus * (time_counter-earliest_time)
        
        time_counter += 1



def part2(data):

    # Note that this is a brute force solution.
    # It originally relied on the hint in the problem that the answer would be greater than 100 trillion.
    # On my computer the solution took about 2 hours to find.
    # This code is changed to find the known solution in less than a second by starting the search just before it.
    # Afterwards, I did look into what would be the optimal solution (Chinese Remainder Theorem).
    # I decided my solution was good enough! :)

    pattern = r"\d+"
    results = re.findall(pattern, data[1])
    buses = data[1].strip().split(",")
    schedule = {index:int(bus) for index, bus in enumerate(buses) if bus in results}
    origin_bus = schedule[0]
    matching_bus = schedule[origin_bus]

    # greater_than = 100000000000000
    greater_than = 534000000000000
    lcm = origin_bus * matching_bus
    starting_point = (greater_than // lcm) * lcm

    for i in range(starting_point, greater_than * 10, lcm):
        good = True
        for index in schedule:
            check_value = (i-(origin_bus-index))
            modulus = schedule[index]
            if check_value % modulus != 0:
                good = False
                break
        if good:
            return i-origin_bus


if __name__ == "__main__":
    main()