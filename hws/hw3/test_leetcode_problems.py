
from leetcode_problems import merge_alternately, gcd_of_strings, \
        students_with_books, two_sum, move_zeroes

sample_word_merge = [
        ("abc", "def", "adbecf"),
        ("hello", "world", "hweolrllod"),
        ("", "abc", "abc"),
        ("abc", "", "abc"),
        ("a", "xyz", "axyz"),
        ("abcd", "123", "a1b2c3d")]

sample_gcd = [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
        ("ABCDEF", "ABCDEFABCDEF", "ABCDEF"),
        ("ABC", "DEF", ""),
        ("", "", ""),
        ("ABC", "ABC", "ABC")]

sample_books = [
        ([2, 3, 1, 4], 2, [True, True, False, True]),
        ([5, 5, 5, 5], 0, [True, True, True, True]),
        ([1, 2, 3, 4], 5, [True, True, True, True]),
        ([], 10, [])]

sample_sum = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([], 0, None),
        ([1, 2, 3, 4, 5], 10, None)]


def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected

def test_merge_alternately():
    for word1, word2, expected in sample_word_merge:
        assert merge_alternately(word1, word2) == expected

def test_gcd_of_strings():
    for word1, word2, expected in sample_gcd:
        assert gcd_of_strings(word1, word2) == expected

def test_students_with_books():
    for books, extra, expected in sample_books:
        assert students_with_books(books, extra) == expected

def test_two_sum():
    for nums, target, expected in sample_sum:
        assert two_sum(nums, target) == expected

def test_move_zeroes():
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0, 0, 0, 0, 0]
    move_zeroes(nums)
    assert nums == [0, 0, 0, 0, 0]

    nums = [1, 2, 3, 4, 5]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 4, 5]

    nums = [0, 0, 0, 1, 2, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]

    nums = [1, 0, 2, 0, 3, 0]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]

    nums = [1, 2, 3, 0, 0, 0]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]

