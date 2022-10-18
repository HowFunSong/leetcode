
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        tempNode = TreeNode(data)

        if (self.root == None):
            self.root = tempNode
            return
        else:
            current = self.root
            parent = None

        while True :
            if(data < current.val):
                parent = current
                current = current.left
                if (current == None):
                    parent.left = tempNode
                    current = tempNode
                    return 
            else:
                parent = current
                current = current.right
                if (current == None):
                    parent.right = tempNode
                    current = tempNode
                    return


def searchBST(root: TreeNode, val: int) :
    global target 
    target = TreeNode()

    def preorder1(root:TreeNode,val,find:bool):
        
        if find == True:
            return

        if root==None:
            return
        if root.val == val:
            global target 
            target = root
            find = True
        preorder1(root.left,val,find)
        preorder1(root.right,val,find)

    preorder1(root,val,False)
    if target.val == 0 :
        return None
    return target
          
def preorder(root:TreeNode):
    if root==None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root:TreeNode):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def inorder(root:TreeNode):
    if root==None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)





datalist = [100,90,110,95,120,105,140,70]
i = 0
tree1 = Tree()
while (i<len(datalist)):
    tree1.insert(datalist[i])  
    i+=1

print("-----preorder-----")
preorder(tree1.root)






