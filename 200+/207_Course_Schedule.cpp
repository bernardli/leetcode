
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
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        for (auto i = prerequisites.begin(); i != prerequisites.end(); ++i)
        {
            int course = (*i)[0];
            int preCourse = (*i)[1];
            if (course == preCourse)
            {
                return false;
            }
            if (pre.count(course) == 0)
            {
                pre[course] = vector<int>();
            }
            pre[course].emplace_back(preCourse);
        }

        for (auto i = pre.begin(); i != pre.end(); ++i)
        {
            if (courseVaildMap.count(i->first) != 0 && courseVaildMap[i->first] == true){
                continue;
            }
            if (checkVaild(i->first) == false)
            {
                return false;
            }
        }
        return true;
    }

    bool checkVaild(int course)
    {
        if (pre.count(course) == 0){        // 没有前驱的课必可行
            courseVaildMap[course] = true;
            return true;
        }
        
        if (courseVaildMap.count(course) != 0 && courseVaildMap[course] == false){
            return false;
        }else if (courseVaildMap.count(course) != 0 && courseVaildMap[course] == true){
            return true;
        }else{
            courseVaildMap[course] = false;
        }

        vector<int> preCourses = pre[course];
        for (auto i = preCourses.begin(); i != preCourses.end(); ++i)
        {
            if (checkVaild(*i) == false)
            {
                return false;
            }
        }
        courseVaildMap[course] = true;
        return true;
    }

private:
    unordered_map<int, vector<int>> pre;
    unordered_map<int, bool> courseVaildMap;
};

int main()
{
    Solution s;
    vector<vector<int>> v = {{1, 0}};
    cout << s.canFinish(2, v) << endl;
    s = Solution();
    v = {{1, 0},
         {0, 1}};
    cout << s.canFinish(2, v) << endl;
    return 0;
}