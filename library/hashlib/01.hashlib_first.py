import hashlib
sha256 = hashlib.sha256()

pwd = '0000'
#sha256을 사용하기 위해 encode를 해야한다.
encode_pwd = pwd.encode()
print(encode_pwd)
sha_pwd = hashlib.sha256(encode_pwd).hexdigest()
print(sha_pwd)

pwd2 = '0000'
encode_pwd2 = pwd2.encode()
print(encode_pwd2)
sha_pwd2 = hashlib.sha256(encode_pwd2).hexdigest()
print(sha_pwd2)

print(sha_pwd == sha_pwd2)

"""
참고 사이트
https://www.vitoshacademy.com/hashing-passwords-in-python/
를 이용해서 password 장고와 유사하게 만들어보기
입력 비밀번호가 같더라도 slat값이 다르다면 false만들어내기
위의 내용에서는 hexdigest()를 없애면 되긴하는데 salt값을 정확히 건드리진 못하겠기에...
"""