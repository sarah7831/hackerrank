# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
for i in range (n):
     number = input()
     if len(number) == 10 and number[0] in '789' and number.isdigit():
        print("YES")
     else:
        print("NO")
