import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

app = Dash()


# 1- criando nosso dataframe
df = pd.DataFrame({
    'Fruits': ['Maça', 'Laranja', 'Melão', 'Laranja', 'Uva', 'Melão' ],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['Gramado', 'São Luís', 'Gramado', 'São Luís', 'Curitiba', 'Curitiba']
})

# 2- Criando graficos
fig = px.bar(
    df,
    x='Fruits',
    y='Amount',
    color='City',
    barmode='group'
)

# 3- criando o Dashboard
app.layout = html.Div(
    children=[
        html.H1('Hello Dash'), 
        html.Div(
            children=[
                '''
                    Dash
                '''
            ]
        ),
        dcc.Graph(
            id='emaple-graph',
            figure=fig
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

    