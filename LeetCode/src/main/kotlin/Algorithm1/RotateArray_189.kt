package Algorithm1

class RotateArray_189 {
    fun rotate(nums: IntArray, k: Int): Unit {
        val oriNums = nums.copyOf()
        var j = k % nums.size
        for (num in oriNums)
        {
            nums[j] =  num
            j = (j + 1) % nums.size
        }
    }
}