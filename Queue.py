#Equeue for Addition of Elements.
#Dqueue for Deletion of Elements.

def Equeue(Q,qsize,front,rear):
    for i in range(0,qsize,1):
        e=int(input('Enter an Elment to be inserted:'))
        Q.append(e)
        rear.append(1)
    return rear
    return Q
def Dqueue(re,qsize,front):
    re=len(rear)
    for i in range(0,re,1):        
        i=input('Want to Perform an Deletion Operation(y/n):')
        if(i=='y'):
            print('The Number is Deleted from the Queue:{0}'.format(Q[front]))
            Q.remove(Q[front])
        elif(i=='n'):
            print('OK, Fine')
        else:
            print('Invalid Choice')


print('***************************************')


Q=[]

rear=[]

qsize=int(input('Enter The Size of the Queue:'))

front=0

re=0


print('OPerations  are:\n1.Equeue for Addition of Element.\n2.Dqueue for Deletion of Elements.\n3. Display.')

print('Press: 1 for Equeue.\n 2 for Dqueue\n3 for Display')

for i in range(0,100,1):
    ip=int(input('Enter the Operation Which you Want to Perform:'))
    if(ip==1):
        Equeue(Q,qsize,front,rear)
    elif(ip==2):
        Dqueue(re,qsize,front)
    elif(ip==3):
        if(len(Q)==0):
            print('Queue is Empty')
        else:
            print(Q)
