class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        // Get length
        ListNode* tmp = head;
        int length = 0;
        while(tmp){
            tmp = tmp->next;
            length += 1;
        }

        length = std::floor(length/2);
        tmp = head;

        for(int i = 0; i < length; ++i)
            tmp = tmp->next;

        return tmp;
    }
};
