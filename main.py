import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from datetime import date


mydata = pd.read_csv('../data/senegal.csv')
senegalData = mydata[['location','date','total_cases','new_cases','total_deaths','new_deaths','total_tests','new_tests','population','median_age','aged_65_older','aged_70_older']]
mydata1 = pd.read_csv('../data/mali.csv')
maliData = mydata1[['location','date','total_cases','new_cases','total_deaths','new_deaths','total_tests','new_tests','population','median_age','aged_65_older','aged_70_older']]
mydata2 = pd.read_csv('../data/gabon.csv')
gabonData = mydata2[['location','date','total_cases','new_cases','total_deaths','new_deaths','total_tests','new_tests','population','median_age','aged_65_older','aged_70_older']]
mydata3 = pd.read_csv('../data/benin.csv')
beninData = mydata3[['location','date','total_cases','new_cases','total_deaths','new_deaths','total_tests','new_tests','population','median_age','aged_65_older','aged_70_older']]
mydata4 = pd.read_csv('../data/burkina_faso.csv')
others = pd.read_csv('../data/others.csv')
burkina_fasoData = mydata4[['location','date','total_cases','new_cases','total_deaths','new_deaths','total_tests','new_tests','population','median_age','aged_65_older','aged_70_older']]

benin = beninData[:].iloc[-1]
senegal = senegalData[:].iloc[-1]
gabon = gabonData[:].iloc[-1]
mali = maliData[:].iloc[-1]
burkina = burkina_fasoData[:].iloc[-1]
nouveau_cas = (benin.fillna(0))["new_cases"]+(burkina.fillna(0))["new_cases"]+(mali.fillna(0))["new_cases"]+(senegal.fillna(0))["new_cases"]+(gabon.fillna(0))["new_cases"]
nouveau_decces = (benin.fillna(0))["new_deaths"]+(burkina.fillna(0))["new_deaths"]+(mali.fillna(0))["new_deaths"]+(senegal.fillna(0))["new_deaths"]+(gabon.fillna(0))["new_deaths"]
total_test = (benin.fillna(0))["total_tests"]+(burkina.fillna(0))["total_tests"]+(mali.fillna(0))["total_tests"]+(senegal.fillna(0))["total_tests"]+(gabon.fillna(0))["total_tests"]
nouveau_test = (benin.fillna(0))["new_tests"]+(burkina.fillna(0))["new_tests"]+(mali.fillna(0))["new_tests"]+(senegal.fillna(0))["new_tests"]+(gabon.fillna(0))["new_tests"]
total_cas = (benin.fillna(0))["total_cases"]+(burkina.fillna(0))["total_cases"]+(mali.fillna(0))["total_cases"]+(senegal.fillna(0))["total_cases"]+(gabon.fillna(0))["total_cases"]
total_decces = (benin.fillna(0))["total_deaths"]+(burkina.fillna(0))["total_deaths"]+(mali.fillna(0))["total_deaths"]+(senegal.fillna(0))["total_deaths"]+(gabon.fillna(0))["total_deaths"]
test = 0
if nouveau_test <= total_test:
    test = nouveau_test
else:
    test = total_test

def date_conv(madate):
    newDate=""
    if "January" in madate:
        newDate = madate.replace("January","Janvier")
    if "February" in madate:
        newDate = madate.replace("February","Fevrier")
    if "March" in madate:
        newDate = madate.replace("March","Mars")
    if "April" in madate:
        newDate = madate.replace("April","Avril")
    if "May" in madate:
        newDate = madate.replace("May","Mai")
    if "June" in madate:
        newDate = madate.replace("June","Juin")
    if "July" in madate:
        newDate = madate.replace("July","Juillet")
    if "August" in madate:
        newDate = madate.replace("August","Aout")
    if "September" in madate:
        newDate = madate.replace("September","Septembre")
    if "October" in madate:
        newDate = madate.replace("October","Octobre")
    if "November" in madate:
        newDate = madate.replace("November","Novembre")
    if "December" in madate:
        newDate = madate.replace("December","Décembre")
    return newDate


