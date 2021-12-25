package Algorithm1

class BinarySearch_704 {
    fun search(nums: IntArray, target: Int): Int
    // nums : Sorted in ascending order
    {
        val len : Int = nums.size
        var min : Int = 0
        var max : Int = len - 1
        var mid : Int = (min + max)/2

        while (true)
        {
            if (max < min)
                break
            if (nums[mid] == target)
                return mid
            else if (nums[mid] > target) {
                // search smaller numbers
                max = mid - 1
            } else
            {
                // search bigger numbers
                min = mid + 1
            }
            mid = (min + max) / 2
        }

        // case : target not found
        return -1
    }
}