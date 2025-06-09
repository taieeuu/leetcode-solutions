/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let curr = head
    let prev = null

    while(curr != null){
        let next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    }
    return prev
};

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
function printLinkedList(head) {
    let cur = head;
    let res = [];
    while (cur !== null) {
        res.push(cur.val);
        cur = cur.next;
    }
    console.log(res.join(" -> ") + " -> null");
}

let head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
console.log("原始鏈表:");
printLinkedList(head);

let reversedHead = reverseList(head);
console.log("反轉後鏈表:");
printLinkedList(reversedHead);