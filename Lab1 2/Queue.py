# Queue Class implementation based on a python list
#@Author Josh Wright
class Queue:
    #constructor method
    #@param self
    #   The queue being constructed
    #@param args
    #   Arguments passed in to be added to the queue
    #@requires args is a python list
    #@ensures self is an empty queue or a queue of the ordered values of args
    def __init__(self,args=[]):
        self.rep = []
        if len(args)!= 0:
            self.rep = args 

    #Method to return the length of the Queue
    #@params self
    #   The Queue to find the length of
    #@returns the length of the Queue
    def __len__(self):
        return len(self.rep)

    #Returns the string representation of the queue
    def __str__(self):
        return self.rep.toString()

    #Returns the list representation of the queue
    #mostly for testing purposes
    #@return self.rep for the Queue object
    def toList(self):
        return self.rep

    #Adds an entry to the back/right side of the queue
    #@params self
    #   The queue that is being added to
    #@params entry
    #   The entry being enqueued
    #@updates self
    #@restores entry
    #@requires |entry| !=0
    #ensures self = $self + [entry]
    def enqueue(self,entry):
        self.rep.append(entry)

    #Removes an entry from the front/left side or the list
    #@params self
    #   The Queue that is having an entry removed
    #@updates self
    #@requires |self| > 0
    #@ensures self = $self - $self[0]
    def dequeue(self):
        return self.rep.pop(0)

    def front(self):
        return self.rep[0]
        
    def rotate(self,rotations=1):
        for i in range(0,rotations):
            self.rep.append(self.rep.pop(0))
















    


        
