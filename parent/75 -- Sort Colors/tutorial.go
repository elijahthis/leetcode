package main

func sortColors(nums []int) {
	//  We used the Dutch National Flag algorithm (invented by Dijkstra)
	// Time: O(n)
	// Space: O(1)
	lo, mid, hi := 0, 0, len(nums)-1

	for mid <= hi {
		switch nums[mid] {
		case 0:
			nums[lo], nums[mid] = nums[mid], nums[lo]
			lo++
			mid++
		case 1:
			mid++
		default:
			nums[mid], nums[hi] = nums[hi], nums[mid]
			hi--
		}
	}
}
