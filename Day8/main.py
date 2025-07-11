import time
import utils


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, seen = part1(data)
    part1_time = time.time()
    answer2 = part2(data, seen)
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

    i = 0
    seen = set()
    accumulator = 0

    while i not in seen:
        seen.add(i)

        parts = data[i].strip().split()
        op = parts[0]
        value = int(parts[1])
        
        if op == "nop":
            i += 1 
        elif op == "acc":
            accumulator += value
            i += 1
        else:
            i += value
    

    return accumulator, seen


def part2(data, possibles):

    length = len(data)

    for change in possibles:
        if "acc" in data[change]:
            continue

        i = 0
        seen = set()
        accumulator = 0

        while i not in seen and i < length:
            seen.add(i)

            parts = data[i].strip().split()
            op = parts[0]
            value = int(parts[1])

            if i == change:
                if op == "nop":
                    op = "jmp"
                else:
                    op = "nop"
            
            if op == "nop":
                i += 1 
            elif op == "acc":
                accumulator += value
                i += 1
            else:
                i += value
        
        if i >= length:
            break

    return accumulator



if __name__ == "__main__":
    main()