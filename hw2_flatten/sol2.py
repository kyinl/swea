import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    count = 0
    while count < N:
        index_max = max(range(len(boxes)), key=boxes.__getitem__)
        index_min = min(range(len(boxes)), key=boxes.__getitem__)
        boxes[index_max] -= 1
        boxes[index_min] += 1
        count += 1
    box_max = max(boxes)
    box_min = min(boxes)
    print('#{} {}'.format(tc, box_max - box_min))
