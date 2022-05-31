# 리스트 안에 특정한 요소가 있는지 검색

# 순차 탐색 : 특정한 요소의 위치 리턴(찾는 경우), 못찾으면 -1
# 알고리즘 복잡도 : O(n)
def seq_search(list1, key):
    size = len(list1)

    for i in range(size):
        if key == list1[i]:
            return i
    return -1
    
# 찾는 숫자가 여러 개 있다면 모든 위치를 리스트로 리턴
def seq_search2(list1, key):
    list_idx = []
    size = len(list1)

    for i in range(size):
        if key == list1[i]:
            list_idx.append(i)            
    return list_idx
       

if __name__ == "__main__":
    list1 = [17,92,18,33,58,7,33,42]

    print("18 값 ", seq_search(list1, 18))
    print("33 값 ", seq_search(list1, 33))
    print("800 값 ", seq_search(list1, 800))
    print()
    print("18 값", seq_search2(list1, 18))
    print("33 값 ", seq_search2(list1, 33))
    print("800 값 ", seq_search2(list1, 800))