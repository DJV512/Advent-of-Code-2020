import time
import utils


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, answer2 = part1(data)
    part1_time = time.time()
    # answer2 = part2(data)
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


def narrow_down(char, low, high):
    
    if char in ["B", "R"]:
        low = low + (high - low + 1) // 2
    elif char in ["F", "L"]:
        high = high - (high - low + 1) // 2
    
    return low, high


def part1(data):

    ids = []
    for seat in data:
        seat = seat.strip()
        row_low = 0
        row_high = 127
        seat_low = 0
        seat_high = 7
        for i, char in enumerate(seat):
            if i < 7:
                row_low, row_high = narrow_down(char, row_low, row_high)
            else:
                seat_low, seat_high = narrow_down(char, seat_low, seat_high)

        ids.append(row_low * 8 + seat_low)

    ids = sorted(ids)

    for i, id in enumerate(ids):
        if i == 0:
            pass
        else:
            if id - ids[i-1] == 2:
                seat = id-1
                break

    return max(ids), seat


if __name__ == "__main__":
    main()