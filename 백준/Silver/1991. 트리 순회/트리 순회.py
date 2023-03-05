import sys 

class Node:
  def __init__(self,data,left,right):
    self.data = data
    self.left = left
    self.right = right


def pre_order(s):
  print(s.data, end='')
  if s.left != None:
    pre_order(tree[s.left])
  if s.right != None:
    pre_order(tree[s.right])    

def inorder(s):
  if s.left != None:
    inorder(tree[s.left])
  print(s.data, end='')
  if s.right != None:
    inorder(tree[s.right])  

def post_order(s):
  if s.left != None:
    post_order(tree[s.left])
  if s.right != None:
    post_order(tree[s.right])  
  print(s.data, end='')



n = int(input())  # 노드의 갯수
tree = {}



for i in range(n):
  data, left, right = sys.stdin.readline().split()
  if left == '.':
    left = None
  if right == '.':
    right = None
  obj = Node(data, left, right) 
  tree[data] = obj

# print(tree)
pre_order(tree['A'])  # A에 해당하는 Node의 객체 전달
print()
inorder(tree['A'])
print()
post_order(tree['A'])