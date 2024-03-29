import pytest
# 잼민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다.
# 캐릭터가 있는 장소는 1 X 1 크기의 정사각형으로 이뤄진 N X M 크기의 직사각형으로,
# 각각의 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다.
# 맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의개수,
# B는 서쪽으로부터 떨어진 칸의 개수이다. 캐릭터는 상하좌우로 움직일 수 있고,
# 바다로 되어 있는 공간에는 갈 수 없다.
# 캐릭터의 움직임을 설명하기 위해 정해 놓은 매뉴얼은 이러하다.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸 전진한다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
#    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
# 잼민이는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.
# 메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
@pytest.mark.parametrize(
    "n, m, info, map, expected",
    [(4, 4,
      "1 1 0",
      [[1, 1, 1, 1],
       [1, 0, 0, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 1]],
      3),
     (4, 4,
      "0 0 0",
      [[0, 0, 1, 1],
       [1, 0, 0, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 1]],
      5)
     ])
def test_solve(n, m, info, map, expected):
    result = solve1(n, m, info, map)
    assert result == expected


def solve_m(n, m, info, map):
    return map.count(0)

def solve1(n, m, info, field):
    d = [[0] * m for _ in range(n)]
    x, y, direction = map(int, info.split())

    d[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def turn_left():
        nonlocal direction
        direction -= 1
        if direction == -1:
            direction = 3

    count = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]

        if d[nx][ny] == 0 and field[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if field[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    return count