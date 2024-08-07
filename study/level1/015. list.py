###### list : 여러 개의 요소를 담을 수 있는 시퀀스 자료형 - [] 사용
list_data = list(range(5))
print(f"range 함수로 리스트 만들기 : {list_data = }")
str_data = list("Hello")
print(f"string을 리스트로 변환 : {str_data = }")
tuple_data = list((1, 2, 3))
print(f"tuple을 리스트로 변환 : {tuple_data = }\n")

test_list = [20, 30, 40, 50, 60]
# 메서드 : 추가
test_list.append(70)
print(f"한개만 추가(value) : {test_list}")
test_list.extend([80, 90])
print(f"여러개 추가(list) : {test_list}")
test_list.insert(0, 10)
print(f"특정 위치에 추가(idx, value) : {test_list}\n")

# 메서드 : 삭제
del test_list[1]
print(f"위치 지정 삭제(idx) : {test_list}")
test_list.remove(40)
print(f"특정 값 삭제(value) : {test_list}")
deleted_value = test_list.pop(0)
print(f"값 삭제 후 : {test_list}, 삭제된 값 반환(idx) : {deleted_value}")
test_list = test_list[:1] + test_list[3:]
print(f"index 1 ~ 3미만 요소 삭제 : {test_list}")

# 메서드 : 선택
test_list = test_list[1:3]
print(f"index 1 ~ 3미만 요소 선택 : {test_list}")