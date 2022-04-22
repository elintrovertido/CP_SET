from collections import deque

class node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class binarytree:
    def __init__(self):
        self.root = None
    
    # preorder root-> left -> right
    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # inorder left -> root -> right
    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        print(root.data,end= " ")
        self.inorder(root.right)

    # postorder left -> right -> root
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")

    # number of nodes present in binary tree
    def numberofnodes(self,root):
        if root is None:
            return 0
        return 1 + self.numberofnodes(root.left) + self.numberofnodes(root.right)
    # number of leaf nodes in tree
    def numof_leafnodes(self,root):
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return self.numof_leafnodes(root.left) + self.numof_leafnodes(root.right)
    # number of non-leaf nodes
    def numof_nonleafnodes(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return 1 + self.numof_nonleafnodes(root.left) + self.numof_nonleafnodes(root.right)

    # number of full nodes in tree
    def numof_fullnodes(self,root):
        if root is None:
            return 0
        if root.left is not None and root.right is not None:
            return 1
        return self.numof_fullnodes(root.left) + self.numof_fullnodes(root.right)

    # level order traversal
    def levelorder(self,root):
        res = []
        if root is None:
            return res
        queue = deque([])
        queue.append(self.root)
        while len(queue)!=0:
            level_size = len(queue)
            currentlevel = []
            for i in range(level_size):
                current = queue.popleft()
                currentlevel.append(current.data)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            res.append(currentlevel)
        return res

    def zigzatraversal(self,root):
        res = self.levelorder(root)
        sol = []
        count = 1
        for i in res:
            if count & 1 == 0:
                sol.append(list(reversed(i)))
                count += 1
            else:
                sol.append(i)
                count += 1 
        return sol
    
    # level order successor
    def levelordersucccessor(self,root,key):
        if root is None:
            return res
        queue = deque([])
        queue.append(self.root)
        while len(queue)!=0:
            current = queue.popleft()
            
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

            if current.data ==  key:
                break
        return queue.popleft().data         
    
    # minimum dept of binary tree
    def minimumdepth(self,root):
        if root is None:
            return 0
        mindepth = 0
        queue = deque([])
        queue.append(self.root)
        while len(queue)!=0:
            mindepth += 1
            current = queue.popleft()

            if current.left is None and current.right is None:
                return mindepth
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return mindepth

    # right view of tree
    def rightview(self,root):
        res = []
        if root is None:
            return res
        queue = deque([])
        queue.append(self.root)
        while len(queue)!=0:
            levelsize = len(queue)
            for i in range(levelsize):
                current = queue.popleft()

                if (i==levelsize-1):
                    res.append(current.data)
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
        return res
            


# driver code
tree = binarytree()
tree.root = node(1)
tree.root.left = node(2)
tree.root.right = node(3)
tree.root.right.right = node(4)

# preorder traversal
print("preorder : ",end= " " )
tree.preorder(tree.root)
print()

# inorder traversal
print("inorder : ",end= " " )
tree.inorder(tree.root)
print()

# postorder traversal
print("postorder : ",end= " " )
tree.postorder(tree.root)
print()

# number of nodes in binary tree
print("number of nodes in tree: ", end= " ")
res = tree.numberofnodes(tree.root)
print(res)

# number of leaf nodes in tree
print("number of leaf nodes: ",end=" ")
print(tree.numof_leafnodes(tree.root))

# number of non - leaf nodes in tree
print("number of non - leaf nodes: ",end=" ")
print(tree.numof_nonleafnodes(tree.root))

# number of full nodes in tree
print("number of full nodes: ",end=" ")
print(tree.numof_fullnodes(tree.root))

# level order traversal
print("level order : ")
print(tree.levelorder(tree.root))

# zigzag order traversal
print("zigzag traversal : ")
print(tree.zigzatraversal(tree.root))

# successor of node level order
print("successor of node level order")
print(tree.levelordersucccessor(tree.root,2))

# minimum depth of tree
print("minimum depth of tree")
print(tree.minimumdepth(tree.root))

# right view
print("right view : ",tree.rightview(tree.root))