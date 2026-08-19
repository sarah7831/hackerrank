if __name__ == '__main__':
    
    N = int(input())
    result_list = []
    
    for _ in range(N):
        # Split the input line into command and its arguments
        command_args = input().split()
        command = command_args[0]
        
        if command == "insert":
            index = int(command_args[1])
            element = int(command_args[2])
            result_list.insert(index, element)
            
        elif command == "print":
            print(result_list)
            
        elif command == "remove":
            element = int(command_args[1])
            result_list.remove(element)
            
        elif command == "append":
            element = int(command_args[1])
            result_list.append(element)
            
        elif command == "sort":
            result_list.sort()
            
        elif command == "pop":
            result_list.pop()
            
        elif command == "reverse":
            result_list.reverse()
