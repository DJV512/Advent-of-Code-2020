import time
import utils

from copy import deepcopy


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(deepcopy(data))
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

    layout = data
    
    while True:
        new_layout = [["x" for x in range(width)] for y in range(length)]
        for y in range(length):
            for x in range(width):
                occupied = 0
                seat = layout[y][x]
                if seat == ".":
                    new_layout[y][x] = "."
                    continue
                for direction in utils.DIRS_8:
                    next_y = y+direction[0]
                    next_x = x+direction[1]
                    if 0 <= next_y < length and 0 <= next_x < width:
                        if layout[next_y][next_x] == "#":
                            occupied += 1
                if seat == "L":
                    if occupied == 0:
                        new_layout[y][x] = "#"
                    else:
                        new_layout[y][x] = "L"
                elif seat == "#":
                    if occupied >= 4:
                        new_layout[y][x] = "L"
                    else:
                        new_layout[y][x] = "#"
                else:
                    print("ERROR - Seat Type Not Definec")
        
        if new_layout == layout:
            break
        else:
            layout = new_layout

    return sum(1 for y in layout for x in y if x == "#")


def part2(data):

    length = len(data)
    width = len(data[0])

    layout = data
    
    while True:
        new_layout = [["x" for x in range(width)] for y in range(length)]
        for y in range(length):
            for x in range(width):
                occupied = 0
                seat = layout[y][x]
                if seat == ".":
                    new_layout[y][x] = "."
                    continue
                for direction in utils.DIRS_8:
                    next_y = y+direction[0]
                    next_x = x+direction[1]
                    if 0 <= next_y < length and 0 <= next_x < width:
                        if layout[next_y][next_x] == "#":
                            occupied += 1
                        elif layout[next_y][next_x] == "L":
                            continue
                        elif layout[next_y][next_x] == ".":

                            to_inc = {}
                            to_dec = {}
                            to_stay = {}

                            if next_y - y == 1:
                                to_inc["next_y"] = next_y
                            elif next_y - y == -1:
                                to_dec["next_y"] = next_y
                            else:
                                to_stay["next_y"] = next_y

                            if next_x - x == 1:
                                to_inc["next_x"] = next_x
                            elif next_x - x == -1:
                                to_dec["next_x"] = next_x
                            else:
                                to_stay["next_x"] = next_x

                            while True:
                                for key in to_inc:
                                    to_inc[key] += 1
                                for key in to_dec:
                                    to_dec[key] -= 1
                                
                                for d in [to_inc, to_dec, to_stay]:
                                    if "next_x" in d:
                                        temp_x = d["next_x"]
                                    if "next_y" in d:
                                        temp_y = d["next_y"]

                                if 0 <= temp_y < length and 0 <= temp_x < width:
                                    
                                    if layout[temp_y][temp_x] == "#":
                                        occupied += 1
                                        break
                                    if layout[temp_y][temp_x] == "L":
                                        break
                            
                                else:

                                    break
                                
                if seat == "L":
                    if occupied == 0:
                        new_layout[y][x] = "#"
                    else:
                        new_layout[y][x] = "L"
                elif seat == "#":
                    if occupied >= 5:
                        new_layout[y][x] = "L"
                    else:
                        new_layout[y][x] = "#"
                else:
                    print("ERROR - Seat Type Not Defined")

        
        if new_layout == layout:
            break
        else:
            layout = new_layout

    return sum(1 for y in layout for x in y if x == "#")


if __name__ == "__main__":
    main()