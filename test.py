import pytest

from main import sum2
from main import multiply2
from main import exponent2
from main import plus2
from main import get_prime_nums


def test_sum2():
    assert 2 == sum2(15, 8)


@pytest.mark.parametrize('a, b, rsl, index',
                         [
                             (2, 2, 4, 1),
                             (3, 2, 9, 2),
                             (4, 3, 64, 3),
                             (3, 8, 6561, 4)
                         ])
def test_sqrt(a, b, rsl, index):
    if index <2:
        print("\nНачинаем тестирование")
    elif index == 2:
        print("\nТестирование пройдено на половину")

    assert a ** b == rsl
    if index == 4:
        print("\nТестирование закончено")


@pytest.mark.parametrize('g, k, result',
                         [
                             (2, 2, 4),
                             (3, 2, 6),
                             (4, 3, 12),
                             (3, 8, 24)
                         ])
def test_multiply(g, k, result):
    assert g * k == result

# def test_plus2(get_prime_nums):
#     prime_nums = get_prime_nums
#     assert plus2(prime_nums) == [3, 4, 5, 7, 9, 13]
#
#
# def test_multiply2(get_prime_nums):
#     prime_nums = get_prime_nums
#     assert multiply2(prime_nums) == [2, 4, 6, 10, 14]
#
#
# def test_exponent2(get_prime_nums):
#     prime_nums = get_prime_nums
#     assert exponent2(prime_nums) == [1, 4, 9, 25, 49]
