var productExceptSelf = function(nums) {
    const result = []
    const fromLeft = new Array(nums.length)
    const fromRight = new Array(nums.length)

    fromLeft[0] = 1;
    for (let i = 1; i < nums.length; i++) {
        fromLeft[i] = fromLeft[i - 1] * nums[i - 1]
    }

    fromRight[nums.length - 1] = 1
    for (let i = nums.length - 2; i >= 0; i--) {
        fromRight[i] = fromRight[i + 1] * nums[i + 1]
    }

    for (let i = 0; i < nums.length; i++) {
        result.push(fromLeft[i] * fromRight[i])
    }
    return result
};