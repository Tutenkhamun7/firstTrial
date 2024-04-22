class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None 

    def insertData(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current= current.next
            current.next = node
    
    def displayData(self):
        current = self.head
        while(current.next):
            print(str(current.data) +"->", end="")
            current = current.next
        print(current.data)

    def compareData(self,l1,l2):
        head1=l1.head
        head2=l2.head
        equal = False
        if head1.data==head2.data:
            equal = True
            current1=head1
            current2=head2
            while(equal and (current1.next)):
                current1=current1.next
                current2=current2.next

                if current1.data!=current2.data:
                    equal = False
        return equal

LinkedListObj = LinkedList()
LinkedListObj1 = LinkedList()

n = int(input("Enter size: "))

for i in range(n):
    val = int(input("Enter list1 data: "))
    LinkedListObj.insertData(val)
    val1 = int(input("Enter list2 data: "))
    LinkedListObj1.insertData(val1)


# LinkedListObj.displayData()
# LinkedListObj1.displayData()

compObj =LinkedList()
x = compObj.compareData(LinkedListObj,LinkedListObj1)

print(x)
