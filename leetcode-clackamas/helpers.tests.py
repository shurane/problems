from helpers import TreeNode, D

t = TreeNode.fromList([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # full
# print(t.printAll())
assert list(t.inorder()) == list(range(1,16))
assert t != None
# u = TreeNode.fromList([1000,200,300,40,None,None,7])
# print(u.printAll())

v = TreeNode.fromList([1,None,3,None,None,None,7,None,None,None,None,None,None,None,15]) # right only
v2 = TreeNode.fromListDirectional([1,3,7,15], dir=D.r)
# print(v.printAll())
assert list(v.inorder()) == [1,3,7,15]
assert list(v2.inorder()) == [1,3,7,15]
assert v == v2
assert v != t
assert t != v

w = TreeNode.fromList([1,2,None,4,None,None,None,8]) # left only
w2 = TreeNode.fromListDirectional([1,2,4,8], dir=D.l)
# print(w.printAll())
assert list(w.inorder()) == [1,2,4,8]
assert list(w2.inorder()) == [1,2,4,8]
assert w == w2
assert w != t
assert t != w
