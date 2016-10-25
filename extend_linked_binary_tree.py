
# coding: utf-8

# In[66]:

from linked_binary_tree import LinkedBinaryTree
class ExtendLinkedBinaryTree(LinkedBinaryTree):
    
    def preorder_next(self, p):
        """Method to find next preorder element."""
        # get node of the position p
        position_node = self._validate(p)  
        # if the node has left child, return left child
        if position_node._left is not None:
            return self.left(p)
        # else if the node has right child, return right child
        else:           
            if position_node._right is not None:  
                return self.right(p)
            # else move the position node to the parent node --- incase of no children go up
            else:
                position_node = self._make_position(position_node._parent)      # parent node declaration
                # if p is the left child of the node and there exist right child, return right child
                if self.left(position_node) == p  and self.right(position_node) != None:      
                    return self.right(position_node)
                # if p is the left child and right child exist return right child. If p is right child go up and return the respective node.
                else:  
                    position_node = self._validate(position_node)
                    # Checking if the node is root node and raising an exception if root.parent is called for next preorder
                    try:
                        while position_node == position_node._parent._right:
                            position_node = position_node._parent
                    except AttributeError:
                        raise AttributeError("This is the last element in preorder.")
                    return self._make_position(position_node._parent._right)
    
    
    def inorder_next(self,v):
        """Method to find next inorder element."""
        
        # if internal node
        if not self.is_leaf(v):
            rchild = self.right(v) 
            # Check is the node has right child and return if true
            if rchild == None:
                return self.parent(self.parent(v))  
            # if node doesnot have rightchild 
            else:
                # go down until left child exist and return the last left child
                while self.left(rchild) != None: 
                    rchild = self.left(rchild)
                return rchild
        else: # incase of external node
            rchild = v 
            p = self.parent(rchild) # change p to parent
            # if the node is right child, change p's parent
            while self.right(p) == rchild:
                # checking if p is root
                if self.is_root(p): 
                    return None
                else:
                    # set p to parent
                    rchild = p 
                    p = self.parent(rchild)
            return p
        
    def postorder_next(self,v): 
        "Method to find next postorder element."
        parent = self.parent(v)
        # if v is internal node
        if not self.is_leaf(v): 
            # if v is right child, return parent
            if self.right(parent) == v:
                return self.parent(v)
            # else, v = parent.right
            else:
                v = self.right(parent)
                # while v is internal node, set v to left child
                while not self.is_leaf(v):
                    if self.left(v) == None:
                        v = self.right(v)
                    else:
                        v = self.left(v)
            # return the leftmost child
            return v
        
        else:
            # v is right child, return parent
            if self.right(parent) == v:
                return parent
        
            else:# incase of left child v
                # if right child exist, return that
                if self.right(parent) == None:
                    return parent
                # else, set v to parent.right 
                else:    
                    v = self.right(parent)
                
                # loop in case of internal node
                while not self.is_leaf(v):
                    # if v has left child return that
                    if self.left(v) != None:
                        v = self.left(v)
                    # else return right child
                    else:
                        v = self.right(v)
                        
                return v    
    
    def delete_subtree(self, p):
        """Method to delete subtree at position p and return node"""
        # set node at position p 
        node = self._validate(p)
        # set parent node
        parent = node._parent
        
        # if the node is left child set the child to none
        if parent._left == node:
            parent._left = None
    
        else:# else set right node to none
            parent._right = None
        
        
        node._parent = node             
        self._size = 1

        for i in self.postorder():
            self._size += 1
        self._size -= 1

        return node._element
  

if __name__ == '__main__':
    
    p = ExtendLinkedBinaryTree()
    
    t0 = p._add_root(0)
    t1 = p._add_left(t0,1)
    t2 = p._add_right(t0,2)
    t3 = p._add_left(t1,3)
    t4 = p._add_right(t1,4)
    t5 = p._add_left(t2,5)
    t6 = p._add_right(t2,6)
    t7 = p._add_left(t4,7)
    t8 = p._add_right(t4,8)
    t9 = p._add_right(t5,9)
    t10 = p._add_left(t9,10)
    
    try:
        print ("--------------------------------------------------------------------")
        print ("Position of a node and its element:")
        print ("---------------------------------------------------------------")
        print ("Position:",t5, "\nElement:",t5.element())
        print ()
        print ("--------------------------------------------------------------------")
        print ("preorder() - the elements store in the preorder traversal")
        print ("----------------------------------------------------------------------")

        for y in p.preorder():
            print (y.element(),end =" ")
    
    except Exception as e:
        print (e)
    
    try:
        print("\n")
        print ("--------------------------------------------------------------------")
        print ("preorder_next on few elements")
        print ("--------------------------------------")
        print ("Preorder_next(",t4.element(),")",":", p.preorder_next(t4).element())
        print ("Preorder_next(",t8.element(),")",":", p.preorder_next(t8).element())
    except Exception as e:
        print (e)
        
    print ()
    print ("--------------------------------------------------------------------")
    print ("inorder() - elements stored in the inorder traversal ")
    print ("---------------------------------------------------------------------")
    for x in p.inorder():
        print (x.element(),end = " ")
    
    print ("\n")
    print ("Calling inorder_next on few elements")
    print ("------------------------------------")
    print ("Inorder_next(",t4.element(),")",":", p.inorder_next(t4).element())
    print ("Inorder_next(",t3.element(),")",":", p.inorder_next(t3).element())
    print ()
    print ("--------------------------------------------------------------------")
    print ("postorder() - the elements store in the postorder traversal ")
    print ("--------------------------------------------------------------------")
    
    for i in p.postorder():
        print (i.element(),end =" ")
    print("\n")
    
    
    try:
        print ("postorder_next on few elements")
        print ("--------------------------------------")
        print ("Postorder_next(",t5.element(),")",":", p.postorder_next(t5).element())
        #print ("Postorder_next(",t0.element(),")",":", p.postorder_next(t0).element())
        print ("Postorder_next(",t9.element(),")",":", p.postorder_next(t9).element())
        print ()
    
    except Exception as e:
        print (e)
    
    try:
        print ("delete_subtree() at", t5.element())
        print ("------------------------------------------------------------------------------------")
        p.delete_subtree(t5)
        print ("Calling inorder to print elements in the remaining tree")
        print("--------------------------------------------------------------------------------------------")    
        for i in p.inorder():
            print (i.element(),end = " ")
        print ("\n")
    except Exception as e:
        print (e)
        


# In[ ]:




# In[28]:




# In[ ]:




# In[ ]:



