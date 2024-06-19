import dash
import dash_bootstrap_components as dbc
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# List of dashboard URLs and their titles
dashboard_urls = [
    {"title": "Survey Dashboard", "url": "https://survey-dash1-7kv2sru2jx36mk3qrwdr2d.streamlit.app/"},
    {"title": "App Card Dashboard", "url": "https://app-card-dash-gfrsvbpbw67oqz8man8phw.streamlit.app/"}
]

# Function to create a tile for each dashboard
def create_tile(title, url):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H5(title, className="card-title"),
                dbc.Button("Go to Dashboard", href=url, color="primary"),
            ]
        ),
        style={"width": "18rem", "margin": "1rem"},
    )

# Create the layout with tiles
app.layout = dbc.Container(
    [
        dbc.Row(
            [dbc.Col(create_tile(d['title'], d['url']), width=4) for d in dashboard_urls],
            justify="center",
        )
    ],
    fluid=True,
    className="mt-4",
)

# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)
