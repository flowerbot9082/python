from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__front = None #start left
    self.__real_front_index = None
    self.__back = None #start right
    self.__real_back_index = None
    self.__size = 0
  
  def initial_push(self, val):
    self.__contents[0] = val
    self.__front = self.__contents[0]
    self.__real_front_index = 0
    self.__back = self.__contents[0]
    self.__real_back_index = 0

  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    str_rep = "[ "
    if len(self) == 0:
      str_rep = "[ ]"
    else:
      for i in range(self.__real_front_index, self.__real_back_index + 1):
        a = 0
        if i == self.__real_front_index:
          str_rep += str(self.__contents[i])
        elif i > len(self.__contents) - 1:
          a = i % (len(self.__contents) - 1)
          str_rep += ", " + str(self.__contents[a])
        else:
          a = i
          str_rep += ", " + str(self.__contents[a])  
      str_rep += " ]"        
    return str_rep

  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    self.__capacity = 2 * self.__capacity
    og_contents = []
    if len(self) == 1:
      og_contents.append(self.__contents[0])
    else:
      for i in range(self.__real_front_index, self.__real_back_index + 1):
        a = 0
        if i > len(self.__contents) - 1: 
          a = i % (len(self.__contents) - 1)
        else:
          a = i
        og_contents.append(self.__contents[a])
    self.__contents = self.__capacity * [None]
    for i in range(0, len(og_contents)):
      self.__contents[i] = og_contents[i]
    self.__front = self.__contents[0]
    self.__real_front_index = 0
    self.__back = self.__contents[len(self) - 1]
    self.__real_back_index = len(self) - 1
    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if len(self) == 0:
      self.initial_push(val)
    else:
      self.__real_front_index -= 1
      if self.__real_back_index - self.__real_front_index == len(self.__contents):
        self.__real_front_index += 1
        self.__grow()
        self.__real_front_index -= 1
      index_array = self.__real_front_index
      self.__contents[index_array] = val
      self.__front = self.__contents[index_array]
    self.__size += 1
  
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if len(self) == 0:
      return None
    elif len(self) == 1:
      val_rm = self.__front
      self.__real_front_index = None
      self.__real_back_index = None
      self.__front = None
      self.__size = self.__size - 1
      return val_rm
    val_rm = self.__contents[self.__real_front_index]
    self.__real_front_index += 1
    index_array = self.__real_front_index
    if self.__real_front_index >= len(self.__contents): #change 2
      index_array = index_array % (len(self.__contents) - 1)
    self.__front = self.__contents[index_array]
    self.__size = self.__size - 1
    return val_rm

    
  def peek_front(self):
    # TODO replace pass with your implementation.
    return self.__front
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if len(self) == 0:
      self.initial_push(val)
    else:
      self.__real_back_index += 1
      if self.__real_back_index - self.__real_front_index == len(self.__contents):
        self.__real_back_index -= 1
        self.__grow()
        self.__real_back_index += 1 
      index_array = self.__real_back_index 
      if index_array > (len(self.__contents) - 1):
        index_array = index_array % (len(self.__contents) - 1)
      self.__contents[index_array] = val
      self.__back = self.__contents[index_array]
    self.__size += 1
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if len(self) == 0:
      return None
    elif len(self) == 1:
      val_rm = self.__back
      self.__real_front_index = None
      self.__real_back_index = None
      self.__back = None
      self.__size = self.__size - 1
      return val_rm
    val_rm = self.__contents[self.__real_back_index]
    self.__real_back_index -= 1
    index_array = self.__real_back_index
    self.__back = self.__contents[index_array]
    self.__size = self.__size - 1
    return val_rm
    

  def peek_back(self):
    # TODO replace pass with your implementation.
    return self.__back

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
