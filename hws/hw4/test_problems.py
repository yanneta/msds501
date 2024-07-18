from problems import reverse_string, find_max_average, find_numbers, \
        contains_duplicate, find_winners_and_losers

def test_reverse_string():
    # Test case 1
    s1 = ['h', 'e', 'l', 'l', 'o']
    reverse_string(s1)
    assert s1 == ['o', 'l', 'l', 'e', 'h']

    # Test case 2
    s2 = ['a', 'b', 'c', 'd']
    reverse_string(s2)
    assert s2 == ['d', 'c', 'b', 'a']

    # Test case 3
    s3 = ['a']
    reverse_string(s3)
    assert s3 == ['a']

    # Test case 4
    s4 = []
    reverse_string(s4)
    assert s4 == []

    # Test case 5
    s5 = ['p', 'y', 't', 'h', 'o', 'n']
    reverse_string(s5)
    assert s5 == ['n', 'o', 'h', 't', 'y', 'p']

    # Test case 6 (with numbers as strings)
    s6 = ['1', '2', '3', '4', '5']
    reverse_string(s6)
    assert s6 == ['5', '4', '3', '2', '1']


def test_find_max_average():
    # Test case 1
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    assert find_max_average(nums1, k1) == 12.75
    
    # Test case 2
    nums2 = [5, 5, 5, 5, 5]
    k2 = 1
    assert find_max_average(nums2, k2) == 5.0
    
    # Test case 3
    nums3 = [0, 4, 0, 3, 2]
    k3 = 1
    assert find_max_average(nums3, k3) == 4.0
    
    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 2
    assert find_max_average(nums4, k4) == 4.5
    
    # Test case 5
    nums5 = [-1, -2, -3, -4, -5]
    k5 = 3
    assert find_max_average(nums5, k5) == -2.0


def test_find_numbers():
    # Test case 1
    nums1 = [1, 2, 3, 6, 7, 8, 10]
    assert find_numbers(nums1) == [10]

    # Test case 2
    nums2 = [1, 3, 5, 7]
    assert find_numbers(nums2) == [1, 3, 5, 7]

    # Test case 3
    nums3 = [2, 4, 6, 8, 10]
    assert find_numbers(nums3) == [2, 4, 6, 8, 10]

    # Test case 4
    nums4 = [1, 1, 2, 3, 5, 5, 6, 7]
    assert find_numbers(nums4) == []


def test_contains_duplicate():
    # Test case 1: Example with duplicates
    nums = [1, 2, 3, 1]
    assert contains_duplicate(nums) == True

    # Test case 2: Example with all unique elements
    nums = [1, 2, 3, 4]
    assert contains_duplicate(nums) == False

    # Test case 3: Empty array
    nums = []
    assert contains_duplicate(nums) == False

    # Test case 4: Single element array
    nums = [1]
    assert contains_duplicate(nums) == False


def test_find_winners_and_losers():
    # Test case 1:
    matches = [
        [1, 3], [2, 3], [3, 6], [5, 6], [5, 7], 
        [4, 5], [4, 8], [4, 9], [10, 4]
    ]
    expected_output = [[1, 2, 10], [4, 5, 7, 8, 9]]
    assert find_winners_and_losers(matches) == expected_output

    # Test case 2: No players
    matches = []
    expected_output = [[], []]
    assert find_winners_and_losers(matches) == expected_output

    # Test case 3:
    matches = [[1, 2], [3, 4]]
    expected_output = [[1, 3], [2, 4]]
    assert find_winners_and_losers(matches) == expected_output

    # Test case 4: 
    matches = [[1, 2], [2, 3], [3, 4]]
    expected_output = [[1], [2, 3, 4]]
    assert find_winners_and_losers(matches) == expected_output

    # Test case 5: 
    matches = [[1, 2], [2, 3], [3, 1], [4, 5], [6, 7]]
    expected_output = [[4, 6], [1, 2, 3, 5, 7]]
    assert find_winners_and_losers(matches) == expected_output

