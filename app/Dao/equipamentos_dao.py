def create():
    return []
    
def isin(L, numero_serie):
    for item in L:
        if item['Numero_serie'] == numero_serie:
            return True
    return False

def add(L, nome, preco, data_fabricacao, numero_serie, fabricante):
    L1 = L.copy()
    L1.append({'Nome' : str(nome), 'Preco' : float(preco), 'Data_fabricacao' : data_fabricacao, 
            'Numero_serie' : str(numero_serie), 'Fabricante' : str(fabricante)})    
    return L1

def remove_by_number(L, numero_serie):
    L = [item for item in L if not item['Numero_serie'] == numero_serie]
    return L

def remove_by_indexes(L, idx):       
    L1 = L.copy()    
    L1 = [i for j, i in enumerate(L1) if j not in idx]    
    return L1

def remove_all(L):    
    return create()


