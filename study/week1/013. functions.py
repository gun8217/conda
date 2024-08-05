data_a, data_b = [1, 2, 3], [10, 20, 30]; data_c = ['a', 'b', 'c']; text = "Hello"; data_tuple = (1, 2, 3, 4)


###### sum : 반복 가능한(iterable) 객체(리스트, 튜플 등)의 모든 요소 합을 계산
fun_sum = sum(data_a)
print(f"{fun_sum = }\n")


###### len : 시퀀스(sequence) 또는 컬렉션의 요소의 개수(길이)를 반환
# 시퀀스 : 리스트(list), 튜플(tuple), range 객체, 문자열(string) 등의 순서를 가지고 있는 요소
fun_len_list = len(data_a)
fun_len_text = len(text)
fun_len_tuple = len(data_tuple)
print(f"length : {fun_len_list = }, {fun_len_text = }, {fun_len_tuple = }\n")


###### range : 연속된 정수를 생성(반복문과 함께 사용해 반복 횟수 지정 및 특정 범위 숫자 생성)
numbers = range(5)
print(f"range(stop): {list(numbers)}")
numbers = range(2, 5)
print(f"range(start, stop): {list(numbers)}")
numbers = range(1, 7, 2)
print(f"range(start, stop, step): {list(numbers)}\n")


###### zip : 2개 이상의 객체 병렬로 묶어주는 역할(같은 인덱스 요소를 튜플 묶어 반환)
zip1 = zip(data_a, data_b)
print(f"{list(zip1) = }")
zip2 = zip(data_a, data_c)
tuple_zip = tuple(zip2)
print(f"{tuple_zip = }\n")


###### enumerate : 반복 가능한 인덱스와 값을 튜플로 반환하는 반복자 생성
for index, value in enumerate(data_c):
    print(f"Index: {index}, Value: {value}")
    
for index, value in enumerate(data_b, start=1):
    print(f"index 시작번호 수정 → Index: {index}, Value: {value}")
    
object_enumerate = enumerate(text)
print(f"{list(object_enumerate) = }")