# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

def height(root, depth=0):
  if root.left == None and root.right == None:
    return depth
  elif root.left != None and root.right == None:
    return height(root.left, depth + 1)
  elif root.left == None and root.right != None:
    return height(root.right, depth + 1)
  return max(height(root.left, depth + 1), height(root.right, depth + 1))
