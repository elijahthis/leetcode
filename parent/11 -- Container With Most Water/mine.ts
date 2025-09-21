function maxArea(height: number[]): number {
	// TWO POINTER
	let left = 0;
	let right = height.length - 1;
	let max_area = 0;

	while (left < right) {
		// Calculate the area between left and right pointers
		const width = right - left;
		const minHeight = Math.min(height[left], height[right]);
		const area = width * minHeight;
		max_area = Math.max(max_area, area);

		if (height[left] < height[right]) {
			left++;
		} else {
			right--;
		}
	}

	return max_area;
}
