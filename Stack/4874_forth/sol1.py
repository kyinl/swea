import sys
sys.stdin = open('sample_input.txt')


# 후위 표기식을 계산하는 함수
def cal(st):
    result = st.split()
    count_decimal = 0
    count_sign = 0
    # 에러 걸러내기
    for value in result:
        if value.isdecimal():
            count_decimal += 1
        else:
            count_sign += 1
    if count_decimal != count_sign:
        return 'error'

    stack = []
    for idx in range(len(result)):
        # 만약 숫자면 스택에 push
        if result[idx].isdecimal():
            stack.append(int(result[idx]))
        # 만약 기호면, 스택에 있는 두 숫자를 연산한 후 스택에 push
        #
        elif result[idx] == '.':
            if len(stack) > 1:
                return 'error'
            return stack[0]
        else:
            if len(stack) < 2:
                return 'error'
            num1 = stack.pop()
            num2 = stack.pop()
            if result[idx] == '+':
                stack.append(num2 + num1)
            elif result[idx] == '-':
                stack.append(num2 - num1)
            elif result[idx] == '*':
                stack.append(num2 * num1)
            elif result[idx] == '/':
                # 여기서 / 로 했더니 계속 패스가 안됐다.
                stack.append(num2 // num1)
            else:
                return 'error'


T = int(input())

for tc in range(1, T+1):

    string = input()
    print('#{} {}'.format(tc, cal(string)))
