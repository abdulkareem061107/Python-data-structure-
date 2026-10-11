from collections import defaultdict, deque

graph = defaultdict(list)
m = int(input("Enter the number of friendships: "))
print("Enter friendships (User1 User2):")

for i in range(m):
    u, v = input(f"Friendship {i + 1}: ").split()
    graph[u].append(v)
    graph[v].append(u)


def display_friends(user):
  print(f"\nDirect friends of {user}:")
  for friend in graph[user]:
    print(friend)


def bfs(start):
  visited = set()
  queue = deque([start])
  visited.add(start)
  print("\nBFS Traversal:")
  while queue:
    user = queue.popleft()
    print(user, end=" ")
    for friend in graph[user]:
      if friend not in visited:
        visited.add(friend)
        queue.append(friend)
  print()


def dfs_util(start, visited):
  visited.add(start)
  print(start, end=" ")
  for friend in graph[start]:
    if friend not in visited:
      dfs_util(friend, visited)


def dfs(start):
  visited = set()
  print("\nDFS Traversal:")
  dfs_util(start, visited)
  print()


print("\nSocial Network:")
for user in graph:
  print(user, "->", graph[user])

start = input("\nEnter the user to start traversal: ")

if start in graph:
  display_friends(start)
  bfs(start)
  dfs(start)
else:
  print("User not found!")
