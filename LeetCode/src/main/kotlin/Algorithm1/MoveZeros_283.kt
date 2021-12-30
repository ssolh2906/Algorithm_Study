package Algorithm1

class MoveZeros_283 {
    fun moveZeroes(nums: IntArray): Unit {
        var ptr0 = 0    // point index of the 1st 0
        var ptrNum = 0

        // ptrNum iteration
        while (true) {
            while (ptr0 < nums.size &&nums[ptr0] != 0) {
                ptr0 ++
            }
            ptrNum = ptr0
            while ( ptrNum < nums.size && nums[ptrNum] == 0 ) {
                ptrNum ++
            }

            if (ptrNum >= nums.size || ptr0 >= nums.size || ptr0 > ptrNum) {
                break
            }

            nums[ptr0] = nums[ptrNum]
            nums[ptrNum] = 0

        }
    }
}