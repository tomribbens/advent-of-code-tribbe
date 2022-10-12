from aoc_tribbe.aoc2015.d11 import is_valid_pw, get_next_pw


def test_requirements():
    assert not is_valid_pw("hijklmmn")
    assert not is_valid_pw("abbceffg")
    assert not is_valid_pw("abbcegjk")
    assert is_valid_pw("abbcdaaa")

    assert get_next_pw("abcdefgh") == "abcdffaa"
    assert get_next_pw("ghijklmn") == "ghjaabcc"

