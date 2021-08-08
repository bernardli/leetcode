
#include <iostream>
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <memory>
#include <unordered_map>
#include <queue>
#include <typeinfo>
#include <list>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode *head = new ListNode();
        ListNode *P1 = l1;
        ListNode *P2 = l2;
        ListNode *P = head;

        while (P1 != nullptr && P2 != nullptr)
        {
            if (P1->val < P2->val)
            {
                P->next = P1;
                P1 = P1->next;
                P = P->next;
            }else{
                P->next = P2;
                P2 = P2->next;
                P = P->next;
            }
        }
        while (P1 != nullptr)
        {
            P->next = P1;
            P1 = P1->next;
            P = P->next;
        }
        while (P2 != nullptr)
        {
            P->next = P2;
            P2 = P2->next;
            P = P->next;
        }
        
        return head->next;
    }
};

int main()
{
    Solution s;

    return 0;
}