'''
함수 만들기
# 1. 무슨 함수 만들지(이름)
# 2. input: 파라미터, 매개변수, 인수, 인자, argument
# 3. output: 리턴값, 결과값
# 4. 구현(implement)
함수명 규칙: 소문자로 짓고 여러 단어가 들어가는 경우 _로 연결한다.
'''

### 값을 더하는 함수 정의 ###

'''
함수를 만들기 전에 생각해야 할 것
무엇을 input으로 받을 건지, 뭘 결과값으로 내뱉어줄건지
input 받은 값으로 결과값을 어떻게 만들어낼건지
'''

# x, y 값을 받아서 더하도록

# 1. input: x, y
# 2. output: x와 y를 더한 값
# 3. 구현: x + y
def sum(x, y):
    result = x + y
    return result


### 더하는 함수 사용하기 ###

# 값을 바로 넣어도 되고, 변수에 넣어도 된다.
# 넘길 때의 변수명과 함수의 파라미터명은 달라도 된다.
# 함수의 파라미터는 함수 내에서만 유효하다.

# 이렇게만 하면, 계산은 됐으나 return값을 받지 못한 상태임
#sum(1, 2)

# 리턴값을 받아야 한다.
sumResult = sum(1, 2)
print(sumResult)

# 또는 sum(1, 2) 자체에 더한 결과값이 들어있는 상태이기 때문에 그냥 출력해도 된다.
print(sum(1, 2))


### 만약, 몇 개를 더하게 될 지 모른다면? 파라미터 개수를 모를 때 ###

def add_many(*args):
    result = 0
    for i in args:
        result += i

    return result

print(add_many(1, 2, 3, 4, 5))




### 리턴값이 없는 함수 ###

def minus(x, y):
    print("x에서 y를 뺀 값은 %d입니다." % (x - y))

minus(10, 7)
