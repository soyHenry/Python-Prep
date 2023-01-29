def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    cantidadValores=0 
    newArr=[] 		  
    newArrSorted=[]   
    res ={}
    if not (type(diccionario_par) is dict):  
        return None
    if not (clave in diccionario_par.keys()): 
        return None                                 
    if len(diccionario_par[list(diccionario_par.keys())[0]])>0: 
        cantidadValores=len(diccionario_par[list(diccionario_par.keys())[0]])
        for i in range(0, cantidadValores):
            newObj={}
            for key in diccionario_par:
                newObj[key]=diccionario_par[key][i]
            newArr.append(newObj)
        newArrSorted = sorted(newArr, key=lambda d: d[clave], reverse=not (descendente))
        for key in diccionario_par:
            newArr2 = []
            for i in range(0, cantidadValores):
                newArr2.append(newArrSorted[i][key])
            res[key] = newArr2
    else:
            return diccionario_par
    
    return res

dicc = {
        'clave1':['c','a','b'],
        'clave2':['casa','auto','barco'],
        'clave3':[1,2,3]
        }

print (OrdenarDiccionario(dicc,"clave1")) 
