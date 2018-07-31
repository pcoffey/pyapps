# Some Dictionay play
# All Dictionary
lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level


gandolf = Wizard("Gandolf", 42)
print(gandolf.__dict__)

print(lookup)
print(lookup['loc'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

# Have data source and want to randomly access it, can use Dict
import collections

User = collections.namedtuple('User', 'id, name, email')
users = [
    User(1, 'user1', 'user1@example.com'),
    User(2, 'user2', 'user2@example.com'),
    User(3, 'user3', 'user3@example.com'),
    User(4, 'user4', 'user4@example.com')
]

lookup = dict()
for u in users:
    lookup[u.email] = u

print(lookup['user1@example.com'])