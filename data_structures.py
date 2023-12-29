from collections import deque

lista = [1, 2, 3, 4]
print(lista.index(2))
queue = deque([1, 2, 3, 4])
queue.append(6)
print(queue)
print(f"queue len: {len(queue)}")

squares = list(map(lambda x: x ** 2, lista))
print(squares)

listb = [1, 1, 2, 3, 4, 5, 6, 6, -1]
setb = set(listb)
setb.add(-1)
seta = set(setb)
print(sorted(setb))
print(seta)

a = lista[len(lista)//2]
print(a)

sample = "   fly me   to   the moon  "
print(sample.split())

print(len(sample.split()[-1]))
c = 6.56
print(int(c))

