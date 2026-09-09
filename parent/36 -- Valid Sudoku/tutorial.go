package main

func isValidSudoku(board [][]byte) bool {
	rows := map[int]map[int]bool{}
	cols := map[int]map[int]bool{}
	squares := map[int]map[int]bool{}

	// defaults
	for i := range 9 {
		rows[i] = map[int]bool{}
		cols[i] = map[int]bool{}
		squares[i] = map[int]bool{}
	}

	for r := range 9 {
		for c := range 9 {
			if board[r][c] != '.' {
				val := int(board[r][c] - '0')
				sq_idx := (3 * (r / 3)) + (c / 3)

				if _, exists := rows[r][val]; exists {
					return false
				}
				if _, exists := cols[c][val]; exists {
					return false
				}
				if _, exists := squares[sq_idx][val]; exists {
					return false
				}

				rows[r][val] = true
				cols[c][val] = true
				squares[sq_idx][val] = true
			}
		}
	}
	return true
}