senegalData['casParMillion']=senegalData['total_cases']/senegalData['population']
gabonData['casParMillion']=gabonData['total_cases']/gabonData['population']
maliData['casParMillion']=maliData['total_cases']/maliData['population']
burkina_fasoData['casParMillion']=burkina_fasoData['total_cases']/burkina_fasoData['population']
beninData['casParMillion']=beninData['total_cases']/beninData['population']

senegalData['deccesParMillion']=senegalData['total_deaths']/senegalData['population']
gabonData['deccesParMillion']=gabonData['total_deaths']/gabonData['population']
maliData['deccesParMillion']=maliData['total_deaths']/maliData['population']
burkina_fasoData['deccesParMillion']=burkina_fasoData['total_deaths']/burkina_fasoData['population']
beninData['deccesParMillion']=beninData['total_deaths']/beninData['population']

burundi = others.loc[others['location']=='Burundi'].iloc[-1]
camer = others.loc[others['location']=='Cameroon'].iloc[-1]
camer['location'] = camer['location'].replace('Cameroon','Cameroun')
rca = others.loc[others['location']=='Central African Republic'].iloc[-1]
rca['location'] = rca['location'].replace('Central African Republic','Centrafrique')
congo = others.loc[others['location']=='Congo'].iloc[-1]
ivoir = others.loc[others['location']=="Cote d'Ivoire"].iloc[-1]
guinee = others.loc[others['location']=="Guinea"].iloc[-1]
guinee['location'] = guinee['location'].replace('Guinea','Guinee')
guineeB = others.loc[others['location']=="Guinea-Bissau"].iloc[-1]
guineeB['location'] = guineeB['location'].replace('Guinea-Bissau','Guinee-Bissau')
madagascar = others.loc[others['location']=="Madagascar"].iloc[-1]
niger = others.loc[others['location']=="Niger"].iloc[-1]
rdc = others.loc[others['location']=="Democratic Republic of Congo"].iloc[-1]
rdc['location'] = rdc['location'].replace('Democratic Republic of Congo','R. D. Congo')
equatorial = others.loc[others['location']=="Equatorial Guinea"].iloc[-1]
equatorial['location'] = equatorial['location'].replace('Equatorial Guinea','Guinee Equatoriale')
rwanda = others.loc[others['location']=="Rwanda"].iloc[-1]
togo = others.loc[others['location']=="Togo"].iloc[-1]
tchad = others.loc[others['location']=="Chad"].iloc[-1]
tchad['location'] = tchad['location'].replace('Chad','Tchad')

iso = ['SEN','BEN','GAB','MLI','BFA','BDI','CMR','CAF','COG','CIV','GIN','GNB','MDG','NER','COD','GNQ','RWA','TGO','TCD']
colors = [mydata.loc[:,'total_cases'].iloc[-1],mydata3.loc[:,'total_cases'].iloc[-1],mydata2.loc[:,'total_cases'].iloc[-1],mydata1.loc[:,'total_cases'].iloc[-1],mydata4.loc[:,'total_cases'].iloc[-1],burundi.loc['total_cases'],camer.loc['total_cases'],rca.loc['total_cases'],congo.loc['total_cases'],ivoir.loc['total_cases'],guinee.loc['total_cases'],guineeB.loc['total_cases'],madagascar.loc['total_cases'],niger.loc['total_cases'],rdc.loc['total_cases'],equatorial.loc['total_cases'],rwanda.loc['total_cases'],togo.loc['total_cases'],tchad.loc['total_cases']]

