def find_duplicate(nums):
    if (
        not isinstance(nums, list)
        or not all(isinstance(num, int) and num > 0 for num in nums)
    ):
        return False

    seen_numbers = set()

    for num in nums:
        if num in seen_numbers:
            return num
        seen_numbers.add(num)

    return False
