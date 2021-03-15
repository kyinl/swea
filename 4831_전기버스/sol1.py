import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    KNM = list(map(int, input().split()))
    K = KNM[0]
    N = KNM[1]
    M = KNM[2]
    # K, N, M = map(int, input().split()) 으로 해도 된다.
    charge_list = list(map(int, input().split()))
# 내 풀이의 아이디어: 일단 충전을 고려하지 않고 진행하다가 배터리가 0이 되면 지나온 충전소를 확인해서
# 올바르게 충전했더라면 현재 남아있어야 할 배터리의 양으로 바꿔준다.
    battery = K  # 현재 남은 배터리의 양
    station = 0  # 현재까지 진행한 정류장의 수
    charge = 0  # 충전 횟수
    before_charge_list = []  # 배터리가 다 닳은 시점에서, 이미 지나온 충전소의 번호들을 담는 리스트
    # 이중 while 문: 안쪽의 while 문은 반복 진행중에 배터리가 다 닳았을 경우 충전을 고려하기 위함
    while battery > 0:
        while battery > 0:
            # 한칸씩 가면서 배터리를 한칸씩 쓴다.
            station += 1
            battery -= 1
        # 도착했으면 while 문 탈출
        if station >= N:
            break
        # 만약 멈춘 곳에 충전소가 있다면 바로 K만큼 충전
        if station in charge_list:
            battery = K
            charge += 1
        # 만약 멈춘 곳에 충전소가 없다면, 지나온 충전소 중 가장 가까운 충전소에서 충전했을 시 현재 남아있을 배터리 양으로 변경
        else:
            for charge_station in charge_list:
                if charge_station < station:
                    before_charge_list.append(charge_station)
            # 지나온 충전소 중 가장 현재 위치와 가까운 충전소 구하기
            before_charge_max = 0
            for before_charge_station in before_charge_list:
                if before_charge_station > before_charge_max:
                    before_charge_max = before_charge_station
            # 만약 지나온 충전소가 너무 멀어서 다음 충전소까지 가기에 충분하지 않은 경우
            if station - before_charge_max >= K:
                # 0을 출력하도록 한다.
                charge = 0
            else:
                # 올바른 배터리 양으로 변경
                battery += K - (station - before_charge_max)
                charge += 1
                # 리스트를 재사용하기 위해 비워준다.
                before_charge_list = []

    print('#{} {}'.format(tc, charge))
