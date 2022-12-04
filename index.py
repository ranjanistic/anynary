# Own number system

"""
  x = 19

  b = 4
  ch = [a, b, c, d]
       [i1,i2,i3,i4] (1 based index for simplicity)
   rep = x/b = 4
   extra = x%b = 3 (i3)
   set = rep + extra = 5 (the x falls in 5th repeatable set)
   set/b
   dig = n

   repr = [    ch[extra-2],ch[extra] ]


  a,b,c,d,

  ba,bb,bc,bd,     ca,cb,cc,cd,     da,db,dc,dd,

  baa,bab,bac,bad, bba,bbb,bbc,bbd, bca,bcb,bcc,bcd, bda,bdb,bdc,bdd,
  caa,cab,cac,cad, cba,cbb,cbc,cbd, cca,ccb,ccc,ccd, cda,cdb,cdc,cdd,
  daa,cab,cac,cad, cba,cbb,cbc,cbd, cca,ccb,ccc,ccd, cda,cdb,cdc,ddd,

  baaa,

"""

print("\n\u001B[34mCreate your own counting representation system.\u001B[0m\n")

base = input("Enter the max count of unique characters ")

if not base.isdigit():
  print("Invalid integer")
  exit(1)
base = int(base)
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
sys = sys || "your"
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
    repr = ""
    rep = x / base
    
    x % base
    for i in range(0,x):
      for j in range(0,base):
      chars[0]
  elif ch == 2:
    x = input(f"Enter a {sys} number representative: ")
  elif ch == 3:
    nos = []
    x = int(input(f"Enter limit in decimal representation: "))
    for i in range(0,x):
      if i%base == 0:
        nos.append(
      chars[i]
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