# 숫자 n 개를 리스트로 입력받아 최솟값 구하기

# 숫자 입력 받기
# q라는 문자가 입력되면 리스트 추가하는 것을 종료
# def num_input(list1):
#     while True:
        
#         a = input("숫자를 입력해주세요. : ")
#         if a == "q":
#             break
#         else:
#             list1.append(int(a))
#             print("숫자 입력을 계속합니다. 숫자 추가를 끝내기 위해서는 q를 입력하세요")

#     return list1

def num_input(list1):
    i = 1
    print("리스트에 추가할 숫자를 입력하세요.\n 숫자 추가를 끝내기 위해서는 q 를 입력하세요.")
    while True:
        print(str(i), ": ", end="")
        num = input()

        if num != "q":
            list1.append(int(num))
        else:
            break
        i = i+1
    return list1

# 최솟값 구하기
def min(list1):
    min = list1[0]
    for n in list1:
        if n < min:
            min = n

    return min

if __name__ == "__main__":
    list1 = list() # 비어있는 리스트 생성
    a = num_input(list1)
    print("귀하가 입력하신 값은 {}입니다. 그 값들 중 최솟값은 {}입니다.".format(a, min(list1)))