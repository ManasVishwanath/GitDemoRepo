def compute_highest_char(inputString):
    k = {}

    for char in inputString:
        if char in k.keys():
            k[char] = k[char] + 1
        else:
            k[char] = 1

    return sorted(k.items(), key=lambda x: x[1], reverse=True)[0][0]


def test_basic_case():
    assert compute_highest_char("aabbcccdd") == "c"


def test_with_spaces():
    assert compute_highest_char("hello world") == "l"


def test_only_one_character():
    assert compute_highest_char("aaaaa") == "a"


def test_special_chars():
    assert compute_highest_char("!!??!!") == "!"


def test_numeric_case():
    assert compute_highest_char("112233333") == "3"


def test_mixed_string():
    s = "ABCabc123!!!"
    assert compute_highest_char(s) == "!"
