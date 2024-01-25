class Node:
    def __init__(self,value=0):
        self.data=value
        self.next=None 
class MyLinkedList:
    def __init__(self):
        self.length=0
        self.head=None

    def get(self, index: int) -> int:
        temp=self.head
        if index < self.length:
            for i in range(index):
                temp=temp.next
            return temp.data
        return -1
        

    def addAtHead(self, val: int) -> None:
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
            self.length+=1
        else:
            newnode.next=self.head
            self.head=newnode
            self.length+=1

    def addAtTail(self, val: int) -> None:
        newnode=Node(val)
        temp=self.head
        if self.length==0:
            self.addAtHead(val)
            return
        while temp.next:
            temp=temp.next
        temp.next=newnode
        self.length+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.length:
            return
        if index==0:
            self.addAtHead(val)
        elif index==self.length:
            self.addAtTail(val)
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            newnode=Node(val)
            newnode.next=temp.next
            temp.next=newnode
            self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.length-=1
        elif index<self.length:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            #print(temp.data)
            temp.next = temp.next.next
            self.length-=1
   


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)