import sys
sys.stdin = open('input.txt')

T = 10


# 후위 표기식으로 변환하는 함수
def stack(string):
    # 스택 선언
    stk = []
    # 결과를 담을 리스트 선언
    result = []
    for s in string:
        # 숫자가 아니면 결과에 담는다
        if s != '+':
            result.append(s)
        # 스택에 아무것도 없다면 스택에 담는다
        elif len(stk) == 0:
            stk.append(s)
        # 스택에 무언가가 있다면 pop 해서 결과에 담고 현재 값을 스택에 담는다
        elif len(stk) > 0:
            result.append(stk.pop())
            stk.append(s)
    # for 다 돌고 스택에 남은 것 result 에 담기
    result.extend(stk)
    # string 으로 변환해 반환
    return ''.join(result)


# 후위 표기식을 계산하는 함수
def cal(result):
    stk = []
    for idx in range(len(result)):
        # 만약 숫자면 스택에 담는다
        if result[idx] != '+':
            stk.append(int(result[idx]))
        # 만약 더하기면, 스택에 있는 두 숫자를 pop 해서 더한 후 스택에 넣는다.
        elif result[idx] == '+':
            stk.append(stk.pop() + stk.pop())
    # 스택의 0번 인덱스 항목을 반환한다.
    return stk[0]


for tc in range(1, T+1):
    L = int(input())
    string = input()
    print('#{} {}'.format(tc, cal(stack(string))))
