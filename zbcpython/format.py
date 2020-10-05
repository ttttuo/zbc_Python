#format함수
#.format (java의 system.out.printf()와 유사)
age = 26
name = 'Python'
print('{0} was {1} years old'.format(name, age))
print('{0} is easy'.format(name))

#문자열 더하기
print(name + ' 나이는 ' + str(age) + '이다')
print('{}의 나이는 {}이다'.format(name, age))

##format()의 추가 용법
#소수점 이하 원하는 자리까지 표기
print("{0:.3f}".format(1/3)) #0:.3f => 소수점 이허 세번째 자리까지 실수타입(float)으로.. 1/3의 값을 표현하라
#총 자리수 지정한 소수점 자리표기
y = 3.42134234123
print("{0:10.4f}".format(y))
#    3.4213
print("{0:10.11f}".format(y)) #제한된 자리수 보다 소수점자리를 크게하면 그냥 무시하고 처음부터 표시
print("{0:10.7f}".format(y))
#특수문자 채우는 것도 되나?
print("{0:_^10.4f}".format(y)) #됨
print("{0:^^10.11f}".format(y)) #그냥 소수점 11자리까지의 실수만 표기됨
print("{0:^^10.7f}".format(y))


#밑줄로 11칸 채우고 가운데 정렬
print("{0:_^11}".format("Hello"))
#정렬
# < : 왼쪽정렬, > : 오른쪽 정렬, ^ : 가운데 정렬
#왼쪽정렬
print("{0:_<11}".format("hi"))
print("{0:_>11}".format("hello"))

#사용자 지정 키워드 사용
print("{name} wrote {book}".format(name="Lim", book="Zero Base Coding"))
