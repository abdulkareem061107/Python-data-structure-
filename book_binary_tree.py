class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new = Node(value)
        if self.root is None:
            self.root = new
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new
                    return
                current = current.right
            else:
                return

    def inorder(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, n, res):
        if n is None:
            return
        self._inorder(n.left, res)
        res.append(n.value)
        self._inorder(n.right, res)

    def preorder(self):
        res = []
        self._preorder(self.root, res)
        return res

    def _preorder(self, n, res):
        if n is None:
            return
        res.append(n.value)
        self._preorder(n.left, res)
        self._preorder(n.right, res)

    def postorder(self):
        res = []
        self._postorder(self.root, res)
        return res

    def _postorder(self, n, res):
        if n is None:
            return
        self._postorder(n.left, res)
        self._postorder(n.right, res)
        res.append(n.value)


tree = BinaryTree()
print("\n1,Insert \n2,Inorder \n3,Preorder \n4,Postorder \n5,Exit")
while True:
    choice = input("\nChoice: ")

    match choice:
        case "1":
            book = input("Enter book name: ")
            tree.insert(book)
        case "2":
            print(tree.inorder())
        case "3":
            print(tree.preorder())
        case "4":
            print(tree.postorder())
        case "5":
            break
        case _:
            print("Invalid choice")
