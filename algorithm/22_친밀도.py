friend_info = {"Summer":["John", "Justin","Mike"],"John":["Summer", "Justin"],"Justin":["Summer","Mike","John","May"],"Mike":["Summer","Justin"],"May":["Justin"],"May":["Justin","Kim"],"Kim":["May"],"Tom":["Jerry"],"Jerry":["Tom"]}

def print_all_friends(g, name):
    # 앞으로 처리해야 할 사람들을 큐(리스트)에 저장
    queue = []

    # 큐에 추가한 사람들 기록
    end = set()
    # name을 queue, end 추가
    queue.append((name, 0)) # queue = [("Summer",0),("Justin",1)]
    end.add(name)
  
    # 반복문 : 큐에 사람이 있을 때까지
    while queue:
        # 큐에서 한 사람씩 꺼내서 이름 출력
        person, liked = queue.pop(0)
        print(person, liked)

        # 반복문 -  꺼낸 이름을 키 값으로 해서 아직 큐에 추가된 적이 없는 사람을
        for p in g[person]:
            if p not in end:
                # 큐에 추가하고 end에도 추가
                queue.append((p,liked+1))
                end.add(p)
            
    return end

if __name__ == "__main__":
    print(print_all_friends(friend_info, "Summer"))
    print()
    print(print_all_friends(friend_info, "Jerry"))