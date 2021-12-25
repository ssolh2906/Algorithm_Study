package Algorithm1

import kotlin.math.abs

class SquareOfaSortedArray_977 {
    fun sortedSquares(nums: IntArray): IntArray {
        val size = nums.size
        val result = IntArray(size)
        var front = 0
        var rear = size - 1
        var ptr = size - 1
        var maxneg : Int
        var maxpos : Int


        while (ptr > -1)
        {
            maxneg = -nums[front]
            maxpos = nums[rear]
            if (maxneg < maxpos)
            {
                result[ptr] = maxpos * maxpos
                rear -= 1
            } else {
                result[ptr] = maxneg * maxneg
                front += 1
            }
            ptr -= 1
        }
        return result
    }
}