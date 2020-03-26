class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    #pushing an element into linkedlist
    def push(self,newnode):
        if self.head is None:
            self.head=newnode
        else: 
            temp=self.head
            self.head=newnode
            newnode.next=temp
    #printing elements of linkedlist
    def printllist(self):
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            else:
                print(currentnode.data)
                currentnode=currentnode.next
if __name__=='__main__':
    firstnode=Node(4)
    llist=LinkedList()
    llist.push(firstnode)
    secondnode=Node(2)
    llist.push(secondnode)
    thirdnode=Node(2)
    llist.push(thirdnode)
    fourthnode=Node(1)
    llist.push(fourthnode)
    llist.printllist()


    