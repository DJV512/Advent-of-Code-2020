"""Solution for day 4, part 2 puzzle on aventofcode.com"""

import re

valid_passports = 0

with open(file='input.txt',mode='rt',encoding='utf-8',newline='\n') as file:
    file_list = file.read().split('\n\n')
    file_list_curated = []
    passport_data = []
    for item in file_list:
        file_list_curated.append(item.replace('\n',' '))
    for item in file_list_curated:
        x = item.split()
        dictionary_temp = {}
        for key_value in x:
            key_value = key_value.split(':')
            key = key_value[0]
            value = key_value[1]
            dictionary_temp.update({key:value})
        passport_data.append(dictionary_temp)


def passport_field_check(p_data):
    keys = p_data.keys()
    if ('byr' in keys and
        'iyr' in keys and
        'eyr' in keys and
        'hgt' in keys and
        'hcl' in keys and
        'ecl' in keys and
        'pid' in keys):
        return True


def passport_byr_check(byr):
    if 1920 <= int(byr) <= 2002:
        return True


def passport_iyr_check(iyr):
    if 2010 <= int(iyr) <=2020:
        return True


def passport_eyr_check(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True


def passport_hgt_check(hgt):
    if hgt.endswith('cm'):
        hgt = int(hgt.strip('cm'))
        if 150 <= hgt <= 193:
            return True
    elif hgt.endswith('in'):
        hgt = int(hgt.strip('in'))
        if 59 <= hgt <= 76:
            return True


def passport_hcl_check(hcl):
    p = re.compile('#[a-z0-9]{6}')
    if len(hcl) > 7:
        return False
    if p.match(hcl):
        return True


def passport_ecl_check(ecl):
    if (ecl == 'amb' or
        ecl == 'blu' or
        ecl == 'brn' or
        ecl == 'gry' or
        ecl == 'grn' or
        ecl == 'hzl' or
        ecl == 'oth'):
        return True


def passport_pid_check(pid):
    p = re.compile('[0-9]{9}')
    if len(pid) != 9:
        return False
    if p.match(pid):
        return True


def main():
    global valid_passports
    for passport in passport_data:
        if (passport_field_check(passport) is True and
            passport_byr_check(passport.get('byr')) is True and
            passport_iyr_check(passport.get('iyr')) is True and
            passport_eyr_check(passport.get('eyr')) is True and
            passport_hgt_check(str(passport.get('hgt'))) is True and
            passport_hcl_check(str(passport.get('hcl'))) is True and
            passport_ecl_check(str(passport.get('ecl'))) is True and
            passport_pid_check(str(passport.get('pid'))) is True):

            valid_passports += 1
            print(passport)
            print()


main()

print(valid_passports)