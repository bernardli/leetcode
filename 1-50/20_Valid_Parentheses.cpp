
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
    bool isValid(string s)
    {
        stack<char> record;
        unordered_map<char, char> map;
        map['('] = ')';
        map['{'] = '}';
        map['['] = ']';
        for (char c : s)
        {
            if (map.find(c) != map.end()){
                record.push(c);
            }else{
                if (record.size() == 0) return false;
                else{
                    char topChar = record.top();
                    if (map[topChar] != c) return false;
                    record.pop();
                }
            }
        }
        if(record.size() != 0) return false;
        return true;
    }
};

int main()
{
    Solution s;
    cout<<s.isValid("()")<<endl;
    cout<<s.isValid("()[]{}")<<endl;
    cout<<s.isValid("(]")<<endl;
    return 0;
}