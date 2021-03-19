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
from app.Dao.chamado_dao import *

@app.callback(
    [
        Output("data-table-chamado", "data"),
        Output("data-table-chamado", "selected_rows")
    ],
    [
        Input('btt_salvar_chamado', 'n_clicks'),
        Input('btt_deletar_tudo_2', 'n_clicks'),
        Input('btt_deletar_itens_2', 'n_clicks'),
    ],
    [
        State("titulo", "value"),
        State("chamado", "value"),
        State("equipamento", "value"),
        State("data_abertura", "value"),
        State("data-table-chamado", "selected_rows"),
        State("data-table-chamado", "data"),
    ])
def update_data_table(n_clicks_add_1, n_clicks_delete_tudo_1, n_clicks_delete_itens_1,
                titulo_chamado, descrição, equipamento, data_abertura,
                selected_data, data):

    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
        return create(), []
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
    L = data.copy()
    

    if button_id == 'btt_salvar_chamado':
        if all([titulo_chamado, descrição, equipamento, data_abertura]):
            if not isin(L, titulo_chamado):
                L = add(L,titulo_chamado, descrição, equipamento, data_abertura) 
            
    elif button_id == 'btt_deletar_tudo_2':        
        L = create()        

    elif button_id == 'btt_deletar_itens_2':
        L = remove_by_indexes(L, selected_data)

    print(L)

    return L, []
