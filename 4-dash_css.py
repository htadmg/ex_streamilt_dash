from dash import Dash, dcc, html

app = Dash()

app.layout = html.Div(
    children=[
        html.H1('testando dash com html'), 
        html.H2("text",
            style={
                'font-size':'50px',
                'color': 'blue'
            }
        ),
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
