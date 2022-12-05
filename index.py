# Own number system
import time
import redis

SYS_NAME = "sys:"

redis = redis.Redis(host='localhost', port=6379, db=0)

def key_sysname(n):
 return f"sys:{n}:name"

def encrypt(decimal, chars=[]):
  """
  x = 26

  b = 4
  ch = [a, b, c, d]
       [i1,i2,i3,i4] (1 based index for simplicity)

   rep = x//b = 6
   extra = x%b = 2 (i2)
   set = rep + 1 = 7 (x falls in 7th d0 repeatable set)

   rep1 = set//b = 1
   extra1 = set%b = 3 (i3)
   set1 = rep1 + 1 = 2 (x falls in 2nd d1 repeatable set)

   rep2 = set1//b = 0
   extra2 = set1%b = 2 (i2)
   set2 = rep2 + 1 = 1 (x falls in 1st d2 repeatable set)

   repr = [ ch[extra2],   ch[extra1],ch[extra] ]
 	  [   b, 		c,      b   ]


  a,b,c,d,

  ba,bb,bc,bd,     ca,cb,cc,cd,     da,db,dc,dd,

  baa,bab,bac,bad, bba,bbb,bbc,bbd, bca,bcb,bcc,bcd, bda,bdb,bdc,bdd,
  caa,cab,cac,cad, cba,cbb,cbc,cbd, cca,ccb,ccc,ccd, cda,cdb,cdc,cdd,
  daa,dab,dac,dad, dba,dbb,dbc,dbd, dca,dcb,dcc,dcd, dda,ddb,ddc,ddd,

  baaa,
  """
  b = len(chars)
  x = decimal
  repr = []
  while x > 1:
    index = x%b
    repr.append(chars[index])
    rep = x//b
    x = rep + 1
  repr.reverse()
  return "".join(repr)

names = redis.keys("sys:*:name")
if len(names):
  print("Existing systems found")
  for i,n in enumerate(names):
    print(f"{i}) {n.decode('utf-8').split(':')[1]}")
print(f"-1) Create new system")

opt = int(input("Choose: "))

if opt >= 0:
#  print(names)
  name = names[opt].decode("utf-8")
  chars = redis.zrange(name, 0, -1)
  chars = list(map(lambda x: x.decode("utf-8"), list(chars)))
  print(chars)
  base = len(chars)
  sys = name.split(":")[1]
else:
  print("\n\u001B[34mCreate your own counting representation system.\u001B[0m\n")

  base = input("Enter the max count of unique characters ")

  if not base.isdigit():
    print("Invalid integer")
    exit(1)
  base = int(base) - 1

  z = str(input(f"Enter representation for nothingness (default:0) "))
  z = z or '0'

  chars = [z]

  for i in range(0,base):
    ch = None
    while not ch or ch in chars:
      ch = str(input(f"Enter unique representation for {i+1} "))
    chars.append(ch)

  print(chars)
  base = len(chars)
  sys = input("Name of your counting system: ")
  sys = sys or "your"
  data = {}
  for i,c in enumerate(chars):
    data[c] = i
  redis.zadd(key_sysname(sys), data)

ch = -1
print(f"1) Convert a decimal number representative to {sys} representative")
print(f"2) Convert a {sys} number representative to decimal representative")
print(f"3) Show all decimal number representations in {sys} system representative")
print("99) Exit\n")

print("\nWhat do you want from your system?\n")
ch = int(input("Choice: "))

while ch != 99:
  if ch == 1:
    x = int(input("Enter a decimal number representative, positive integer only: "))
    if x < 0:
      break
    if x < len(chars):
      print(chars[x])
      time.sleep(2)
      continue
    print(encrypt(x, chars))
    time.sleep(2)
    continue
  elif ch == 2:
    x = input(f"Enter a {sys} number representative: ")
  elif ch == 3:
    nos = []
    x = int(input(f"Enter limit in decimal representation: "))
  else:
    break

exit(0)

chars[0]
chars[1]
chars[1]
chars[1]
chars[1]
chars[1]
chars[1]
chars[1]
chars[1]
chars[1]
