function convert(s: string, numRows: number): string {
	// TWO POINTER
	let result = "";
	let resultMap = new Map();
	let currRow = 0;
	let op: "add" | "sub" = "add";

	if (s.length < 3) return s;

	for (let i = 0; i < s.length; i++) {
		resultMap.set(currRow, (resultMap.get(currRow) ?? "") + s[i]);

		if (op === "add") currRow = currRow + 1;
		else currRow = currRow - 1;

		if (currRow === numRows - 1) op = "sub";
		if (currRow === 0) op = "add";
	}

	resultMap.forEach((value) => (result += value));

	return result;
}
