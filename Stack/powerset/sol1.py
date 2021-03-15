# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 의 powerset 중 원소의 합이 10인 부분집합을 구하시오.


def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        result = 0
        for idx in range(len(a)):  # 답이면 원하는 작업을 한다
            if a[idx]:
                a[idx] = idx + 1
                result += (idx + 1)
            else:
                a[idx] = 0
        if result == 10:
            a = list(set(a))
            a.remove(0)
            print(sorted(a))

    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k-1] = c[i]
            backtrack(a, k, input)


def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2


def process_solution(a, k):
    pass


MAXCANDIDATES = 100
NMAX = 10
a = [0] * NMAX
backtrack(a, 0, 10)

