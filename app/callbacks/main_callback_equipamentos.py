import pandas as pd
from datetime import date, datetime, timedelta
from dash.dependencies import Input, Output, State
import dash

# ----------------------------------------------------
# IMPORTS FRONT END
# ----------------------------------------------------
from app import app
from app.layout.layout_main import *
from app.layout.layout_result import *
from app.Dao.equipamentos_dao import *


@app.callback(
    [
        Output("data-table-quipamentos", "data"),
        Output("data-table-quipamentos", "selected_rows")
    ],
    [
        Input('btt_salvar_equipamentos', 'n_clicks'),
        Input('btt_deletar_tudo_1', 'n_clicks'),
        Input('btt_deletar_itens_1', 'n_clicks'),
    ],
    [
        State("name", "value"),
        State("preco", "value"),
        State("data_fabricacao", "value"),
        State("numero_serie", "value"),
        State("fabricante", "value"),
        State("data-table-quipamentos", "selected_rows"),
        State("data-table-quipamentos", "data"),
    ])
def update_data_table(n_clicks_add, n_clicks_delete_tudo, n_clicks_delete_itens,
                nome, preco, data_fabricacao, numero_serie, fabricante,
                selected_data, data):

    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
        return create(), []
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
    L = data.copy()
    

    if button_id == 'btt_salvar_equipamentos':
        if all([nome, preco, data_fabricacao, numero_serie, fabricante]):
            if not isin(L, numero_serie):
                if len(nome) >= 6:
                    L = add(L,nome, preco, data_fabricacao, numero_serie, fabricante)      
            
    elif button_id == 'btt_deletar_tudo_1':        
        L = create()        

    elif button_id == 'btt_deletar_itens_1':
        L = remove_by_indexes(L, selected_data)

    return L, []

