class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode p0 = null;
        ListNode p1 = head;
        ListNode p2 = head;
        int i = 1;
        while(i< n){
            p2=p2.next;
            i += 1;
        }
        // if(p1 == p2 ){return null;} //condition for 1 length
        while( p2.next != null){
            p2 = p2.next;
            p0 = p1;
            p1 = p1.next;
        }            
        
        if(p0 == null && p1 == p2){ //condition n==1 and length ==1
            return null;
        }
        if(p0 == null){ // p1 is head and p2 is tail. and p1 should be removed
            return p1.next;
        }
        if(p1 == p2) { //condition for n ==1
            p0.next = null;
            return head;
        }
        p0.next = p1.next;
        p1 = null;
        return head;
    }
}