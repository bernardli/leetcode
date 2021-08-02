
#include <iostream>
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<memory>
#include<unordered_map>
#include<queue>

using namespace std;


struct node
{
    int num;
    string str;
    node(int x, string y) :num(x), str(y) {}
};

struct cmp
{
    bool operator()(node a, node b)
    {
        if (a.num == b.num) {
            if (a.str < b.str) { return true; }
            else{ return false; }
            // if (a.str < b.str) { return true; }
            // else{ return false; }
        }
        else if (a.num > b.num) {
            return true;
        }
        else
        {
            return false;
        }
        //return a.num > b.num || (a.num == b.num && a.str < b.str); 
    }
};


class Solution {
public:
    /**
     * return topK string
     * @param strings string字符串vector strings
     * @param k int整型 the k
     * @return string字符串vector<vector<>>
     */
    vector<vector<string> > topKstrings(vector<string>& strings, int k) {
        unordered_map<string, int> hashtable;
        for (auto str : strings) {
            auto it = hashtable.find(str);
            if (it == hashtable.end()) {
                hashtable[str] = 0;
            }
            hashtable[str] += 1;
        }
        /*
        for (auto iter = hashtable.begin(); iter != hashtable.end(); iter++) {
            cout << iter->second << endl;
        }
        */
        priority_queue<node, vector<node>, cmp> heap;
        for (auto it = hashtable.begin(); it != hashtable.end(); it++) {
           if (heap.size() != k){
               heap.push(node(it->second, it->first));
               continue;
           }
           
           if (heap.top().num < it->second || (heap.top().num == it->second && heap.top().str > it->first)){
               heap.pop();
               heap.push(node(it->second, it->first));
           }
        }

        vector<vector<string>> result;
        while (heap.empty() != true){
            node temp = heap.top();
            heap.pop();
            result.emplace_back(vector<string>({ temp.str, to_string(temp.num) }));
        }
        reverse(result.begin(), result.end());
        return result;
    }
};

int main()
{
    Solution foo;
    vector<string> strings = { "a", "b", "c", "b" };

    vector<vector<string>> result = foo.topKstrings(strings, 2);
    for (auto it = result.begin(); it != result.end(); it++) {
        cout << (*it)[0]<<":"<<(*it)[1]<< endl;
    }

    strings = {"123","123","231","32"};
    result = foo.topKstrings(strings, 2);
    for (auto it = result.begin(); it != result.end(); it++) {
        cout << (*it)[0]<<":"<<(*it)[1]<< endl;
    }
    
    return 0;
}