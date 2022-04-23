def postfix(s):
    priority = {"+":1,"-":1,"*":2,"/":2,"^":3}
    operators = ["+","-","*","/","^","(",")"]
    res = ""
    stack = []
    for i in s:
        if i not in operators:
            res += i
        elif i=="(":
            stack.append("(")
        elif i==")":
            while stack and stack[-1]!="(":
                res += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!="(" and priority[i]<=priority[-1]:
                res += stack.pop()
            stack.append(i)
    while stack:
        res += stack.pop()
    return res   


n = int(input())
for i in range(n):
    s = input()
    print(postfix(s))