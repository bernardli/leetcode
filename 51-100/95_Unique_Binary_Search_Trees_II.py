from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.recursion(0, n - 1)

    def recursion(self, left, right):
        rootList = []
        for i in range(left, right + 1):
            currNum = i + 1
            leftNodeList = self.recursion(left, i - 1)
            rightNodeList = self.recursion(i + 1, right)
            

            for i in range(max(len(leftNodeList), 1)):
                if len(leftNodeList) == 0:
                    leftNode = None
                else:
                    leftNode = leftNodeList[i]
                for j in range(max(len(rightNodeList), 1)):
                    if len(rightNodeList) == 0:
                        rightNode = None
                    else:
                        rightNode = rightNodeList[j]
                    root = TreeNode(currNum, leftNode, rightNode)
                    rootList.append(root)


            # if len(leftNodeList) == 0:
            #     for rightNode in rightNodeList:
            #         root = TreeNode(currNum, None, rightNode)
            #         rootList.append(root)
            # elif len(rightNodeList) == 0:
            #     for leftNode in leftNodeList:
            #         root = TreeNode(currNum, leftNode, None)
            #         rootList.append(root)
            # else:
            #     for leftNode in leftNodeList:
            #         for rightNode in rightNodeList:
            #             root = TreeNode(currNum, leftNode, rightNode)
            #             rootList.append(root)

        return rootList

    def run(self):
        result = self.generateTrees(3)
        print('debug')

foo = Solution()
foo.run()            