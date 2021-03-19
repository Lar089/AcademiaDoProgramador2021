def create():
    return []
    
def isin(L, titulo_chamado):
    for item in L:
        if item['Titulo_chamado'] == titulo_chamado:
            return True
    return False

def add(L, titulo_chamado, descricao, equipamento, data_abertura):
    L2 = L.copy()
    L2.append({'Titulo_chamado' : str(titulo_chamado), 'Descricao' : str(descricao), 
            'Equipamento' : str(equipamento), 'Data_abertura' : str(data_abertura)})    
    return L2

def remove_by_number(L, titulo_chamado):
    L = [item for item in L if not item['Titulo_chamado'] == titulo_chamado]
    return L

def remove_by_indexes(L, idx):       
    L2 = L.copy()    
    L2 = [i for j, i in enumerate(L2) if j not in idx]    
    return L2

def remove_all(L):    
    return create()


