/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == nullptr || head->next == nullptr) return head;

        ios::sync_with_stdio(false);
        cin.tie(0);

        ListNode* temp = head;
        ListNode* last = nullptr;

        // Count the length of the linked list
        int lengthOfList = 0;
        while(temp->next != nullptr) {
            lengthOfList++;
            temp = temp->next;
            if(temp->next == nullptr)
                last = temp;
        }
        lengthOfList++;
        temp = temp->next;

        // find the optimal number of rotations 
        int numberOfRotations = k % lengthOfList;

        if(numberOfRotations == 0) return head;

        // the location where we will cur the list to make its next point to nulptr
        int spliceLocation = lengthOfList - numberOfRotations;

        // re-set the temp list pointer to head to locate the splice address
        temp = head;
        for(int i = 1; i < spliceLocation; i++)
            temp = temp->next;

        ListNode* subList = temp->next;
        temp->next = nullptr; // point the last node to nullptr;

        last->next = head;
        head = subList;
        return head;


    }
};
