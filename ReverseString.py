def reverseString(givenString):
  j = len(givenString) - 1
  index = 0

  givenList = list(givenString)

  while index < j:
    temp = givenList[index]
    givenList[index] = givenList[j]
    givenList[j] = temp
    index += 1
    j -= 1

  result = "".join(givenList)
  return result


inputString = (input("What is your name? "))
print("Your reversed name is ", reverseString(inputString));
