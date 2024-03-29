# Problem
'''
N X N 크기의 공간에 물고기 M마리와 아기상어 1마리가 있습니다. 공간은 1 X 1 크기의 정사각형으로 나누어져 있습니다.
한 칸에는 물고기가 최대 1마리 존재합니다. 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수입니다.
가장 처음에 아기상어의 크기는 2이고, 아기상어는 1초에 상하좌우로 인접한 한 칸씩 이동합니다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있습니다.
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있습니다.
따라서 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있습니다.
아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같습니다.
 - 더이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청합니다.
 - 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 갑니다.
 - 먹을 수 있는 물고기가 1마리보다 많으면, 거리가 가장 가까운 물고기를 먹으러 갑니다.
    - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나가야 하는 칸의 개수의 최솟값입니다.
    - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기를 먹습니다.

아기 상어의 이동은 1초 걸리고, 물고기를 먹는 데 걸리는 시간은 없다고 가정합니다.
즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹습니다.
물고기를 먹으면, 그 칸은 빈칸이 됩니다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가하는데,
예를들어, 크기가 2인 아기상어는 물고기 2마리를 먹으면 크기가 3이됩니다.
공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하세요.
'''

# Input
'''
첫째 줄에 공간의 크기 N(2 <= M <= 20)가 주어집니다.
둘째 줄부터 N개의 줄에 공간의 상태가 주어집니다.
공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고 아래와 같은 의미를 가집니다.
- 0: 빈칸
- 1~6 : 칸의 있는 물고기의 크기
- 9 : 아기 상어의 위치
아기 상어는 공간에 1마리 있습니다.
'''

# Output
'''
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아 먹을 수 있는 시간을 출력합니다.
'''

# Example
'''
Input1
3
0 0 0
0 0 0
0 9 0

Output1
0

Input2
3
0 0 1
0 0 0
0 9 0
Output2
3

Input3
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
Output3
14
'''

# Solution
import heapq
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [[-1,0], [1,0], [0,-1], [0,1]]

def solution():
    heap = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                heapq.heappush(heap, (0, i, j))
                arr[i][j] = 0

    body, eat, ret = 2, 0, 0
    check = [[False] * N for _ in range(N)]
    while heap:
        d, x, y = heapq.heappop(heap)
        if 0 <  arr[x][y] < body:
            eat += 1
            arr[x][y] = 0
            if eat == body:
                body += 1
                eat = 0
            ret += d
            d = 0
            while heap:
                heap.pop()
            check = [[False] * N for _ in range(N)]
        for dx, dy in di:
            nd, nx, ny = d+1, x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if check[nx][ny] or arr[nx][ny] > body:
                continue
            check[nx][ny] = True
            heapq.heappush(heap, (nd, nx, ny))
    
    return ret
    
print(solution())