from recursionsorting import recursion
from recursionsorting import sorting

def test_sum_array():
    """
    check that sum_array function works correctly
    """
    assert recursionsorting.sum_array([2]) == 2, 'incorrect'
    assert recursionsorting.sum_array([10, 1, 5, 7, 8, 12, 2]) == 45, 'incorrect'
    assert recursionsorting.sum_array([4, 8, 10]) == 22, 'incorrect'

def test_fibonacci():
    """
    check that fibonacci function works correctly
    """
    assert recursionsorting.fibonacci(1) == 1, 'incorrect'
    assert recursionsorting.fibonacci(7) == 13, 'incorrect'
    assert recursionsorting.fibonacci(51) == 20365011074, 'incorrect'

def test_factorial():
    """
    check that factorial function works correctly
    """
    assert recursionsorting.factorial(1) == 1, 'incorrect'
    assert recursionsorting.factorial(7) == 5040, 'incorrect'
    assert recursionsorting.factorial(10) == 3628800, 'incorrect'

def test_reverse():
    """
    check that reverse function works correctly
    """
    assert recursionsorting.reverse('word') == 'drow', 'incorrect'
    assert recursionsorting.reverse('') == '', 'incorrect'
    assert recursionsorting.reverse('fhiewiuryeui') == 'iueyruiweihf', 'incorrect'

def test_bubble_sort():
    """
    check that bubble_sort function works correctly
    """
    assert recursionsorting.bubble_sort([14, 21, 1]) == [1, 14, 21], 'incorrect'
    assert recursionsorting.bubble_sort([5, 89, 7, 2, 65, 17, 1]) == [1, 2, 5, 7, 17, 65, 89], 'incorrect'
    assert recursionsorting.bubble_sort([3]) == [3], 'incorrect'

def test_merge_sort():
    """
    check that merge_sort function works correctly
    """
    assert recursionsorting.merge_sort([14, 21, 1]) == [1, 14, 21], 'incorrect'
    assert recursionsorting.merge_sort([5, 89, 7, 2, 65, 17, 1]) == [1, 2, 5, 7, 17, 65, 89], 'incorrect'
    assert recursionsorting.merge_sort([3]) == [3], 'incorrect'

def test_quick_sort():
    """
    check that quick_sort function works correctly
    """
    assert recursionsorting.quick_sort([14, 21, 1]) == [1, 14, 21], 'incorrect'
    assert recursionsorting.quick_sort([5, 89, 7, 2, 65, 17, 1]) == [1, 2, 5, 7, 17, 65, 89], 'incorrect'
    assert recursionsorting.quick_sort([3]) == [3], 'incorrect'
