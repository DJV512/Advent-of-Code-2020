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

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    DIRECTION_TO_INDEX = {d:i for i, d in enumerate(DIRECTIONS)}


    direction = (0, 1)
    position = (0,0)

    for move in data:
        command = move[0]
        amount = int(move[1:])

        if command == "F":
            position = (position[0] + direction[0]*amount, position[1] + direction[1]*amount)
        elif command == "L":
            steps = amount // 90
            index = DIRECTION_TO_INDEX[direction]
            index = (index-steps) % 4
            direction = DIRECTIONS[index]
        elif command == "R":
            steps = amount // 90
            index = DIRECTION_TO_INDEX[direction]
            index = (index+steps) % 4
            direction = DIRECTIONS[index]
        elif command == "N":
            position = (position[0] - amount, position[1])
        elif command == "S":
            position = (position[0] + amount, position[1])
        elif command == "W":
            position = (position[0], position[1] - amount)
        elif command == "E":
            position = (position[0], position[1] + amount)
    
    return utils.manhattan((0,0), position)


def rotate_waypoint(command, amount, waypoint):

    if amount == 180:
        return (waypoint[0]*-1, waypoint[1]*-1)
    
    else:
        if command == "L":
            if amount == 90:
                return (waypoint[1]*-1, waypoint[0])
            else:
                return (waypoint[1], waypoint[0]*-1)
        else:
            if amount == 90:
                return (waypoint[1], waypoint[0]*-1)
            else:
                return (waypoint[1]*-1, waypoint[0])


def part2(data):

    position = (0,0)
    waypoint = (-1, 10)

    for move in data:
        command = move[0]
        amount = int(move[1:])

        if command == "F":
            position = (position[0] + amount * waypoint[0], position[1] + amount * waypoint[1])
        elif command == "L":
            waypoint = rotate_waypoint(command, amount, waypoint)
        elif command == "R":
            waypoint = rotate_waypoint(command, amount, waypoint)
        elif command == "N":
            waypoint = (waypoint[0] - amount, waypoint[1])
        elif command == "S":
            waypoint = (waypoint[0] + amount, waypoint[1])
        elif command == "W":
            waypoint = (waypoint[0], waypoint[1] - amount)
        elif command == "E":
            waypoint = (waypoint[0], waypoint[1] + amount)
    
    return utils.manhattan((0,0), position)


if __name__ == "__main__":
    main()