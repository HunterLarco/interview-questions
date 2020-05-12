# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

def checkBST(root, domain=(-float('inf'), float('inf'))):
  if root is None:
    return True:
  if not (domain[0] < root.data < domain[1]):
    return False
  return (
      checkBST(root.left, domain=(domain[0], root.data)) and
      checkBST(root.right, domain=(root.data, domain[1])))
