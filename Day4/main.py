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

    with open(FILENAME) as f:
        data = f.read()
    
    return data


def part1(data):

    passports = data.split("\n\n")
    valid = 0
    for passport in passports:
        if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
            valid += 1

    return valid


def part2(data):
    passports = data.split("\n\n")
    valid = 0
    for passport in passports:
        parts = passport.split()
        good_parts = []
        if len(parts) < 7:
            continue
        else:
            present_and_valid = 0
            for part in parts:
                if "byr" in part:
                    matches = re.findall(r"byr:\d+", part)
                    if matches:
                        if len(matches[0]) != 8:
                            break
                    year = int(part[-4:])
                    if 1920 <= year <= 2002:
                        present_and_valid += 1
                        good_parts.append(part)
                    else:
                        break

                elif "iyr" in part:
                    matches = re.findall(r"iyr:\d+", part)
                    if matches:
                        if len(matches[0]) != 8:
                            break
                    year = int(part[-4:])
                    if 2010 <= year <= 2020:
                        present_and_valid += 1
                        good_parts.append(part)
                    else:
                        break

                elif "eyr" in part:
                    matches = re.findall(r"eyr:\d+", part)
                    if matches:
                        if len(matches[0]) != 8:
                            break
                    year = int(part[-4:])
                    if 2020 <= year <= 2030:
                        present_and_valid += 1
                        good_parts.append(part)
                    else:
                        break

                elif "hgt" in part:
                    matches = re.findall(r"hgt:\d+(?:cm|in)", part)
                    if matches:
                        shortened = matches[0].replace("hgt:", "")
                        unit = shortened[-2:]
                        height = int(shortened[:-2])
                        if unit == "cm":
                            if 150 <= height <= 193:
                                present_and_valid += 1
                                good_parts.append(part)
                            else:
                                break
                        elif unit == "in":
                            if 59 <= height <= 76:
                                present_and_valid += 1
                                good_parts.append(part)
                            else:
                                break
                    else:
                        break

                elif "hcl" in part:
                    matches = re.findall(r"hcl:#[0-9a-f]+", part)
                    if matches:
                        if len(matches[0]) != 11:
                            break
                        else:
                            present_and_valid += 1
                            good_parts.append(part)
                    else:
                        break

                elif "ecl" in part:
                    matches = re.findall(f"ecl:(?:amb|blu|brn|gry|grn|hzl|oth)", part)
                    if matches and len(matches[0]) == 7:
                        present_and_valid += 1
                        good_parts.append(part)
                    else:
                        break

                elif "pid" in part:
                    matches = re.findall(r"pid:\d+", part)
                    if matches:
                        if len(matches[0]) != 13:
                            break
                        else:
                            present_and_valid += 1
                            good_parts.append(part)
                    else:
                        break


            if present_and_valid == 7:
                valid += 1

    return valid


if __name__ == "__main__":
    main()