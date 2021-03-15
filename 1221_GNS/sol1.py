import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
# 순서를 담은 리스트 생성
order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

# input 특이사항: 테스트 케이스의 번호가 '#1' 형태로 주어지기 때문에
# int 로 바꾸지 않고 str 로 고려해야 한다.
for tc in range(1, T+1):
    tc_number, length = input().split()
    # 길이는 int 로 변환 (사용하지는 않았다)
    length = int(length)
    # 문자들이 담긴 리스트
    char = input().split()
    # 결과를 담을 리스트 생성
    result = []
    # order 순서대로 for 문 돌리기
    for idx in range(len(order)):
        # char 리스트 안에 있는 원소들 검사
        for idx_char in range(len(char)):
            # 만약 order 리스트의 현재 원소와 같으면 결과 리스트에 담는다
            if char[idx_char] == order[idx]:
                result.append(char[idx_char])
    # 입력에서 받은 테스트 케이스의 번호(#n)를 그대로 사용
    print('{}\n{}'.format(tc_number, ' '.join(result)))
