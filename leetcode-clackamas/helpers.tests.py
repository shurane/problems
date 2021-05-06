from helpers import TreeNode

t = TreeNode.fromList([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # full
# print(t.printAll())
assert list(t.inorder()) == list(range(1,16))
# u = TreeNode.fromList([1000,200,300,40,None,None,7])
# print(u.printAll())

v = TreeNode.fromList([1,None,3,None,None,None,7,None,None,None,None,None,None,None,15]) # right only
# print(v.printAll())
assert list(v.inorder()) == [1,3,7,15]

w = TreeNode.fromList([1,2,None,4,None,None,None,8]) # left only
# print(w.printAll())
assert list(w.inorder()) == [1,2,4,8]
