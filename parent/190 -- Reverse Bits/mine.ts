function reverseBits(n: number): number {
    let bin_form = n.toString(2)
    let stringifiedbits = "0".repeat(32 - bin_form.length) + bin_form
    let reversed_bits = stringifiedbits.split('').reverse().join('')

    return parseInt(reversed_bits, 2)
	
};