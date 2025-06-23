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
    return utils.parse_input(FILENAME, method="raw")


def part1(data):

    for line1 in data:
        num1 = int(line1.strip())
        for line2 in data:
            num2 = int(line2.strip())
            if num1 != num2:
                if num1 + num2 == 2020:
                    print(num1, num2)
                    return num1 * num2

    


def part2(data):

    for line1 in data:
        num1 = int(line1.strip())
        for line2 in data:
            num2 = int(line2.strip())
            if num1 != num2:
                for line3 in data:
                    num3 = int(line3.strip())
                    if num1 != num3 and num2 != num3:
                        if num1 + num2 + num3 == 2020:
                            print(num1, num2, num3)
                            return num1 * num2 * num3

    return None


if __name__ == "__main__":
    main()