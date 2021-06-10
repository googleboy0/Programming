# Closed Hashing --> separate chaining using linked lists.
# Open addressing --> a) Linear Probing -> go i+1
#                     b) Quadratic Probing -> go by i^2
#                     c) Double Hashing

class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0

    def size(self):
        return self.count
    
    def getBucketIndex(self,hc):
        return (abs(hc)%(self.bucketSize))

    def getValue(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def remove(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None

        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                    return head.value
            prev = head
            head = head.next


    def insert(self,key,value):

        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.buckets[index]
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count+= 1