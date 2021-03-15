import sys
sys.stdin = open('input.txt')
# .__getitem__ 메서드 사용하지 않고 다시 풀었습니다.
T = 10
# input 처리
for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    # flatten 한 횟수를 세어, N과 같아지는 순간 끝나는 while 문 작성.
    count = 0
    while count < N:
        # boxes 안의 최댓값과 최솟값 구하기
        box_max = 0
        box_min = 101
        for box in boxes:
            if box > box_max:
                box_max = box
            if box < box_min:
                box_min = box
        # 만약 boxes 안의 한 값이 최댓값과 같다면 1을 빼준다.
        # 한 번에 하나씩만 이동하기 때문에 break 문을 이용해 바로 탈출한다.
        for idx in range(len(boxes)):
            if boxes[idx] == box_max:
                boxes[idx] -= 1
                break
        # 최솟값을 만났을 때 1을 더해주는 것은 위의 최댓값 - 1 과정과 세트이므로
        # 여기서만 count 에 1을 더해준다.
        for idx2 in range(len(boxes)):
            if boxes[idx2] == box_min:
                boxes[idx2] += 1
                count += 1
                break
    # boxes 의 값을 더하고 빼주면서 최댓값과 최솟값도 바뀌었기 때문에 다시 구해준다.
    box_max = 0
    box_min = 101
    for box1 in boxes:
        if box1 > box_max:
            box_max = box1
        if box1 < box_min:
            box_min = box1
    print('#{} {}'.format(tc, box_max - box_min))
