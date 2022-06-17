#Open a text file for writing
#text_file = open("data.txt", "w")
#text_file.write("This is a simple way to save data\n")
#text_file.write("one line at a time\n")
#text_file.write("Will this work")
#text_file.close()
#print("File created.")
#Open a text file for reading
#Open a text file for reading
#text_file = open("data.txt", "r")
#Read each line into a variable and output
#while True:
# a = text_file.readline()
# if not a: break
# print(a)

#Quote of the day challenge
#text_file=open("Quote of the day","w")
#text_file.write("If you fell down yesterday, stand up today")
#text_file=open("Quote of the day","r")
#print(text_file.readline())

#Quote of the day challenge 2
#text_file=open("Quote of the day","w")
#text_file.write("I'm uncreative 1\n")
#text_file.write("I'm still rather uncreative\n")
#text_file.write("I don't plan on being creative\n")
#text_file.write("Yeah no\n")
#text_file.close()
#text_file=open("Quote of the day","r")
#while True:
 # a=text_file.readline()
 # if not a: break
 # print(a)  
#Product catalogue challenge
#text_file=open("Product catalogue","w")
#text_file.write("Product name:")
#text_file.write(input("\nWhat is the name of your product:"))
#text_file.write("\nCode for product:")
#text_file.write(input("\nWhat is the code for your product:"))
#text_file.write("\nProduct Description:")
#text_file.write(input("\nGive a description for your product:"))
#text_file.close()
#text_file=open("Product catalogue","r")
#while True:
 # a=text_file.readline()
 # if not a: break
 # print(a)  

#product catalogue 2
i=0
print("1.Create a new catalogue")
print("2.Add a product to a catalogue")
print("3.Output items in catalogue")
while True:
  if i ==0:
    text_file=open("Product catalogue","w")
  else: text_file=open("Product catalogue","a")
  text_file.write("\nProduct name:")
  text_file.write(input("\nWhat is the name of your product:"))
  text_file.write("\nCode for product:")
  code=(input("\nWhat is the code for your product:"))
  if len(code) == 0:break
  else: text_file.write(code)
  text_file.write("\nProduct Description:")
  text_file.write(input("\nGive a description for your product:"))
  text_file.close()
  i=1
text_file.close()
text_file=open("Product catalogue","r")
while True:
  a=text_file.readline()
  if not a: break
  print(a) 

#product catalogue 3
