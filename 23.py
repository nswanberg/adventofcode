def rotate(l, n):
    return l[n:] + l[:n]

#input = [int(i) for i in "389125467"] 
input = [int(i) for i in "253149867"]
cups = input[:]

i=1
indexOfCurrent=0
while i <= 100:
  current = cups[indexOfCurrent]
  rotcups = rotate(cups, indexOfCurrent)
  print('-- move ', i, ' --')
  print(cups)
  print(rotcups)

  tempIndex=0
  pickup = rotcups[1+tempIndex:1+tempIndex+3]
  pickup_without_cups = rotcups[:tempIndex+1]+rotcups[1+tempIndex+3:]
 
  # find destination 
  destination = current - 1
  while destination not in pickup_without_cups:
    destination -= 1
    if destination <= 0:
      destination = 9
  
  # visualize
  print('        ' + '   '*indexOfCurrent+'C')
  print('cups: ', cups)
  print('pick up: ', pickup)
  print('destination: ',destination)

  
  iD = pickup_without_cups.index(destination)
  print('indexOfDestination: ', iD)
  rotcups = pickup_without_cups[:iD+1]+pickup+pickup_without_cups[iD+1:]

  cups = rotate(rotcups, -indexOfCurrent)
  print('cups result: ', cups)
  indexOfCurrent = (indexOfCurrent + 1) % 9
  current = cups[indexOfCurrent]
  i+=1
  print('')

oneDex = cups.index(1)
cups = rotate(cups, oneDex)
print(cups)

print(''.join([str(i) for i in cups[1:]]))
