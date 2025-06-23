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
    
    return utils.parse_input(FILENAME, method="grid_list")


def part1(data):

    length = len(data)
    width = len(data[0])
    x = 0
    y = 0
    trees = 0
    while y < length:
        if data[y][x % width] == "#":
            trees += 1
        x += 3
        y +=1

    return trees


def part2(data):

    length = len(data)
    width = len(data[0])
    trees_on_slopes = []
    slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    for slope_y, slope_x in slopes:
        trees = 0
        y=0
        x=0
        while y < length:
            if data[y][x % width] == "#":
                trees += 1
            x += slope_x
            y += slope_y
        trees_on_slopes.append(trees)
    
    total = 1
    for trees in trees_on_slopes:
        total *= trees

    return total


if __name__ == "__main__":
    main()