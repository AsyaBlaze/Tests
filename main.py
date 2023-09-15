import pytest


def sum2(x, y):
    return x + y


def plus2(nums):
    result = []
    for num in nums:
        result.append(num + 2)
    return result


def multiply2(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result


def exponent2(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result


@pytest.fixture()
def get_prime_nums():
    prime_nums = []
    for num in range(1, 50):
        for div in range(2, num):
            if num % div == 0:
                break
            else:
                prime_nums.append(num)
    print(prime_nums)
    return prime_nums
