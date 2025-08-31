# Stack Implementation using User Defined Functions

def push(stack, item, max_size=10):
    if len(stack) >= max_size:
        print("Stack Overflow! Cannot push", item)
    else:
        stack.append(item)
        print(item, "pushed into stack.")

def pop(stack):
    if not stack:
        print("Stack Underflow! Nothing to pop.")
    else:
        print("Popped item:", stack.pop())

def peek(stack):
    if not stack:
        print("Stack is empty, no top element.")
    else:
        print("Top element:", stack[-1])

def display(stack):
    if not stack:
        print("Stack is empty")
    else:
        print("Stack (top → bottom):")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

# Menu-driven Program
stack = []
while True:
    print("\n--- Stack Operations ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = input("Enter element to push: ")
        push(stack, item)
    elif choice == 2:
        pop(stack)
    elif choice == 3:
        peek(stack)
    elif choice == 4:
        display(stack)
    elif choice == 5:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
