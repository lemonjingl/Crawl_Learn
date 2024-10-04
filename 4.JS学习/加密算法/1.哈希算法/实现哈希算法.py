from hashlib import md5,sha1,sha256,sha512
import time
a=int(time.time()*1000)
print(str(a))

obj=md5()
obj1=sha1()
obj2=sha256()
obj3=sha512()

str='lzzsll'.encode('utf-8')

str2='f1e945dbn6r45e4t4r32'.encode('utf-8')
print(str2)
obj.update(str2)
print(obj.hexdigest())

# obj.update(str)
# m=obj.hexdigest()
# s1=obj1.hexdigest()
# s256=obj2.hexdigest()
# s512=obj3.hexdigest()
# print(f'{m}---{len(m)}')
# print(f'{s1}---{len(s1)}')
# print(f'{s256}---{len(s256)}')
# print(f'{s512}--{len(s512)}')
# 5be0d24f7cf33242816b93e6b179109b
# 0x9cc88672ddfe1f841361334d4f11173c
# 0a3dd164f7b9014cdc5359af334d5afb
print(len('319c1fe1b1698919b4eefaae93059d78'))