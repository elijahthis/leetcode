function mincostTickets(days: number[], costs: number[]): number {
    // DYNAMIC PROGRAMMING
	let dayPasses = [1, 7, 30];
	const dp: number[] = new Array(days.length).fill(-1); // Initialize dp array

	function dfs(i: number): number {
		// Base case for recursive function
		if (i >= days.length) return 0; // If all days are covered
		if (dp[i] !== -1) return dp[i]; // Return already computed result

		// Set to Infinity because we're looking for minimum
		dp[i] = Number.MAX_VALUE;

		for (let j = 0; j < costs.length; j++) {
			// Find the first day that is outside the current pass range
			let nextDay = i;
			while (nextDay < days.length && days[nextDay] < days[i] + dayPasses[j]) {
				nextDay++;
			}
			// Calculate the cost of the current pass and add the result of the next days
			dp[i] = Math.min(dp[i], costs[j] + dfs(nextDay));
		}
		return dp[i];
	}

	return dfs(0);
}
