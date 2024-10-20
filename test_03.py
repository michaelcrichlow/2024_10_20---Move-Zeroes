def moveZeroes(nums: list[int]) -> int:
    local_array = []
    for val in nums:
        if val != 0:
            local_array.append(val)

    for i in range(len(nums)):
        nums[i] = 0

    for i in range(len(local_array)):
        nums[i] = local_array[i]

    return 5


def main() -> None:
    print(moveZeroes([0, 0, 1]))


if __name__ == '__main__':
    main()

 # [0,1,0,3,12] -> [1,3,12,0,0]
 # [0] -> [0]
