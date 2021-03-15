import sys
sys.stdin = open('input.txt')


isp = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,
    ')': None
}

icp = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 3,
    ')': None
}


# 후위 표기식으로 변환하는 함수
def trans(string):
    # 스택 선언
    stack = []
    # 결과를 담을 리스트 선언
    result = []
    for s in string:
        # 기호가 아니면 결과에 담는다
        if s not in isp.keys():
            result.append(s)
        # 여는 괄호는 무조건 스택에 push
        else:
            if s == '(':
                stack.append(s)
            # 닫는 괄호는 여는 괄호가 나올 때까지 pop
            elif s == ')':
                while stack:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        result.append(stack.pop())
            else:
                # 스택에 아무것도 없다면 스택에 push
                if not stack:
                    stack.append(s)

                else:
                    # 스택에 무언가가 있다면
                    while stack:
                        # 만약 현재 연산자의 우선순위보다 스택의 마지막 연산자의 우선순위가 크거나 같으면
                        if icp[s] <= isp[stack[-1]]:
                            # 스택의 마지막 연산자를 pop 하여 결과에 담는다
                            result.append(stack.pop())
                        else:
                            # 현재 연산자의 우선순위가 더 클때까지
                            break
                    # pop 이 다 끝나면 현재 연산자를 스택에 push
                    stack.append(s)

    # for 다 돌고 스택에 남은 것을 결과에 담는다
    while stack:
        result.append(stack.pop())
    # string 으로 변환해 반환
    return ''.join(result)


# 후위 표기식을 계산하는 함수
def cal(result):
    stack = []
    for idx in range(len(result)):
        # 만약 숫자면 스택에 push
        if result[idx] not in isp.keys():
            stack.append(int(result[idx]))
        # 만약 기호면, 스택에 있는 두 숫자를 연산한 후 스택에 push
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if result[idx] == '+':
                stack.append(num2 + num1)
            elif result[idx] == '-':
                stack.append(num2 - num1)
            elif result[idx] == '*':
                stack.append(num2 * num1)
            elif result[idx] == '/':
                stack.append(num2 / num1)

    # 스택의 0번 인덱스 항목을 반환한다.
    return stack[0]


T = 10

for tc in range(1, T+1):
    length = input()
    string = input()
    print('#{} {}'.format(tc, cal(trans(string))))
