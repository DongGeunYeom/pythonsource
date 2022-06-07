# 미로찾기
# 미로의 각 위치에 알파벳으로 이름 지증
maze = {
    "a": ["e"],
    "b": ["c", "f"],
    "c": ["b", "d"],
    "d": ["c"],
    "e": ["a", "i"],
    "f": ["b", "h", "j"],
    "g": ["f", "h"],
    "h": ["g", "l"],
    "i": ["e", "m"],
    "j": ["f", "k", "n"],
    "k": ["j", "o"],
    "l": ["p", "h"],
    "m": ["n", "i"],
    "n": ["j", "m"],
    "o": ["k"],
    "p": ["l"],
}


def find_exit(maze, start, end):
    # 앞으로 이동해야 할 이동 경로를 큐에 저장
    play = []

    # 큐에 추가한 꼭짓점을 집합에 저장(중복 제거)
    path = set()

    # 출발점 큐와 집합에 추가
    play.append(start)
    path.add(start)

    # 큐에 경로가 남아있는 동안
    while play:
        way = play.pop(0)

        # 큐에 저장된 이동경로의 마지막 문자가 현재 처리해야 할 꼭짓점임
        goal = way[-1]

        if goal == end:
            return way

        for p in maze[goal]:
            if p not in path:
                print("큐", play, type(play))
                print("집합", path, type(path))
                play.append(way + p)
                path.add(p)

    return "미로 탈출 불가"


if __name__ == "__main__":
    print(find_exit(maze, "a", "p"))
