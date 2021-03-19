import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# ---------------------------------
# LAYOUT GERAL
# ---------------------------------
layout = html.Div([
    html.Div([
        html.P(),
        html.Div([
            html.H4("Controle de Equipamentos"),
        ],
        style={'width': '91%', 'float': 'right'}),

        html.Div([
            html.P(),
            dbc.Row([
                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Nome", html_for="nome"),
                        dbc.Input(
                            type="textAlign",
                            id="name",
                            placeholder="Ex: Nome do equipamento",
                        ),
                ]), width=12,),

                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Preço", html_for="preco"),
                        dbc.Input(
                            type="number",
                            id="preco",
                            placeholder="Ex: 200,00",
                            min=1,
                        ),
                ]), width=6,),

                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Data de Fabricação", html_for="data_fabricacao"),
                        dbc.Input(
                            type="date",
                            id="data_fabricacao",
                        ),
                ]), width=6,),

                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Número de Série", html_for="numero_serie"),
                        dbc.Input(
                            type="textAlign",
                            id="numero_serie",
                            placeholder="Ex: ZA72282190",
                        ),
                ]), width=12,),

                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Fabricante", html_for="fabricante"),
                        dbc.Input(
                            type="textAlign",
                            id="fabricante",
                            placeholder="Ex: Fabricante",
                        ),
                ]), width=12,),


                ],
                form=True,
            ),
            html.Div([
                html.Div([
                    dbc.Button(id='btt_salvar_equipamentos', color="primary",
                            n_clicks=0, children='Salvar'),
                    html.Div(id='output-state-1')
                ], style={'width': '19,5%', 'float': 'right'}),
                html.Div(id='id-div-1')
            ]),

        ],
            style={'width': '92%', 'float': 'right'}),
    ]),
    html.Div([
        html.P(),
        html.Div([
            html.H4("Controle de Chamadas"),
        ],
        style={'width': '91%', 'float': 'right'}),

        html.Div([
            html.P(),
            dbc.Row([
                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Título do Chamado", html_for="titulo"),
                        dbc.Input(
                            type="textAlign",
                            id="titulo",
                            placeholder="Ex: Título do chamado",
                        ),
                ]), width=12,),

                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Descrição do Chamado", html_for="chamado"),
                        dbc.Input(
                            type="textAlign",
                            id="chamado",
                            placeholder="Ex: Descrição do chamado",
                        ),
                ]), width=12,),

                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Equipamento", html_for="equipamento"),
                        dbc.Input(
                            type="textAlign",
                            id="equipamento",
                            placeholder="Ex: Equipamento",
                        ),
                ]), width=6,),

                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label(
                            "Data de Abertura", html_for="data_abertura"),
                        dbc.Input(
                            type="date",
                            id="data_abertura",
                        ),
                ]), width=6,),

                ],
                form=True,
            ),
            html.Div([
                html.Div([
                    dbc.Button(id='btt_salvar_chamado', color="primary",
                            n_clicks=0, children='Salvar'),
                    html.Div(id='output-state-2')
                ], style={'width': '19,5%', 'float': 'right'}),
                html.Div(id='id-div-2')
            ]),
            html.P(),

        ],
            style={'width': '92%', 'float': 'right'}),
    ]),
],
    style={'width': '36%', 'float': 'left', 'display': 'inline-block'}
)

# color:"#DBD2B2"
