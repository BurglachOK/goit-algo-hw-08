import heapq


def cables_addiction(cables):
    money = 0
    for i in range(len(cables) - 1):
        if len(cables) == 1:
            return cables[0]
        heapq.heapify(cables)
        min_elem_1 = heapq.heappop(cables)
        min_elem_2 = heapq.heappop(cables)
        cost = min_elem_1 + min_elem_2
        money += cost
        heapq.heappush(cables, cost)
    print('Мінімальні загальні витрати:', money)


gables = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cables_addiction(gables)
