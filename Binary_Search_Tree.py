class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      # TODO complete Node initialization
      self.height = 1
      self.r_child = None
      self.l_child = None
      self.parent = None

  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def __None_check(self):
    pass
  def __balance(self, t):
    if t.r_child is None:
      right_child_height = 0
    
    if t.l_child is None:
      pass
    #left_child_height
    #left_right_child_height
    #right_left_child_height
    pivot = None
    double_rot_pivot = None
    balance_factor = t.r_child.height - t.l_child.height
    if balance_factor < -1: #rotate right
      if t.l_child.l_child.height - t.l_child.r_child.height > 0:
        #double rotate
        pass
    elif balance_factor > 1: #rotate left
      if t.r_child:
        pass
      pass
    else:
      pass
    return t
  
  def __create_node(self, value):
    return self.__BST_Node(value)
      
  def __r_ins(self, value, root):
    #finished
    #recursive function for insert_element
    
    if root is None:
      return self.__create_node(value)
    if value == root.value:
      raise ValueError
    else:
      if value < root.value:
        #GO LEFT
        root.l_child = self.__r_ins(value, root.l_child)
        root.height = root.l_child.height + 1
      elif value > root.value:
        #GO RIGHT
        root.r_child = self.__r_ins(value, root.r_child)
        root.height = root.r_child.height + 1
    if root.r_child is None or root.l_child is None:
      pass
    else:
      root.height = max(root.r_child.height, root.l_child.height) + 1
    return root

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    self.__root = self.__r_ins(value, self.__root)
  
  def __search_min(self, root):
    if root.l_child is None:
      return root.value
    else:
      self.__search_min(root.l_child)
  
  def __r_rem(self, value, root):
    #figure out how to get parent
    #recursive function for remove_element
    parent = root
    if root is None:
      #value not found
      raise ValueError
    else:
      if value == root.value:
        #REMOVAL
        if root.l_child is None and root.r_child is None:
          #no children case
          root = None
        elif root.l_child is None and root.r_child is not None:
          pass
          #parent.r_child = root.r_child 
        elif root.r_child is None and root.l_child is not None:
          pass
          #parent.l_child = root.l_child
        else:
          #2 children case
          a = self.__search_min(root.r_child) 
          root.value = a
          root.r_child = self.__r_rem(a, root.r_child)

      elif value < root.value:
        #GO LEFT
        root.l_child = self.__r_rem(value, root.l_child)
      elif value > root.value:
        #GO RIGHT
        root.r_child = self.__r_rem(value, root.r_child)
    if root is not None:
      root.height -= 1
    print(root.value)
    return root


  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__r_rem(value, self.__root)
    # TODO replace pass with your implementation

  def check_rec(self, root):
    if root is None:
      print(root)
    elif root is not None:
      print(str(root.value))
    
  def __rio(self, root, ret_str):
    #self.check_rec(root)
    if root is None:
      return
    self.__rio(root.l_child, ret_str)
    ret_str.append(root.value)
    self.__rio(root.r_child, ret_str)
    
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    #Left, self, Right
    return_str = []
    if self.__root is None:
      return "[ ]"
    self.__rio(self.__root, return_str)
    initial = "[ "
    end = " ]"
    return_str = initial + ', '.join(map(str,return_str)) + end
    return return_str

  def __rpre(self, root, ret_str):
    if root is None:
      return
    ret_str.append(root.value)
    self.__rio(root.l_child, ret_str)
    self.__rio(root.r_child, ret_str)

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    return_str = []
    if self.__root is None:
      return "[ ]"
    self.__rpre(self.__root, return_str)
    initial = "[ "
    end = " ]"
    return_str = initial + ', '.join(map(str,return_str)) + end
    return return_str
  
  def __rpos(self, root, ret_str):
    if root is None:
      return
    self.__rpos(root.l_child, ret_str)
    self.__rpos(root.r_child, ret_str)
    ret_str.append(root.value)

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    return_str = []
    if self.__root is None:
      return "[ ]"
    self.__rpos(self.__root, return_str)
    initial = "[ "
    end = " ]"
    return_str = initial + ', '.join(map(str,return_str)) + end
    return return_str
    # TODO replace pass with your implementation

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation
    if self.__root == None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

  def __r_list(self, root, ret_list):
    if root is None:
      return
    self.__r_list(root.l_child, ret_list)
    ret_list.append(root.value)
    self.__r_list(root.r_child, ret_list)

  def to_list(self):
    return_list = []
    self.__r_list(self.__root, return_list)
    return return_list

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.

