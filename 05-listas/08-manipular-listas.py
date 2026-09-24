frutas = [ "maça", "banana", "laranja"]

#index()
print("index(): ", frutas.index("banana"))

#Count 
print("Count(): ", frutas.count("banana"))

#Append
frutas.append("Uva")
print("Append():", frutas)


#extend
outras_frutas = ["Abacaxi", "Morango"] 
frutas.extend(outras_frutas)
print("Extend():", frutas)