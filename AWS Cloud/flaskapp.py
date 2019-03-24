# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import sqlite3
import datetime
from flask import Flask




server = Flask(__name__)
server.secret_key ='test'

#conn = sqlite3.connect('/home/ubuntu/flaskapp/agristick.db',check_same_thread=False)
#c = conn.cursor()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,server=server, external_stylesheets=external_stylesheets)


app.layout = html.Div(style={'backgroundColor': '#7CFC00'},children=[
    html.H1(
        children='Agri-Stick',
        style = {
                'textAlign':'center',
                'color' : '#000000'
        }),

    html.H2(children= 'A product for better farming',
        style={
                'textAlign':'center',
                'color': '#FFFFFF'
        }),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
                    id='interval-component',
            interval=1*3000, # in milliseconds
            n_intervals=3000
        )
        ])


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])

def update_graph_live(n_intervals):

    conn = sqlite3.connect('/home/ubuntu/flaskapp/agristick.db',check_same_thread=False)
    conn.execute('pragma journal_mode=wal;')
    c = conn.cursor()

    c.execute('SELECT * FROM DATASEN ORDER BY id DESC LIMIT 10 OFFSET 0')
    conn.commit()
    data = c.fetchall()
    conn.close()
    dts0 = data[9][1]
    dts1 = data[8][1]
    dts2 = data[7][1]
    dts3 = data[6][1]
    dts4 = data[5][1]
    dts5 = data[4][1]
    dts6 = data[3][1]
    dts7 = data[2][1]
    dts8 = data[1][1]
    dts9 = data[0][1]

    dt0 = datetime.datetime.strptime(dts0,'%Y-%m-%d %H:%M:%S.%f')
    dt1 = datetime.datetime.strptime(dts1,'%Y-%m-%d %H:%M:%S.%f')
    dt2 = datetime.datetime.strptime(dts2,'%Y-%m-%d %H:%M:%S.%f')
    dt3 = datetime.datetime.strptime(dts3,'%Y-%m-%d %H:%M:%S.%f')
    dt4 = datetime.datetime.strptime(dts4,'%Y-%m-%d %H:%M:%S.%f')
    dt5 = datetime.datetime.strptime(dts5,'%Y-%m-%d %H:%M:%S.%f')
    dt6 = datetime.datetime.strptime(dts6,'%Y-%m-%d %H:%M:%S.%f')
    dt7 = datetime.datetime.strptime(dts7,'%Y-%m-%d %H:%M:%S.%f')
    dt8 = datetime.datetime.strptime(dts8,'%Y-%m-%d %H:%M:%S.%f')
    dt8 = datetime.datetime.strptime(dts8,'%Y-%m-%d %H:%M:%S.%f')
    dt9 = datetime.datetime.strptime(dts9,'%Y-%m-%d %H:%M:%S.%f')


    soil_temp0 = data[9][2]
    soil_temp1 = data[8][2]
    soil_temp2 = data[7][2]
    soil_temp3 = data[6][2]
    soil_temp4 = data[5][2]
    soil_temp5 = data[4][2]
    soil_temp6 = data[3][2]
    soil_temp7 = data[2][2]
    soil_temp8 = data[1][2]
    soil_temp9 = data[0][2]

    soil_moist0 = data[9][3]
    soil_moist1 = data[8][3]
    soil_moist2 = data[7][3]
    soil_moist3 = data[6][3]
    soil_moist4 = data[5][3]
    soil_moist5 = data[4][3]
    soil_moist6 = data[3][3]
    soil_moist7 = data[2][3]
    soil_moist8 = data[1][3]
    soil_moist9 = data[0][3]

    air_temp0 = data[9][4]
    air_temp1 = data[8][4]
    air_temp2 = data[7][4]
    air_temp3 = data[6][4]
    air_temp4 = data[5][4]
    air_temp5 = data[4][4]
    air_temp6 = data[3][4]
    air_temp7 = data[2][4]
    air_temp8 = data[1][4]
    air_temp9 = data[0][4]

    air_hum0 = data[9][5]
    air_hum1 = data[8][5]
    air_hum2 = data[7][5]
    air_hum3 = data[6][5]
    air_hum4 = data[5][5]
    air_hum5 = data[4][5]
    air_hum6 = data[3][5]
    air_hum7 = data[2][5]
    air_hum8 = data[1][5]
    air_hum9 = data[0][5]


#===================================================================

    fig = plotly.tools.make_subplots(rows=2, cols=2,subplot_titles= ('Soil Temperature','Soil Moisture','Air Temperature','Air Humidity'), vertical_spacing=0.2)
    fig['layout']['margin'] = {
         'l':30 , 'r': 10, 'b': 20, 't': 20
     }
    fig['layout']['legend'] = {'x': 0.53, 'y': 1, 'xanchor': 'left'}


    fig.append_trace({
        'x': [dt0,dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9],
        'y': [soil_temp0,soil_temp1,soil_temp2,soil_temp3,soil_temp4,soil_temp5,soil_temp6,soil_temp7,soil_temp8,soil_temp9],
        'name': 'Soil Temp',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)

    fig.append_trace({
        'x': [dt0,dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9],
        'y': [soil_moist0,soil_moist1,soil_moist2,soil_moist3,soil_moist4,soil_moist5,soil_moist6,soil_moist7,soil_moist8,soil_moist9],
        'name': 'Soil Moist',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 2)

    fig.append_trace({
        'x': [dt0,dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9],
        'y': [air_temp0,air_temp1,air_temp2,air_temp3,air_temp4,air_temp5,air_temp6,air_temp7,air_temp8,air_temp9],
        'name': 'Air Temp',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 2, 1)

    fig.append_trace({
        'x': [dt0,dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9],
        'y': [air_hum0,air_hum1,air_hum2,air_hum3,air_hum4,air_hum5,air_hum6,air_hum7,air_hum8,air_hum9],
        'name': 'Air Humid',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 2, 2)

    fig['layout']['yaxis1'].update(range=[25,35])
    fig['layout']['yaxis2'].update(range=[400,800])
    fig['layout']['yaxis3'].update(range=[25,45])
    fig['layout']['yaxis4'].update(range=[20,80])


    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

