
def mcd(n1, n2):
	resto = 0
	while(n2 > 0):
		resto = n2
		n2 = n1 % n2
		n1 = resto
	return resto

print(mcd(174, 173))
print(mcd(10, 20))
print(mcd(5, 10))
print(mcd(10, 5))



#traza
# loop condicion(n2>0) n1       n2          Resto  
# 1    TRUE            20->10   10->0       0->10                   20%10=0
# 2    False -->retorno resto=10            
# 
# 


