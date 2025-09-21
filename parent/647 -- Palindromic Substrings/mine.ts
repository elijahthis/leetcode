function countSubstrings_mine(s: string): number {
	// TWO POINTER
	// let palindrome_count = s.length;
	let palindrome_count = 0;
	let left_pointer = 0;
	let right_pointer = 0;

	for (let i = 0; i < s.length; i++) {
		for (let j = 0; j < s.length / 2; j++) {
			left_pointer = i - j;
			right_pointer = i + j;

			if (
				s[left_pointer] === s[right_pointer] &&
				left_pointer >= 0 &&
				right_pointer < s.length
			) {
				palindrome_count++;
			} else break;
		}

		if (s[i] === s[i + 1]) {
			for (let j = 0; j < s.length / 2; j++) {
				left_pointer = i - j;
				right_pointer = i + j + 1;

				if (
					s[left_pointer] === s[right_pointer] &&
					left_pointer >= 0 &&
					right_pointer < s.length
				) {
					palindrome_count++;
				} else break;
			}
		}
	}

	return palindrome_count;
}