text = [
    '<b>Pays</b>: ' + mydata.loc[:, 'location'].iloc[-1] + '<br>' + '<b>Nouveaux Cas</b>: ' + mydata.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + mydata.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +'<b>Nouveaux Tests</b>: ' + mydata.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + mydata.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +'<b>Total Décès</b>: ' + mydata.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + mydata3.loc[:, 'location'].iloc[-1] + '<br>' +'<b>Nouveaux Cas</b>: ' + mydata3.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + mydata3.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +'<b>Nouveaux Tests</b>: ' + mydata3.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + mydata3.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +'<b>Total Décès</b>: ' + mydata3.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + mydata2.loc[:, 'location'].iloc[-1] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + mydata2.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + mydata2.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Tests</b>: ' + mydata2.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + mydata2.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Décès</b>: ' + mydata2.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + mydata1.loc[:, 'location'].iloc[-1] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + mydata1.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + mydata1.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Tests</b>: ' + mydata1.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + mydata1.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Décès</b>: ' + mydata1.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + mydata4.loc[:, 'location'].iloc[-1] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + mydata4.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + mydata4.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Tests</b>: ' + mydata4.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + mydata4.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Décès</b>: ' + mydata4.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + burundi.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(burundi.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(burundi.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(burundi.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(burundi.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(burundi.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + camer.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(camer.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(camer.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(camer.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(camer.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(camer.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + rca.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(rca.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(rca.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(rca.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(rca.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(rca.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + congo.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(congo.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(congo.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(congo.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(congo.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(congo.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + ivoir.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(ivoir.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(ivoir.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(ivoir.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(ivoir.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(ivoir.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + guinee.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(guinee.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(guinee.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(guinee.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(guinee.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(guinee.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + guineeB.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(guineeB.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(guineeB.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(guineeB.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(guineeB.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(guineeB.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + madagascar.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(madagascar.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(madagascar.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(madagascar.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(madagascar.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(madagascar.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + niger.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(niger.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(niger.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(niger.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(niger.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(niger.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + rdc.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(rdc.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(rdc.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(rdc.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(rdc.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(rdc.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + equatorial.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(equatorial.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(equatorial.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(equatorial.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(equatorial.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(equatorial.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + rwanda.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(rwanda.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(rwanda.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(rwanda.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(rwanda.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(rwanda.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + togo.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(togo.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(togo.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(togo.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(togo.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(togo.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + tchad.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(tchad.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(tchad.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(tchad.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(tchad.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(tchad.loc['total_deaths']) + '<br>'
    ]
# senegalData['casParMillion']=senegalData['total_cases']/senegalData['population']
# gabonData['casParMillion']=gabonData['total_cases']/gabonData['population']
# maliData['casParMillion']=maliData['total_cases']/maliData['population']
# burkina_fasoData['casParMillion']=burkina_fasoData['total_cases']/burkina_fasoData['population']
# beninData['casParMillion']=beninData['total_cases']/beninData['population']


fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=senegalData['date'].tail(10), y=senegalData['total_cases'].tail(10),mode='lines+markers',name='Senegal'))
fig1.add_trace(go.Scatter(x=maliData['date'].tail(10), y=maliData['total_cases'].tail(10),mode='lines+markers',name='Mali'))
fig1.add_trace(go.Scatter(x=gabonData['date'].tail(10), y=gabonData['total_cases'].tail(10),mode='lines+markers',name='Gabon'))
fig1.add_trace(go.Scatter(x=beninData['date'].tail(10), y=beninData['total_cases'].tail(10),mode='lines+markers',name='Benin'))
fig1.add_trace(go.Scatter(x=burkina_fasoData['date'].tail(10), y=burkina_fasoData['total_cases'].tail(10),mode='lines+markers',name='Burkina Faso'))

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=senegalData['date'].tail(10), y=senegalData['casParMillion'].tail(10),mode='lines+markers',name='Senegal'))
fig2.add_trace(go.Scatter(x=maliData['date'].tail(10), y=maliData['casParMillion'].tail(10),mode='lines+markers',name='Mali'))
fig2.add_trace(go.Scatter(x=gabonData['date'].tail(10), y=gabonData['casParMillion'].tail(10),mode='lines+markers',name='Gabon'))
fig2.add_trace(go.Scatter(x=beninData['date'].tail(10), y=beninData['casParMillion'].tail(10),mode='lines+markers',name='Benin'))
fig2.add_trace(go.Scatter(x=burkina_fasoData['date'].tail(10), y=burkina_fasoData['casParMillion'].tail(10),mode='lines+markers',name='Burkina Faso'))

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=senegalData['date'].tail(10), y=senegalData['deccesParMillion'].tail(10),mode='lines+markers',name='Senegal'))
fig3.add_trace(go.Scatter(x=maliData['date'].tail(10), y=maliData['deccesParMillion'].tail(10),mode='lines+markers',name='Mali'))
fig3.add_trace(go.Scatter(x=gabonData['date'].tail(10), y=gabonData['deccesParMillion'].tail(10),mode='lines+markers',name='Gabon'))
fig3.add_trace(go.Scatter(x=beninData['date'].tail(10), y=beninData['deccesParMillion'].tail(10),mode='lines+markers',name='Benin'))
fig3.add_trace(go.Scatter(x=burkina_fasoData['date'].tail(10), y=burkina_fasoData['deccesParMillion'].tail(10),mode='lines+markers',name='Burkina Faso'))


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('corona-logo-1.jpg'),
                     id='corona-image',
                     style={
                         "height": "60px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
                     )
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Covid - 19", style={"margin-bottom": "0px", 'color': 'white'}),
                html.H5("Pays Pilotes du Projet Also_Covid 19", style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title"),

        html.Div([
            html.H6('Dernière mis a jour: ' + date_conv(str(pd.to_datetime(senegalData['date']).iloc[-1].strftime("%B %d, %Y"))) + '  00:01 (UTC)',
                    style={'color': 'orange'}),

        ], className="one-third column", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        html.Div([
            html.H6(children='Nouveaux Cas',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{nouveau_cas:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40}
                   ),

        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Nouveaux Décès',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{nouveau_decces:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 40}
                   ),

        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Nouveaux Tests',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{test:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 40}
                   ),

        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Total Cas',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{total_cas:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 40}
                   ),

                   ], className="card_container three columns"),

        html.Div([
            html.H6(children='Total Décès',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{total_decces:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 40}
                   ),

                   ], className="card_container three columns")

    ], className="row flex-display"),

html.Div([
        html.Div([
            dcc.Graph(id="my-graph",
                  figure= {
                    "data": [
                        go.Choropleth(locations=iso,
                                      #code_df.loc[:,'COUNTRY'].iloc[-1]
                                      z=colors,
                                      text=text,
                                      hoverinfo="text",
                                      marker_line_color='white',
                                      autocolorscale=True,
                                      #colorbar_title = "Total de cas",
                                      reversescale=True,
                                      #colorscale="Rainbow",
                                      marker={'line': {'color': 'rgb(180,180,180)','width': 0.5}},
                                      colorbar={#"thickness": 10,"len": 0.3,"x": 0.9,"y": 0.7,
                                                #'tickvals': [ min(colors), max(colors)],
                                                #'ticktext': [str(min(colors)), str(max(colors))]
                                                'title':"<b> Total de Cas </b>"
                                                }
                        )
                    ],
                    "layout": go.Layout( height=700,width=1000,geo= { 'scope': "africa"},paper_bgcolor = '#191d40',margin={'t': 10,'b':10,'l':10,'r':10})#height=800,geo={'showframe': True,'showcoastlines': False,
                                                                              #'projection': {'type': "miller"}})
                  }
            )
        ],style={'width':1000,"margin-right": "auto","margin-left": "auto","text-align": "center"}

            )
#margin-left: auto;
  #margin-right: auto;

#['world', 'usa', 'europe', 'asia', 'africa', 'north america', 'south america']
    ],style={'backgroundColor': "#191d40","margin-bottom": "25px","margin-top": "25px",'fontSize': 20,"text-align": "center"}

    ),

html.Div([
    html.Div([
        html.Div([
            html.H6(children="Niveau d'agregation ", style={'color': 'white'}),
            dcc.RadioItems(
                id='aggregation',
                options=[
                    {'label': 'Jour', 'value': 'jour'},
                    {'label': 'Semaine', 'value': 'semaine'},
                    {'label': 'Mois', 'value': 'mois'},
                    {'label': 'Annee', 'value': 'annee'}
                ],
                value='jour',
                style={'color': 'white'}

            ),
            html.Div([
                html.H6(children="Etendu de visibilité", style={'color': 'white'}),
                dcc.Slider(
                    id='taille_aff',
                    min=10,
                    max=len(senegalData['date']),
                    value=10,
                    marks={str(year): str(year) for year in [(x * 10) + 10 for x in range(len(senegalData['date'])) if
                                                             (x * 10) + 10 <= len(senegalData['date'])]},
                    step=None
                )
            ]),

        ]),
    ], style={'backgroundColor': "#191d40", "margin-bottom": "30px"}  # className="row flex-display"
    )
    ,html.Div([
        html.H6(children="EVOLUTION DE NOUVEAUX CAS",
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
        dcc.Graph(
            id='example-graph1',
            figure=fig1
        )
    ]#, className="create_container four columns"
    ),
    html.Div([
            html.H6(children="EVOLUTION DE TOTAL DE CAS PAR MILLION D'HABITANTS",
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            dcc.Graph(
                id='example-graph2',
                figure=fig2
            )
    ]#, className="create_container four columns"
    ),
    html.Div([
        html.H6(children="EVOLUTION DE TOTAL DECES PAR MILLION D'HABITANTS",
                style={
                    'textAlign': 'center',
                    'color': 'white'}
                ),

        dcc.Graph(
            id='example-graph3',
            figure=fig3
        )
    ]#, className="create_container four columns"
    )

 ]#,className="row flex-display"
)

    ], id="mainContainer",
    style={"display": "flex", "flex-direction": "column"}
)


@app.callback(
    Output('example-graph1', 'figure'),
    Output('example-graph2', 'figure'),
    Output('example-graph3', 'figure'),
    Input('taille_aff', 'value'),
    Input('aggregation', 'value'),
    #Input('typeJour', 'value')
    )
def update_figure(taille_aff,aggregation):
    newData = pd.DataFrame(senegalData)
    newData1 = pd.DataFrame(beninData)
    newData2 = pd.DataFrame(maliData)
    newData3 = pd.DataFrame(gabonData)
    newData4 = pd.DataFrame(burkina_fasoData)
    newData = initialData(newData)
    newData1 = initialData(newData1)
    newData2 = initialData(newData2)
    newData3 = initialData(newData3)
    newData4 = initialData(newData4)

    fig1 = go.Figure()
    fig2 = go.Figure()
    fig3 = go.Figure()


    if aggregation == "jour":
        fig1.add_trace(go.Scatter(x=newData['date'].tail(taille_aff), y=newData['total_cases'].tail(taille_aff), mode='lines+markers',name='Senegal'))
        fig1.add_trace(go.Scatter(x=newData2['date'].tail(taille_aff), y=newData2['total_cases'].tail(taille_aff), mode='lines+markers',name='Mali'))
        fig1.add_trace(go.Scatter(x=newData3['date'].tail(taille_aff), y=newData3['total_cases'].tail(taille_aff), mode='lines+markers', name='Gabon'))
        fig1.add_trace(go.Scatter(x=newData1['date'].tail(taille_aff), y=newData1['total_cases'].tail(taille_aff), mode='lines+markers', name='Benin'))
        fig1.add_trace(go.Scatter(x=newData4['date'].tail(taille_aff), y=newData4['total_cases'].tail(taille_aff), mode='lines+markers', name='Burkina Faso'))

        fig2.add_trace(go.Scatter(x=newData['date'].tail(taille_aff), y=newData['casParMillion'].tail(taille_aff), mode='lines+markers', name='Senegal'))
        fig2.add_trace( go.Scatter(x=newData2['date'].tail(taille_aff), y=newData2['casParMillion'].tail(taille_aff), mode='lines+markers', name='Mali'))
        fig2.add_trace( go.Scatter(x=newData3['date'].tail(taille_aff), y=newData3['casParMillion'].tail(taille_aff), mode='lines+markers', name='Gabon'))
        fig2.add_trace( go.Scatter(x=newData1['date'].tail(taille_aff), y=newData1['casParMillion'].tail(taille_aff), mode='lines+markers', name='Benin'))
        fig2.add_trace(go.Scatter(x=newData4['date'].tail(taille_aff), y=newData4['casParMillion'].tail(taille_aff), mode='lines+markers', name='Burkina Faso'))

        fig3.add_trace(go.Scatter(x=newData['date'].tail(taille_aff), y=newData['deccesParMillion'].tail(taille_aff), mode='lines+markers', name='Senegal'))
        fig3.add_trace( go.Scatter(x=newData2['date'].tail(taille_aff), y=newData2['deccesParMillion'].tail(taille_aff), mode='lines+markers', name='Mali'))
        fig3.add_trace( go.Scatter(x=newData3['date'].tail(taille_aff), y=newData3['deccesParMillion'].tail(taille_aff), mode='lines+markers', name='Gabon'))
        fig3.add_trace( go.Scatter(x=newData1['date'].tail(taille_aff), y=newData1['deccesParMillion'].tail(taille_aff), mode='lines+markers', name='Benin'))
        fig3.add_trace(go.Scatter(x=newData4['date'].tail(taille_aff), y=newData4['deccesParMillion'].tail(taille_aff), mode='lines+markers', name='Burkina Faso'))

    elif aggregation == "semaine":
        newData = newData.groupby(['annee','semaine']).sum()
        newData2 = newData2.groupby(['annee', 'semaine']).sum()
        newData3 = newData3.groupby(['annee', 'semaine']).sum()
        newData1 = newData1.groupby(['annee', 'semaine']).sum()
        newData4 = newData4.groupby(['annee', 'semaine']).sum()
        newData['semaine']=get_axis(newData)
        newData2['semaine'] = get_axis(newData2)
        newData3['semaine'] = get_axis(newData3)
        newData1['semaine'] = get_axis(newData1)
        newData4['semaine'] = get_axis(newData4)


        fig1.add_trace(go.Scatter(x=newData['semaine'].tail(taille_aff), y=newData['new_cases'].tail(taille_aff),mode='lines+markers', name='Senegal'))
        fig1.add_trace(go.Scatter(x=newData2['semaine'].tail(taille_aff), y=newData2['new_cases'].tail(taille_aff),mode='lines+markers', name='Mali'))
        fig1.add_trace(go.Scatter(x=newData3['semaine'].tail(taille_aff), y=newData3['new_cases'].tail(taille_aff),mode='lines+markers', name='Gabon'))
        fig1.add_trace(go.Scatter(x=newData1['semaine'].tail(taille_aff), y=newData1['new_cases'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig1.add_trace(go.Scatter(x=newData4['semaine'].tail(taille_aff), y=newData4['new_cases'].tail(taille_aff), mode='lines+markers', name='Burkina Faso'))

        fig2.add_trace(go.Scatter(x=newData['semaine'].tail(taille_aff), y=newData['casParMillion'].tail(taille_aff),mode='lines+markers', name='Senegal'))
        fig2.add_trace(go.Scatter(x=newData2['semaine'].tail(taille_aff), y=newData2['casParMillion'].tail(taille_aff), mode='lines+markers', name='Mali'))
        fig2.add_trace(go.Scatter(x=newData3['semaine'].tail(taille_aff), y=newData3['casParMillion'].tail(taille_aff),mode='lines+markers', name='Gabon'))
        fig2.add_trace(go.Scatter(x=newData1['semaine'].tail(taille_aff), y=newData1['casParMillion'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig2.add_trace(go.Scatter(x=newData4['semaine'].tail(taille_aff), y=newData4['casParMillion'].tail(taille_aff), mode='lines+markers', name='Burkina Faso'))

        fig3.add_trace(go.Scatter(x=newData['semaine'].tail(taille_aff), y=newData['deccesParMillion'].tail(taille_aff), mode='lines+markers', name='Senegal'))
        fig3.add_trace(go.Scatter(x=newData2['semaine'].tail(taille_aff), y=newData2['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Mali'))
        fig3.add_trace(go.Scatter(x=newData3['semaine'].tail(taille_aff), y=newData3['deccesParMillion'].tail(taille_aff), mode='lines+markers', name='Gabon'))
        fig3.add_trace(go.Scatter(x=newData1['semaine'].tail(taille_aff), y=newData1['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig3.add_trace(go.Scatter(x=newData4['semaine'].tail(taille_aff), y=newData4['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Burkina Faso'))


    elif aggregation == "mois":
        newData = newData.groupby(['annee', 'mois']).sum()
        newData2 = newData2.groupby(['annee', 'mois']).sum()
        newData3 = newData3.groupby(['annee', 'mois']).sum()
        newData1 = newData1.groupby(['annee', 'mois']).sum()
        newData4 = newData4.groupby(['annee', 'mois']).sum()
        newData['mois'] = get_axis(newData)
        newData2['mois'] = get_axis(newData2)
        newData3['mois'] = get_axis(newData3)
        newData1['mois'] = get_axis(newData1)
        newData4['mois'] = get_axis(newData4)

        fig1.add_trace(go.Scatter(x=newData['mois'].tail(taille_aff), y=newData['new_cases'].tail(taille_aff), mode='lines+markers', name='Senegal'))
        fig1.add_trace(go.Scatter(x=newData2['mois'].tail(taille_aff), y=newData2['new_cases'].tail(taille_aff),mode='lines+markers', name='Mali'))
        fig1.add_trace(go.Scatter(x=newData3['mois'].tail(taille_aff), y=newData3['new_cases'].tail(taille_aff),mode='lines+markers', name='Gabon'))
        fig1.add_trace(go.Scatter(x=newData1['mois'].tail(taille_aff), y=newData1['new_cases'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig1.add_trace(go.Scatter(x=newData4['mois'].tail(taille_aff), y=newData4['new_cases'].tail(taille_aff),mode='lines+markers', name='Burkina Faso'))

        fig2.add_trace(go.Scatter(x=newData['mois'].tail(taille_aff), y=newData['casParMillion'].tail(taille_aff),mode='lines+markers', name='Senegal'))
        fig2.add_trace(go.Scatter(x=newData2['mois'].tail(taille_aff), y=newData2['casParMillion'].tail(taille_aff),mode='lines+markers', name='Mali'))
        fig2.add_trace(go.Scatter(x=newData3['mois'].tail(taille_aff), y=newData3['casParMillion'].tail(taille_aff),mode='lines+markers', name='Gabon'))
        fig2.add_trace(go.Scatter(x=newData1['mois'].tail(taille_aff), y=newData1['casParMillion'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig2.add_trace(go.Scatter(x=newData4['mois'].tail(taille_aff), y=newData4['casParMillion'].tail(taille_aff),mode='lines+markers', name='Burkina Faso'))

        fig3.add_trace(go.Scatter(x=newData['mois'].tail(taille_aff), y=newData['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Senegal'))
        fig3.add_trace(go.Scatter(x=newData2['mois'].tail(taille_aff), y=newData2['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Mali'))
        fig3.add_trace(go.Scatter(x=newData3['mois'].tail(taille_aff), y=newData3['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Gabon'))
        fig3.add_trace(go.Scatter(x=newData1['mois'].tail(taille_aff), y=newData1['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig3.add_trace(go.Scatter(x=newData4['mois'].tail(taille_aff), y=newData4['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Burkina Faso'))

    elif aggregation == "annee":
        newData = newData.groupby(['annee']).sum()
        newData2 = newData2.groupby(['annee']).sum()
        newData3 = newData3.groupby(['annee']).sum()
        newData1 = newData1.groupby(['annee']).sum()
        newData4 = newData4.groupby(['annee']).sum()
        newData['annee'] = get_axis(newData)
        newData2['annee'] = get_axis(newData2)
        newData3['annee'] = get_axis(newData3)
        newData1['annee'] = get_axis(newData1)
        newData4['annee'] = get_axis(newData4)

        fig1.add_trace(go.Scatter(x=newData['annee'].tail(taille_aff), y=newData['new_cases'].tail(taille_aff),mode='lines+markers', name='Senegal'))
        fig1.add_trace(go.Scatter(x=newData2['annee'].tail(taille_aff), y=newData2['new_cases'].tail(taille_aff),mode='lines+markers', name='Mali'))
        fig1.add_trace(go.Scatter(x=newData3['annee'].tail(taille_aff), y=newData3['new_cases'].tail(taille_aff),mode='lines+markers', name='Gabon'))
        fig1.add_trace(go.Scatter(x=newData1['annee'].tail(taille_aff), y=newData1['new_cases'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig1.add_trace(go.Scatter(x=newData4['annee'].tail(taille_aff), y=newData4['new_cases'].tail(taille_aff),mode='lines+markers', name='Burkina Faso'))

        fig2.add_trace(go.Scatter(x=newData['annee'].tail(taille_aff), y=newData['casParMillion'].tail(taille_aff),mode='lines+markers', name='Senegal'))
        fig2.add_trace(go.Scatter(x=newData2['annee'].tail(taille_aff), y=newData2['casParMillion'].tail(taille_aff),mode='lines+markers', name='Mali'))
        fig2.add_trace(go.Scatter(x=newData3['annee'].tail(taille_aff), y=newData3['casParMillion'].tail(taille_aff),mode='lines+markers', name='Gabon'))
        fig2.add_trace(go.Scatter(x=newData1['annee'].tail(taille_aff), y=newData1['casParMillion'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig2.add_trace(go.Scatter(x=newData4['annee'].tail(taille_aff), y=newData4['casParMillion'].tail(taille_aff),mode='lines+markers', name='Burkina Faso'))

        fig3.add_trace(go.Scatter(x=newData['annee'].tail(taille_aff), y=newData['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Senegal'))
        fig3.add_trace(go.Scatter(x=newData2['annee'].tail(taille_aff), y=newData2['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Mali'))
        fig3.add_trace(go.Scatter(x=newData3['annee'].tail(taille_aff), y=newData3['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Gabon'))
        fig3.add_trace(go.Scatter(x=newData1['annee'].tail(taille_aff), y=newData1['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Benin'))
        fig3.add_trace(go.Scatter(x=newData4['annee'].tail(taille_aff), y=newData4['deccesParMillion'].tail(taille_aff),mode='lines+markers', name='Burkina Faso'))

    return fig1,fig2,fig3

def liste_date(annees,mois,jours):
    mes_date = []
    mesAnnee= list(annees)
    mesMois= list(mois)
    mesJours = list(jours)
    i=0
    while i< len(mesAnnee):
        mes_date.append((mesAnnee[i],mesMois[i],mesJours[i]))
        i=i+1
    return mes_date

def initialData(data):
    data['annee'] = data['date'].apply(lambda x: (pd.to_datetime(x)).year)
    data['mois'] = data['date'].apply(lambda x: (pd.to_datetime(x)).month)
    data['day'] = data['date'].apply(lambda x: (pd.to_datetime(x)).day)
    data['jour'] = [date(x, y, z).isocalendar() for (x, y, z) in liste_date(data['annee'], data['mois'], data['day'])]
    data['semaine'] = data['jour'].apply(lambda x: x[1])
    data['journee'] = data['jour'].apply(lambda x: x[2])
    return data

def get_axis(mesDonnee):
    liste_nom=[]
    for i in range(len(mesDonnee)):
        liste_nom.append(str(mesDonnee.iloc[i,].name))
    return liste_nom


if __name__ == '__main__':
    app.run_server(debug=False,port=8050)
