# 1. 리스트 만들기
# - 데이터가 있는 리스트
animals = ["가물치", "벼메뚜기", "비단뱀", "도롱뇽"]

# - 데이터가 없는 리스트
empty = []

# 2. 데이터 조작하기

# - 데이터 접근하기
# 인덱스는 0부터 시작
print(animals[2])
print(animals[-1]) # -1은 리스트의 마지막 데이터를 호출한다

# - 데이터 추가하기
animals.append("고라니")
print(animals)

# - 데이터 할당하기
animals[1] = "청개구리"
print(animals)

# - 데이터 삭제하기
del animals [0]
print(animals)

# - 리스트 슬라이싱
print(animals[1:3])
print(animals[:]) #전체
print(animals[:3])
print(animals[1:])

# - 리스트 길이
print(len(animals))

# - 리스트 정렬
animals.sort(reverse=True)
print(animals)