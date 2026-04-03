class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Average time: O(n)
        # Worst time: O(n^2)
        # Space: O(1) (in-place)

        target = len(nums) - k

        def quick_select(left, right):
            if left == right:
                return nums[left]

            pivot = nums[left]
            i, j = left - 1, right + 1

            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1

                j -= 1
                while nums[j] > pivot:
                    j -= 1

                if i >= j:
                    break

                nums[i], nums[j] = nums[j], nums[i]

            # Only recurse into ONE side
            if target <= j:
                return quick_select(left, j)
            else:
                return quick_select(j + 1, right)

        return quick_select(0, len(nums) - 1)