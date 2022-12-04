# Own number system

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
    rep = x//b
    x = rep + 1
    repr.append(chars[index])
  repr.reverse()
  return "".join(repr)

print("\n\u001B[34mCreate your own counting representation system.\u001B[0m\n")

base = input("Enter the max count of unique characters ")

if not base.isdigit():
  print("Invalid integer")
  exit(1)
base = int(base) - 1
chars = []

for i in range(0,base):
  ch = None
  while not ch:
    ch = str(input(f"Enter representation for {i+1} "))
  chars.append(ch)

z = str(input(f"Enter representation for nothingness (default:0) "))
z = z or '0'

chars.insert(0,z)

print(chars)
base = len(chars)
sys = print("Name of your counting system: ")
sys = sys or "your"
ch = -1
while ch != 99:
  print("\nWhat do you want from your system?\n")

  print(f"1) Convert a decimal number representative to {sys} representative")
  print(f"2) Convert a {sys} number representative to decimal representative")
  print(f"3) Show all decimal number representations in {sys} system representative")
  print("99) Exit\n")
  ch = int(input("Choice: "))

  if ch == 1:
    x = int(input("Enter a decimal number representative, positive integer only: "))
    if x in range(0,base):
      print(chars[x])
      continue
    print(encrypt(x, chars))
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
