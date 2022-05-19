# format()
# ~~.printf("%d",3) 와 같은 개념
# %c-문자 하나, %f-실수, %d-정수, %s-문자(만능)

print('%d'%100)
print('%5d'%100) # 5자리에 맞춰서 출력
print('%05d'%100)
print()
print('%s'%'hi')
print('%5s'%'hi')
print()
print("%8.2f"%12.21)
print("%-8.2f"%12.21) 
print("%-8.2f"%12.2134567)
print()
print("I eat %d apples" % 3)
print("I eat %s apples" % 3)
number=4
print("I eat %d apples" % number)
print("I eat", number,  "apples")