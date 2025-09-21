class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

function swapPairs(head: ListNode | null): ListNode | null {
	// ITERATIVE
	let ind = 0;
	let dummy = new ListNode(0, head);
	let prev = dummy;
	let curr = head;

	while (curr && curr.next) {
		// save pointers
		let nxtPair = curr.next.next;
		let second = curr.next;

		// reverse this pair
		second.next = curr;
		curr.next = nxtPair;
		prev.next = second;

		// update pairs
		prev = curr;
		curr = nxtPair;
	}
	return dummy.next;
}
