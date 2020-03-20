#Implementing Stack
#push Function!
def Push(top,stack,stack_size,head):
    for i in range(0,stack_size,1):
        top=top+1
        if(top<=4):
            e=int(input('Enter an Element:'))
            stack.append(e)
        else:
            print('Stack is Overflow')
#Pop Function

        
def Pop(stack,stack_size):
    top=int(len(stack))
    if(top==0):
        print('stack is Underflow')
    else:
        print('')
    top-=1
    try:
        for i in range(0,stack_size,1):
            choice=input('Want To Delete an Element(d/n):')
            if(choice=='d'):
                print(stack[top])
                stack.remove(stack[top])
                top=top-1           
            elif(choice=='n'):
                print('Stack is',stack)
                exit
                return stack
            elif(top==0):
                print('stack is UnderFlow')
                return stack
            else:
                print('No Element is Exist')       
        
    except:
        print('Stack is Underflow or a Empty')
    return stack
#For Displaying Stack!

def display(top,stack):
    if(top<=4):
        print(stack)
    elif(top==0):
        print('Stack is Empty')
    else:
        print('Fatal Error')
        
print('**********************************************************')
stack_size=int(input('Enter The Size of Stack Which you want to prefer:'))
stack=[]
top=len(stack)
head=0
print('Instruction:=  Size of Stack size is:{0}'.format(stack_size))
print('Want to Perform an Operation:')
print('Operations Are:\n 1.Push\n 2.Pop \n 3.Display')
print('**********************************************************')
for i in range(0,100,1):
    ip=int(input('Enter The Operation Which You Want to Perform:'))
    if(ip==1):
        Push(top,stack,stack_size,head)
    elif(ip==2):
        Pop(stack,stack_size)
    elif(ip==3):
        display(top,stack)
    else:
        break

