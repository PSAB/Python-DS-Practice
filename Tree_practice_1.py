class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, newNode):
        if not self.leftChild:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self, newNode):
        if not self.rightChild:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# Traversal as standalone functions:

def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.leftChild)
        preorder(tree.rightChild)

def inorder(tree):
    if tree:
        inorder(tree.leftChild)
        print(tree.key)
        inorder(tree.rightChild)

def postorder(tree):
    if tree:
        postorder(tree.leftChild)
        postorder(tree.rightChild)
        print(tree.key)
