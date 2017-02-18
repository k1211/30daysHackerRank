# Task
# The height of a binary search tree is the number of edges between the tree's root and its furthest leaf.
# You are given a pointer, root , pointing to the root of a binary search tree.
# Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def getHeight(self,root):
        if root == None:
            return -1
        else:
            return max(self.getHeight(root.left) , self.getHeight(root.right)) + 1

T = int(raw_input())
myTree = Solution()
root = None
for i in range(T):
    data = int(raw_input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print height