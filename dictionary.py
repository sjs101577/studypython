#딕셔너리 실습
paris={'하이라이트':'불어온다', '이달의소녀':'So what', '로제':'On the ground'}

#하나의 키 - value 쌍을 더 추가하는 방법 : 딕셔너리 변수[[키] = value]
# print(paris)
# paris['스테이씨']='ASAP'
# print(paris)

#특정키 - value 쌍을 삭제하는 방법 : del 변수[키]
# del paris['로제']
# print(paris)

# key value 값을 찾는 방법 : 딕셔너리 변수.get(키)
print(paris.get('이달의소녀'))
print(paris)