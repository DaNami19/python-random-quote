import random
def chounami():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=len(quotes)-1
  rnd=random.randint(0,last)
  print(quotes[0])
  print(quotes[rnd])
if __name__== "__main__":
  chounami()



