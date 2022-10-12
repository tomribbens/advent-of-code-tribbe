from aocd.models import Puzzle


def is_valid_pw(pw):
    if not len(pw) == 8 and not pw.islower():
        return False

    invalid_chars = ['i', 'o', 'l']
    if any(char in pw for char in invalid_chars):
        return False

    prev = pw[0]
    pairs = 0
    straight_members = 1
    has_straight = False
    overlap = False
    for char in pw[1:]:
        if char == prev and not overlap:
            pairs += 1
            straight_members = 1
            overlap = True
        elif len(prev) and ord(prev) + 1 == ord(char):
            straight_members += 1
            if straight_members == 3:
                has_straight = True
            prev = char
            overlap = False
        else:
            prev = char
            straight_members = 1
            overlap = False

    if not has_straight or pairs < 2:
        return False

    return True


def get_next_pw(pw):
    pw_ascii = [ord(char) for char in pw]
    new_pw = ""

    while not is_valid_pw(new_pw):
        pw_ascii[-1] += 1

        for idx in reversed(range(len(pw_ascii))):
            if pw_ascii[idx] > ord('z'):
                pw_ascii[idx] = ord('a')
                if idx > 0:
                    pw_ascii[idx - 1] += 1

        new_pw = ''.join([chr(x) for x in pw_ascii])
    return new_pw


def solve(data):
    part_a = get_next_pw(data)
    part_b = get_next_pw(part_a)
    return part_a, part_b


if __name__ == "__main__":
    p = Puzzle(year=2015, day=11)
    print("part a: {}\npart b: {}".format(*solve(p.input_data)))
