import random
xs=[1,2,3,4,5,6,7,8,9,10]
ys=[1,2,3,4,5,6,7,8,9,10]
combi3=[]
combi5=[]
grid=[]
hit=[]
hits = 0
miss = 0
i=0
ii=0
def inlist(my_list, item):
  o=0
  for counter in my_list:
    if item in counter:
      o=o+1
      return True
  return False    
  o=0
  for counter in my_list:
    if item in counter:
      o=o+1
      return counter.remove(item)
  return False          

def ships(whichone,index):
    whichone=whichone.split()
    j=0
    for counter in whichone:
      whichone[j]=int(whichone[j])
      j=j+1
    if index == "three":
      l1=[whichone[0],whichone[1]]
      l2=[whichone[2],whichone[3]]
      l3=[whichone[4],whichone[5]]
      whichone.clear()
      whichone.append(l1)  
      whichone.append(l2)
      whichone.append(l3)
    elif index == "five":
      l1=[whichone[0],whichone[1]]
      l2=[whichone[2],whichone[3]]
      l3=[whichone[4],whichone[5]]
      l4=[whichone[6],whichone[7]]
      l5=[whichone[8],whichone[9]]
      whichone.clear()
      whichone.append(l1)  
      whichone.append(l2)
      whichone.append(l3)
      whichone.append(l4)
      whichone.append(l5)
    return whichone  
#grid formation
for x in xs:
  for y in ys:
    g=[x,y]
    grid.append(g)

for xx in range(1,xs-1):
  for yy in range (1,ys-1):
    combi3.append([[xx,yy],[xx,yy+1],[xx,yy+2]])
    combi3.append([[xx,yy],[xx+1,yy],[xx+2,yy]])
for xx in range(1,xs-4):
  for yy in range(1,ys-4):
     combi5.append([[xx,yy],[xx,yy+1],[xx,yy+2],[xx,yy+3],[xx,yy+4]])
     combi5.append([[xx,yy],[xx+1,yy],[xx+2,yy],[xx+3,yy],[xx+4,yy]])
     
    
#grid.pop(0)
c_grid=grid    
selected=True
playerCorrect=True
while selected:
  choice1=random.choice(combi3)
  choice2=random.choice(combi3)
  choice3=random.choice(combi3)
  choice4=random.choice(combi3)
  choice5=random.choice(combi5)
  c_Choices=[ choice1, choice2, choice3, choice4, choice5]
  for counter in c_Choices:
    for counter1 in c_Choices:
      if counter != counter1:
        i=i+1
  if i>24:
    selected=False
    while playerCorrect:
      print("Enter the three coordinates of your first ship seperated by a space")
      pChoice1=input()
      print("Enter the three coordinates of your second ship seperated by a space")
      pChoice2=input()
      print("Enter the three coordinates of your third ship seperate by a space")
      pChoice3=input()
      print("Enter the three coordinates of your fourth ship seperated by a space")
      pChoice4=input()
      print("Enter the five coordinates of your fifth ship seperated by a space")
      pChoice5=input()
      pChoice1=ships(pChoice1,"three")
      pChoice2=ships(pChoice2,"three")
      pChoice3=ships(pChoice3,"three")
      pChoice4=ships(pChoice4,"three")
      pChoice5=ships(pChoice5,"five")
      p_Choices=[pChoice1,pChoice2,pChoice3,pChoice4,pChoice5]
      if pChoice1 in combi3:
        i=i+1
      if pChoice2 in combi3:
        i=i+1
      if pChoice3 in combi3:
        i=i+1
      if pChoice4 in combi3:
        i=i+1
      if pChoice5 in combi5:
        i=i+1
      if i>4: 
        playerCorrect=False
      else:
        print("Mistakes in coordinates place again")
i=0        
print(p_Choices)
# print(c_Choices)
continuing=True
while continuing:
  ii=ii+1
  print("Round",ii)
  print("Computer has",len(c_Choices),"ships left")
  crd=input("Enter coordinate to bomb seperated by a space: ")
  crd=ships(crd,"nein")
  hit.append(crd)
  #grid.remove(crd)
  for counter in hit:
    print(counter)
  if inlist(c_Choices,crd):
    print("HIT at ",crd)
    hits=hits+1
    h=0
    i=0
    for counter in c_Choices:
      if crd in counter:
        c_Choices[h].remove(crd)
        break
      else:
        h=h+1 
  else:
    print("miss")
    miss=miss+1
  print(f"You have hit {hits} times and missed {miss} times")
  for counter in c_Choices:
    if not counter:
      c_Choices.remove(counter)
  if not c_Choices:    
    print("Congrats you win, it took you ",ii,"Attempts")
    continuing=False
    break
  c_fire=random.choice(c_grid)
  c_grid.remove(c_fire)
  print(f"Computer fires at {c_fire}")
  if inlist(p_Choices,c_fire):
    print("Hit")
    o=0
    for counter in p_Choices:
      if c_fire in counter:
        p_Choices[o].remove(c_fire)
        print("Ships locations left")
        print(p_Choices)
      else:
        o=o+1
  else:
    print("Computer misses")
  if not p_Choices:
    print(f"Computer wins after {ii} attempts")
    continuing=False
  
  