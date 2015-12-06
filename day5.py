f = open('input/Day5.txt', 'r')

def is_line_nice(line):
    last_character = None
    vowel_count = 0
    repeated_character = False
    for character in line:
        if last_character:
            last_two_characters = last_character + character
            if last_two_characters in ['ab', 'cd', 'pq', 'xy']:
                return False
        if character in ['a', 'e', 'i', 'o', 'u']:
            vowel_count = vowel_count + 1
        if character == last_character:
            repeated_character = True
        last_character = character
    return vowel_count > 2 and repeated_character

def is_line_better_nice(line):
    has_single_repeat = False
    has_double_repeat = False
    for index in range(0, len(line) - 2):
        character = line[index]
        if character == line[index + 2]:
            has_single_repeat = True
        if character + line[index + 1] in line[index + 2:]:
            has_double_repeat = True
    return has_single_repeat and has_double_repeat

def puzzle9():
    f.seek(0)
    nice_count = 0
    for line in f:
        if is_line_nice(line):
            nice_count = nice_count + 1
    return nice_count

def puzzle10():
    f.seek(0)
    nice_count = 0
    for line in f:
        if is_line_better_nice(line):
            nice_count = nice_count + 1
    return nice_count
