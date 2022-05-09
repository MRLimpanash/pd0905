x=int(input("Ievadi pirkuma summu: "))
if x>=500:
  print("Jums jāsamaksā ",x*0.8)
elif 500>x>=200:
  print("Jums jāsamaksā ",x*0.9)
else:
  print("Jums jāsamaksā ",x)