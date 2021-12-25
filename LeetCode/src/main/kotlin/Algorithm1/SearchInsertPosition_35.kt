package Algorithm1

class SearchInsertPosition_35 {
    fun searchInsert(nums: IntArray, target: Int): Int {
        var min  = 0
        var max  = nums.size - 1
        var mid : Int
        var midnum : Int

        if (nums[min] >= target) return min
        if (nums[max] == target) return max
        if (nums[max] < target) return max + 1

        while (min + 1 < max) {
            mid = min + (max - min) / 2
            midnum = nums[mid]
            if (midnum == target) return mid
            else if (midnum < target) {
                min = mid
            } else {
                max = mid
            }
        }
        return min + 1

    }
}