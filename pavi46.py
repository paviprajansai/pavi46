p=input()
p1=""
for i in range(0,len(p)):
	if p[i].islower():
		p1=p1+p[i].upper()
	else:
		p1=p1+p[i].lower()
print(p1)		
