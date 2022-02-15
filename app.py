from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


# Read in data
df = data.countries()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='n_fertility',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in df.select_dtypes('number').columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(df).mark_point().encode(
        x=xcol,
        y='life_expect',
        color='country').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)