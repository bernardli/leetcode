
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

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        Kth = nums.size() - k;
        return patition(nums, 0, nums.size() - 1);
    }
    int patition(vector<int> &nums, int left, int right)
    {
        int selectNum = nums[left];
        int p1 = left;
        int p2 = right;
        while (p1 < p2)
        {
            while (nums[p2] > selectNum && p1 < p2)
            {
                p2 = p2 - 1;
            }
            nums[p1] = nums[p2];
            while (nums[p1] <= selectNum && p1 < p2)
            {
                p1 = p1 + 1;
            }
            nums[p2] = nums[p1];
        }
        nums[p1] = selectNum;
        if (p1 == Kth)
        {
            return nums[p1];
        }
        else if (p1 > Kth)
        {
            return patition(nums, left, p1 - 1);
        }
        else    // p1 < Kth
        {
            return patition(nums, p1 + 1, right);
        }
    }

private:
    int Kth;
};

int main()
{
    Solution s;
    vector<int> v = {3, 2, 1, 5, 6, 4};
    cout << s.findKthLargest(v, 2) << endl;
    v = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    cout << s.findKthLargest(v, 4) << endl;
    return 0;
}