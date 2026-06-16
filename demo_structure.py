import cProfile
from collections import deque

# list = []

# list.append(42)
# list.append(44)
# list.append(0)

# # print(list.pop(0))

# queue = deque()
# queue.append(42)
# queue.append(44)
# queue.append(0)

# # print(queue.popleft())


# def f_with_list():
#     l = []
#     for i in range(100_000):
#         l.append(i)
#     while l:
#         l.pop(0)

# def f_with_queue():
#     l = deque()
#     for i in range(100_000):
#         l.append(i)
#     while l:
#         l.popleft()

# cProfile.run('f_with_list()')
# cProfile.run('f_with_queue()')


# chaine = 'Hello world !!!!!'
# chaine += chaine

# print(chaine)


from io import StringIO
# chaine = StringIO()
# chaine.write('Hello world !!!')
# chaine.write('Hello world !!!')

# print(chaine.getvalue())


# def f_without_stringio():
#     result = ''
#     for i in range(1_000_000):
#         result += f'Hello world !!!!!  {i}'

#     return result

# def f_with_stringio():
#     result = StringIO()
#     for i in range(1_000_000):
#         result.write(f'Hello world !!!!!  {i}')

#     return result.getvalue()


# cProfile.run('f_without_stringio()')
# cProfile.run('f_with_stringio()')


import heapq

l = []

heapq.heappush(l, 42)
heapq.heappush(l, 17)
heapq.heappush(l, 14)
heapq.heappush(l, 24)

# print(heapq.heappop(l))
# print(heapq.heappop(l))
# print(heapq.heappop(l))
# print(heapq.heappop(l))

heapq.heappushpop(l, 18)
# print(l)

# print(heapq.heappop(l))
# print(heapq.heappop(l))
# print(heapq.heappop(l))
# print(l)