#!/usr/bin/env python3
from hashlib import md5
def solve(input):
    def genHash(path, key=input):
        return md5(key + path.encode()).hexdigest()

    start_room = (0, 0)
    vault_room = (3,3)

    def unlockedDoors(room, path, key=input):
        unlocked = {'U':False, 'D':False, 'L':False, 'R':False}
        hash = genHash(path, key)
        unlocked['U'] = hash[0] in {'b', 'c', 'd', 'e', 'f'}
        unlocked['D'] = hash[1] in {'b', 'c', 'd', 'e', 'f'}
        unlocked['L'] = hash[2] in {'b', 'c', 'd', 'e', 'f'}
        unlocked['R'] = hash[3] in {'b', 'c', 'd', 'e', 'f'}
        # edges
        if room[1] == 0:
            unlocked['U'] = False
        if room[1] == 3:
            unlocked['D'] = False
        if room[0] == 0:
            unlocked['L'] = False
        if room[0] == 3:
            unlocked['R'] = False
        return unlocked

    assert(unlockedDoors((0, 0), "", b"hijkl") == {'U':False, 'D':True, 'L':False, 'R':False})
    assert(unlockedDoors((0, 1), "D", b"hijkl") == {'U':True, 'D':False, 'L':False, 'R':True})
    assert(unlockedDoors((1, 1), "DR", b"hijkl") == {'U':False, 'D':False, 'L':False, 'R':False})
    assert(unlockedDoors((0, 0), "DU", b"hijkl") == {'U':False, 'D':False, 'L':False, 'R':True})

    def move(room, dir):
        if dir == 'U':
            return (room[0], room[1] - 1)
        if dir == 'D':
            return (room[0], room[1] + 1)
        if dir == 'L':
            return (room[0] - 1, room[1])
        if dir == 'R':
            return (room[0] + 1, room[1])

    branch_points = set() # set of tuples: (tuple: (x, y), string: path)
    # search for path
    path = ""
    doors = unlockedDoors(start_room, path)
    for dir in doors:
        if doors[dir]:
            branch_points.add((move(start_room, dir), path + dir))

    while True:
        if len(branch_points) == 0:
            # shouldn't be here, there's no path
            print("there's no path!")
            break

        room, path = min(branch_points, key = lambda p : len(p[1]))

        if room == vault_room:
            # print("we've made it!")
            # print("took {} steps, path:".format(len(path)))
            return path

        branch_points.remove((room, path))

        doors = unlockedDoors(room, path)
        for dir in doors:
            if doors[dir]:
                branch_points.add((move(room, dir), path + dir))
    return path

assert(solve(b"ihgpwlah") == "DDRRRD")
assert(solve(b"kglvqrro") == "DDUDRLRRUDRD")
assert(solve(b"ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR")

# real input
print(solve(b"qzthpkfp"))
# it's not RDRDDR

# part 2
def solve_longest(input):
    def genHash(path, key=input):
        return md5(key + path.encode()).hexdigest()

    start_room = (0, 0)
    vault_room = (3,3)

    def unlockedDoors(room, path, key=input):
        unlocked = {'U':False, 'D':False, 'L':False, 'R':False}
        hash = genHash(path, key)
        unlocked['U'] = hash[0] in {'b', 'c', 'd', 'e', 'f'}
        unlocked['D'] = hash[1] in {'b', 'c', 'd', 'e', 'f'}
        unlocked['L'] = hash[2] in {'b', 'c', 'd', 'e', 'f'}
        unlocked['R'] = hash[3] in {'b', 'c', 'd', 'e', 'f'}
        # edges
        if room[1] == 0:
            unlocked['U'] = False
        if room[1] == 3:
            unlocked['D'] = False
        if room[0] == 0:
            unlocked['L'] = False
        if room[0] == 3:
            unlocked['R'] = False
        return unlocked

    def move(room, dir):
        if dir == 'U':
            return (room[0], room[1] - 1)
        if dir == 'D':
            return (room[0], room[1] + 1)
        if dir == 'L':
            return (room[0] - 1, room[1])
        if dir == 'R':
            return (room[0] + 1, room[1])

    branch_points = set() # set of tuples: (tuple: (x, y), string: path)
    # search for path
    path = ""
    doors = unlockedDoors(start_room, path)
    for dir in doors:
        if doors[dir]:
            branch_points.add((move(start_room, dir), path + dir))

    found_path = ""
    while True:
        if len(branch_points) == 0:
            return found_path
            break

        room, path = min(branch_points, key = lambda p : len(p[1]))

        branch_points.remove((room, path))

        if room == vault_room:
            found_path = path
        else:
            doors = unlockedDoors(room, path)
            for dir in doors:
                if doors[dir]:
                    branch_points.add((move(room, dir), path + dir))
    return "NO PATH"

assert(len(solve_longest(b"ihgpwlah")) == 370)
assert(len(solve_longest(b"kglvqrro")) == 492)
assert(len(solve_longest(b"ulqzkmiv")) == 830)

print(len(solve_longest(b"qzthpkfp")))
