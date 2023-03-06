# python3
def heap(data, nodes, i, swaps):
  s=i
  if (2*i+1<nodes) and data[2*i+1]<data[s]:
    s=2*i+1
  if (2*i+2<nodes) and data[2*i+2]<data[s]:
    s=2*i+1
  if i!=s:
    swaps.append((i,s))
    return s
  else:
    return i

def build_heap(data):
  swaps=[]
  
  nodes=len(data)

  for i in range(nodes//2, -1, -1 ):
    while True:
      s = heap(data,nodes,i, swaps)
      if s!=i:
        i=s
      else:
        i=s
        break
    
  #print(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


  return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
  bool1 = False
  readfrom = input()
  if ("I" in readfrom) or ("i" in readfrom):
    bool1 =True
    n = int(input())
    data = list(map(int, input().split()))
    
  if ("F" in readfrom) or ("f" in readfrom):
    name = "test/"+input()
    if not("a" in name):
      bool1 =True
      with open(name) as file:
        n = int(next(file))
        for line in file:
            data= list ([int(j) for j in line.split()])
  if bool1:  
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
