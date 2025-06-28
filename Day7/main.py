import time
import utils
import re


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, rules = part1(data)
    part1_time = time.time()
    answer2 = part2(rules)
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

    all_bags = set()
    rules = {}
    direct_containers = []
    for line in data:
        outer_bag, inner_bags = line.split(" bags contain ")
        inner_bags = inner_bags.strip().replace(" bags", "")
        inner_bags = inner_bags.replace(" bag", "")
        inner_bags = inner_bags.replace(".", "")
        inner_bags = inner_bags.replace("no other", "")
        rules[outer_bag] = inner_bags.split(", ")
        if "shiny gold" in inner_bags:
            direct_containers.append(outer_bag)
            all_bags.add(outer_bag)
    
    total = len(direct_containers)
    new = True
    while new:
        new = False
        new_direct_containers = set()
        for rule in rules:
            for container in rules[rule]:
                for direct_container in direct_containers:
                    if direct_container in container:
                        if rule not in all_bags:
                            new_direct_containers.add(rule)
                            all_bags.add(rule)
                            new = True
        total += len(new_direct_containers)
        direct_containers = list(new_direct_containers)

    return total, rules


def part2(rules):

    containers = rules["shiny gold"]
    total = 0

    while containers:
        new_containers = []
        for container in containers:
            number = re.findall(r"\d+", container)
            if number:
                number = number[0]
                total += int(number)
                next_bag = container.replace(number, "").strip()
                for _ in range(int(number)):
                    for bag in rules[next_bag]:
                        new_containers.append(bag)
        
        containers = new_containers
        
    return total


if __name__ == "__main__":
    main()