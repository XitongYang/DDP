"""
Leap Year Checker Function

Objective:
Write a function named 'is_leap_year' to determine whether a given year is a leap year.

Function Parameter:
year (integer): The year to be checked.

Instructions:
- The function should return 'True' if the 'year' is a leap year and 'False' otherwise.
- A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.
- Use conditional statements to implement the leap year check.

Example Test Cases:
1. is_leap_year(2020) should return 'True'.
2. is_leap_year(1900) should return 'False'.
3. is_leap_year(2000) should return 'True'.
4. is_leap_year(2019) should return 'False'.
"""

def is_leap_year(year):
    # 如果年份能被400整除，则是闰年
    if year % 400 == 0:
        return True
    # 如果年份能被4整除但不能被100整除，则是闰年
    elif year % 4 == 0 and year % 100 != 0:
        return True
    # 其他情况不是闰年
    else:
        return False

# 测试用例
print(is_leap_year(2020))  # 应该返回 True
print(is_leap_year(1900))  # 应该返回 False
print(is_leap_year(2000))  # 应该返回 True
print(is_leap_year(2019))  # 应该返回 False
