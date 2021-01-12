from collections import deque

def solution(people, limit):
    
    people.sort(reverse=True)
    people = deque(people)

    boat = []
    boatCount = 1
    
    while people:
        if len(people) == 1:
            break
        boat.append(people.popleft())
        if boat[0] + people[len(people)-1] <= limit:
            boat.append(people.pop())
        if len(people) != 0:
            boat = []
            boatCount += 1
    
    return boatCount
