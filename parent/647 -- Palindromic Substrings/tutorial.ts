function countSubstrings(s: string): number {
	// TWO POINTER
	// let palindrome_count = s.length;
	let palindrome_count = 0;
	let left_pointer: number;
	let right_pointer: number;

	for (let i = 0; i < s.length; i++) {
		left_pointer = i;
		right_pointer = i;

		while (
			left_pointer >= 0 &&
			right_pointer < s.length &&
			s[left_pointer] === s[right_pointer]
		) {
			palindrome_count++;
			left_pointer--;
			right_pointer++;
		}

		left_pointer = i;
		right_pointer = i + 1;

		while (
			left_pointer >= 0 &&
			right_pointer < s.length &&
			s[left_pointer] === s[right_pointer]
		) {
			palindrome_count++;
			left_pointer--;
			right_pointer++;
		}
	}

	return palindrome_count;
}
