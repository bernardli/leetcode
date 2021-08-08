
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
    vector<string> generateParenthesis(int n)
    {
        num = n;
        int leftCount = 0;
        int rightCount = 0;
        dfs(leftCount, rightCount, "");
        return result;
    }
    void dfs(int leftCount, int rightCount, string currStr)
    {
        if (currStr.size() == num * 2){
            result.emplace_back(currStr);
            return;
        }
        if (leftCount < num){
            dfs(leftCount + 1, rightCount, currStr += "(");
            currStr.pop_back();
        }
        if (rightCount < leftCount){
            dfs(leftCount, rightCount + 1, currStr += ")");
            currStr.pop_back();
        }

    }
private:
    int num;
    vector<string> result;
};

int main()
{
    Solution s;
    s.generateParenthesis(3);
    return 0;
}