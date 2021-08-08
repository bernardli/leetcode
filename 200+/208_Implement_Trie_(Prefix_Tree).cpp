
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

// Definition for a binary tree node.
struct MyTreeNode
{
    char val;
    bool isEnd;
    unordered_map<char, MyTreeNode *> sons;
    MyTreeNode() : val(' '), sons(unordered_map<char, MyTreeNode *>()), isEnd(false) {}
    MyTreeNode(char x) : val(x), sons(unordered_map<char, MyTreeNode *>()), isEnd(false) {}
};

class Trie
{
public:
    /** Initialize your data structure here. */
    Trie() : head(new MyTreeNode())
    {
    }

    /** Inserts a word into the trie. */
    void insert(string word)
    {
        searchAndInsert(head->sons, word, 0);
    }

    /** Returns if the word is in the trie. */
    bool search(string word)
    {
        return searchWord(head->sons, word, 0);
    }

    bool searchWord(const unordered_map<char, MyTreeNode *> &sons, string &word, int wordIdx)
    {
        if (sons.count(word[wordIdx]) != 0)
        {
            auto thisNode = sons.find(word[wordIdx])->second;
            if (wordIdx == word.size() - 1 && thisNode->isEnd == true)
            {
                return true;
            }
            else
            {
                return searchWord(thisNode->sons, word, wordIdx + 1);
            }
        }
        else
        {
            return false;
        }
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix)
    {
        return searchPrefix(head->sons, prefix, 0);
    }

    bool searchPrefix(const unordered_map<char, MyTreeNode *> &sons, string &prefix, int wordIdx)
    {
        if (wordIdx == prefix.size())
        {
            return true;
        }
        if (sons.count(prefix[wordIdx]) != 0)
        {
            auto nextSons = sons.find(prefix[wordIdx])->second->sons;
            return searchPrefix(nextSons, prefix, wordIdx + 1);
        }
        else
        {
            return false;
        }
    }

    void searchAndInsert(unordered_map<char, MyTreeNode *> &sons, string &word, int wordIdx)
    {
        if (wordIdx == word.size())
        {
            return;
        }
        if (sons.count(word[wordIdx]) == 0)
        {
            sons[word[wordIdx]] = new MyTreeNode(word[wordIdx]);
        }
        searchAndInsert(sons[word[wordIdx]]->sons, word, wordIdx + 1);
        if (wordIdx == word.size() - 1){
            sons[word[wordIdx]]->isEnd = true;
        }
    }

private:
    MyTreeNode *head;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */


int main()
{

    return 0;
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */