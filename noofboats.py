def noOfBoat(people, limit):
    people.sort()
    l = len(people)
    left = 0
    right = l - 1
    boat = 0
    while (left <= right):
      if (left == right):

        boat += 1
        break

      if ((people[left] + people[right]) <= limit):
        left += 1
      right -= 1  
      boat += 1
        

    return boat


print(noOfBoat([3, 2, 2, 1], 3))