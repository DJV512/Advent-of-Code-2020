import time
import utils


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

    adapters = sorted([int(x.strip()) for x in data])

    change1 = 0
    change3 = 0
    current_joltage = 0

    for adapter in adapters:
        if adapter - current_joltage == 1:
            change1 += 1
        elif adapter - current_joltage == 3:
            change3 += 1
        
        current_joltage = adapter
    
    change3 += 1

    return change1 * change3


def part2(data):

    adapters = sorted([int(x.strip()) for x in data])
    adapters.insert(0,0)

    start = 0
    joltage = 0

    subsections = []

    for i in range(len(adapters)):
        if adapters[i]-joltage == 3:
            subsections.append(adapters[start:i])
            start = i
        joltage=adapters[i]
    subsections.append(adapters[start:])

    ways = 1

    for subsection in subsections:
        ways *= num_paths(subsection) 

    return ways


def num_paths(joltages):
    if len(joltages) in [1,2]:
        return 1

    joltage = joltages[0]

    if joltage == max(joltages):
        return 1
    
    total = 0
    total += num_paths(joltages[1:])
    if joltages[2] - joltage <= 3:
        total += num_paths(joltages[2:])
        if len(joltages) > 3:
            if joltages[3] - joltage <= 3:
                total += num_paths(joltages[3:])
    
    return total



if __name__ == "__main__":
    main()