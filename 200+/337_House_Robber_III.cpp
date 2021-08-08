
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
#include <limits>

using namespace std;

template <typename T>
void printVector(const vector<T> &vec)
{
    for (int i = 0; i < vec.size(); ++i)
    {
        cout << vec[i] << " ";
    }
}


//   Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    int rob(TreeNode *root)
    {
        pair<int, int> result = dfs(root);
        return max(result.first, result.second);
    }
    pair<int, int> dfs(TreeNode *root)
    {
        if (root == nullptr)
        {
            return pair<int, int>(0, 0);
        }
        pair<int, int> leftMax = dfs(root->left);
        pair<int, int> rightMax = dfs(root->right);
        int usedThisNode = root->val + leftMax.second + rightMax.second;
        int notUsedThisNode = max({leftMax.first + rightMax.second, leftMax.second + rightMax.first, leftMax.first + rightMax.first, leftMax.second + rightMax.second});
        return pair<int, int>(usedThisNode, notUsedThisNode);
    }
};
int main()
{

    return 0;
}