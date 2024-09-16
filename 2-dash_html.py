import dash
from dash import dcc, html
from datetime import datetime

app = dash.Dash()
app.layout = html.Div(
    children=[
        html.Img(src="https://github.com/htadmg.png"),
        html.Hr(),
        html.H1('Testando'),
        html.Span(
            children=[
                f'hoje é {datetime.now().date()}',
                html.Br(),
                'Desenvolvido por', html.B(' Agata Domingues'),
                html.Br(),
                html.I('sdfhisdufhisudh')
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)