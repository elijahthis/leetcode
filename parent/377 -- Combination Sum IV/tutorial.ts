function combinationSum4(nums: number[], target: number): number {
    // DYNAMIC PROGRAMMING
	let dp = { 0: 1 };

	for (let total = 1; total < target + 1; total++) {
		dp[total] = 0;
		for (let j = 0; j < nums.length; j++) {
			dp[total] += dp?.[total - nums[j]] ?? 0;
		}
	}
	return dp[target];
}
