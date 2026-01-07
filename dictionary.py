# dictionary = a collection of {key : value} pairs
#               orderd and changeable. no duplicates



capitals = {"USA" : "Whasington D.C",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"
            }


#print(dir(capitals))

#print(capitals.get("USA"))

#print(capitals.get("Japan"))

#if capitals.get("Japan"):
    #print("That capital exists")
#else:
    #print("That capital does not exist")
    
#capitals.update({"Germany" : "Berlin"})
#capitals.update({"USA" : "Destroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()


keys = capitals.keys()

#print(keys)

#for key in capitals.keys():
    #print(key)
    
values = capitals.values()
#print(values)

#for value in capitals.values():
    #print(value)


items = capitals.items()
#print(items)
#for key, value in capitals.items():
    #print(f"{key} : {value}")
    
