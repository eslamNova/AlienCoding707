import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html 


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash Test'),
    html.Div(children='''Dash: A web application framework'''),
    dcc.Graph(id='example',
    figure={
        'data':[
            {'x':[1,2,3,4,5], 'y':[5,6,7,2,1], 'type':'line', 'name':'boats'},
            {'x':[1,2,3,4,5], 'y':[2,2,2,2,3], 'type':'bar', 'name':'cars'}
            ],
            'layout':{
                'title': 'basic dash example'
            }
        })
    ])

if __name__ == '__main__':
    app.run_server(debug= True)