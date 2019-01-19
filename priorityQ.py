class priorityQueue():

    def __init__(self,list):
        self.queue = list

    def set_priority(self):
        print("""Priorities can range from 1 to 3.
1 is the highest priority and 3 is the lowest priority.""")
        for i in range(len(self.queue)):
            if len(self.queue[i]) == 1:
                priority = input("Set your priority for" + str(self.queue[i] ))
                while priority not in ["1","2","3"]:
                    priority = input("Please try again\n")
                self.queue[i].append(priority)
                #This changes the queue into a 2D array with each item being a list made up of the actual value and its priority
        return(self.queue)

    def enqueue(self,userInput):
        self.queue.append(userInput)
        #This adds whatever the user enters to the queue
        return(self.queue)

    def dequeue(self):
        queueLength = len(self.queue)
        if queueLength == 0:
            print("Queue is already empty")
        else:
#checks for the first value with priority 1
            for i in range(queueLength):
                if self.queue[i][1] == "1":
                    self.queue.remove(self.queue[i])
                    return(self.queue)
                    break
            if len(self.queue) == queueLength:
#If the length stays the same the computer knows that the queue has not been dequed yet
#The following checks for the first value with priority 2
                for i in range(queueLength):
                    if self.queue[i][1] == "2":
                        self.queue.remove(self.queue[i])
                        return(self.queue)
                        break
#What is remaining can only be values of priority 3 so the first value is removed
            if len(self.queue) == queueLength:
                self.queue.remove(self.queue[0])
                return(self.queue)

    def get_queue(self):
        printedQueue = []
        queueLength = len(self.queue)
        if queueLength > 0:
            if len(self.queue[0]) == 2:
                for i in range(queueLength):
                    printedQueue.append(self.queue[i][0])
                return(printedQueue)
            else:
                return(self.queue)

queue = priorityQueue([])
print("Your queue is empty now.")
while True:

    Choice = input('''1.Enqueue
2.Dequeue
3.Print Queue
4.Quit\n''')

    while Choice not in ["1","2","3","4"]:
        Choice = input("Please try again\n")

    if Choice == "1":
        userInput = input("What value do you want to add to the queue?")
        queue.enqueue([userInput])
        queue.set_priority()
    elif Choice == "2":
        queue.dequeue()
    elif Choice == "3":
        print(queue.get_queue())
    else:
        break
