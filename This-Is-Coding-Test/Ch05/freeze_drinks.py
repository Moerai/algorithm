import pytest

@pytest.mark.parametrize(
    "n, m, field, expected",
    [(4, 5,
      ["00110",
       "00011",
       "11111",
       "00000"],
      3
      )]
)
def test_solve(n, m, field, expected):
    result = solve_book(n, m, field)
    assert result == expected


def solve_book(n, m, graph):
    graph = list(map(list, graph))
    graph = [list(map(int, row)) for row in graph]

    count = 0

    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우에는 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        # 현재 노드를 아직 방문하지 않았다면
        if graph[x][y] == 0:
            # 해당 노드 방문 처리
            graph[x][y] = 1
            # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    # 모든 노드(위치)에 대하여 음료수 채우기
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 수행
            if dfs(i, j):
                count += 1

    return count