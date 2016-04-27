# Written by Eric Martin for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
        
        
    def rearrange(self):
        if not self.head:
            return
        First = self.head
 #       print(First.value)
        before_temp = First
  #      print(before_temp.value)
        temp = before_temp.next_node
  #      print(temp.value)

        
            
        while First.next_node:

            if self.compare(First.value, temp.value):
                
                before_temp.next_node = temp.next_node
                temp.next_node = First.next_node
                First.next_node = temp


                First = temp
                before_temp = temp
                temp = temp.next_node       
            else:
                if temp.next_node == None:
                    First = First.next_node
                    before_temp = First
                    temp = before_temp.next_node
                else:
                    before_temp = temp
                    temp = temp.next_node




                    
          
            

                
                
