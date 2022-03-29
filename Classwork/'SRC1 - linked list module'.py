'SRC1 - linked list module'
class Node:
    'Node class for linked list'
    def __init__(self,data :int,ptr :int) -> None:
        self.data = data
        self.ptr = ptr
    #end procedure

    def __repr__(self) -> str:
        return f'(Data: {self.data}; Pointer: {self.ptr})'
    #end function
#end class

class LinkedList:
    'Linked list class'
    def __init__(self,size) -> None:
        self.sp = -1
        self.nf = 0
        self.container = [Node(None,-1)]
        while size > 1:
          self.container.insert(0,Node(None,size-1))
          size -= 1
        #end while
    #end procedure (constructor)

    def __repr__(self) -> str:
        output_str = f'(Start Pointer: {self.sp}; Next free: {self.nf})\n'
        for node in self.container:
          output_str += node.__repr__() + '\n'
        #next node
        return output_str
    #end function

    def insert(self,item):
        if self.nf == -1:
            print("List is full")
        else:
            self.container[self.nf].data = item
            if self.sp == -1:
                temp = self.container[self.nf].ptr
                self.container[self.nf].ptr = -1
                self.sp = self.nf
                self.nf = temp
            else:
                p = self.sp
                if item < self.container[p].data: 
                    self.container[p].ptr = self.sp
                    self.sp = self.nf
                else:
                    found = False
                    while (self.container[p].ptr != -1) and (found == False):
                        if item >= self.container[self.container[p].ptr].data:
                            p = self.container[p].ptr
                        else:
                            found = True
                    temp = self.nf
                    self.nf = self.container[temp].ptr
                    self.container[temp].ptr = self.container[p].ptr
                    self.container[p].ptr = temp
      #End Procedure

    def delete(self,item):
        if self.sp == -1:
            print("List is empty")
        else:
            p = self.sp
            if item == self.container[self.sp].data:
                start = self.container[self.sp].ptr
            else:
                while item != self.container[self.container[p].ptr].data:
                    p = self.container[p].ptr
            temp = self.container[p].ptr
            self.container[p].ptr = self.container[temp].ptr
            self.container[temp].ptr = self.nf
            self.nf = temp
    #End Procedure

#end class

if __name__ == "__main__":
    my_node = Node(-1,-1)
    print(my_node)
    my_list = LinkedList(5)
    print(my_list)
    my_list.insert(4)
    print(my_list)
    my_list.delete(4)
    print(my_list)