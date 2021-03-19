import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_table
import plotly.figure_factory as ff

# ---------------------------------
# IMPORTS
# ---------------------------------


# ---------------------------------
# LAYOUT GERAL
# ---------------------------------
layout = html.Div([

    html.Div([
        html.P(),
        dcc.Tabs([
            dcc.Tab(label='Equipamentos Registrados', children=[
                dcc.Loading(id="loading-2",children=[
                html.P(),
                html.Div(
                    dash_table.DataTable(
                        id="data-table-quipamentos",
                        columns=[{"name": "Nome", "id": "nome"}] + [
                            {"name": "Número de Série", "id": "numero_serie"}] + [
                            {"name": "Fabricante", "id": "fabricante"}] ,
                        data=[],
                        page_size=10,
                        style_cell={'minWidth': 95, 'maxWidth': 95,
                                    'width': 95, 'textAlign': 'center'},
                        style_table={'height': '450px'},
                        style_as_list_view=True,
                        row_selectable='multi',                
                    ),
                    style={'width': '100%', 'float': 'right'},
                ),

                html.P(),
                html.Div([
                    html.Div([
                        dbc.Button(id='btt_deletar_tudo_1',
                                n_clicks=0, children='Limpar Lista', color="primary"),
                        dbc.Button(id='btt_deletar_itens_1',
                                n_clicks=0, children='Remover Itens', color="primary"),
                    ], style={'float': 'right'}),
                    html.Div(id='id_delete_all_1'),                  
                ]),
                html.P(),
                ])
            ]),
            dcc.Tab(label='Chamadas Registrado', children=[
                html.P(),
                html.Div(
                    dash_table.DataTable(
                        id="data-table-chamado",
                        columns=[{"name": "Título do Chamado", "id": "titulo_chamado"}] + [
                            {"name": "Descrição do Chamado", "id": "descricao"}] + [
                            {"name": "Equipamento", "id": "equipamento"}] + [
                            {"name": "Data de Abertura", "id": "data_abertura"}] ,
                        data=[],
                        page_size=10,
                        style_cell={'minWidth': 95, 'maxWidth': 95,
                                    'width': 95, 'textAlign': 'center'},
                        style_table={'height': '450px'},
                        style_as_list_view=True,
                        row_selectable='multi',                
                    ),
                    style={'width': '100%', 'float': 'right'},
                ),

                html.P(),
                html.Div([
                    html.Div([
                        dbc.Button(id='btt_deletar_tudo_2',
                                n_clicks=0, children='Limpar Lista', color="primary"),
                        dbc.Button(id='btt_deletar_itens_2',
                                n_clicks=0, children='Remover Itens', color="primary"),
                    ], style={'float': 'right'}),
                    html.Div(id='id_delete_all_2'),                  
                ]),
                html.P(),
            ]),
        ])


    ],
    style={'width': '90%', 'float': 'right'}),
        
],
    style={'width': '60%', 'float': 'letf', 'display': 'inline-block'}
)

