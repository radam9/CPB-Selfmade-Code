# .format() Method
print('This is a string {}'.format('INSERTED'))
#using index positions
print('The {} {} {}'.format('fox','brown','quick'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {0} {0} {0}'.format('fox','brown','quick'))
#Assigning keywords to the index positions
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
print('The {f} {f} {f}'.format(f='fox',b='brown',q='quick'))
#using the float formatting {value:width.precision f}
result = 100/777
print('The result was {}'.format(result))
print('The result was {r}'.format(r=result))
print('The result was {r:1.3f}'.format(r=result))
print('The result was {r:10.3f}'.format(r=result))
print('The result was {r:10.5f}'.format(r=result))
#Alignment, by defualt, text alignment is left and number are right
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
#Choosing alignment
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
#Padding characters
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
