
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
    int rob(vector<int> &nums)
    {
        if (nums.size() == 1)
            return nums[0];
        if (nums.size() == 2)
            return max(nums[0], nums[1]);
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        for (int i = 2; i < nums.size(); ++i)
        {
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]);
        }
        return dp[nums.size() - 1];
    }
};

int main()
{
    Solution s;
    vector<int> v = {1, 2, 3, 1};
    cout << s.rob(v) << endl;
    v = {2, 7, 9, 3, 1};
    cout << s.rob(v) << endl;
    return 0;
}