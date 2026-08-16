def merge_the_tools(string, k):
    # your code goes heredef 
    for i in range(0, len(string), k):
        temp = string[i:i+k]
        print(''.join(set(temp)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
