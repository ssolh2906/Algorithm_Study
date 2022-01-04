package Top_interview_questions

class Two_Some_1 {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val answer = IntArray(2)
        var sum: Int
        for (i in nums.indices) {
            for (j in i + 1 until nums.size) {
                sum = nums[i] + nums[j]
                if (sum == target) {
                    answer[0] = i
                    answer[1] = j
                    return answer
                }
            }


        }
        return answer
    }
}