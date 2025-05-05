import dash
from dash import html, dcc
import plotly.graph_objs as go

app = dash.Dash(__name__)

app.layout = html.Div([
    # Sidebar
    html.Div(className="sidebar", children=[
        html.H2("Menu"),
        html.Ul([
            html.Li("Overview"),
            html.Li("Assets"),
            html.Li("Reports"),
            html.Li("Settings")
        ])
    ], style={"width": "15%", "float": "left"}),

    # Main content
    html.Div(style={"marginLeft": "15%"}, children=[

        # Filter and header section
        html.Div(className="dark-section", children=[
            html.H1("Vulnerability overview"),
            html.Div([
                html.Button("last week", className="button-toggle selected"),
                html.Button("last month", className="button-toggle"),
                html.Button("last year", className="button-toggle")
            ])
        ]),

        # Entry point bar charts (mocked with dcc.Graph)
        html.Div(className="dark-section", children=[
            html.H3("Entry Point Breakdown"),
            dcc.Graph(
                config={"displayModeBar": False},
                figure=go.Figure(
                    data=[
                        go.Bar(name="Domains", x=["Domains", "Subdomains", "IP", "Containers"], y=[124, 157, 0, 238], marker_color="#7b61ff"),
                        go.Bar(name="Detected", x=["Domains", "Subdomains", "IP", "Containers"], y=[0, 83, 40, 152], marker_color="#19c4c4")
                    ],
                    layout=go.Layout(barmode="group", plot_bgcolor="#0f0f0f", paper_bgcolor="#0f0f0f", font_color="white")
                )
            )
        ]),

        # Stats cards
        html.Div(className="stats-box", children=[
            html.Div(className="card", children=[
                html.H4("329"),
                html.P("Discovered Assets")
            ]),
            html.Div(className="card", children=[
                html.H4("245"),
                html.P("Unable to Verify")
            ]),
            html.Div(className="card", children=[
                html.H4("131"),
                html.P("Scheduled Assets")
            ]),
            html.Div(className="card", children=[
                html.H4("73"),
                html.P("Issues Found")
            ])
        ]),

        # Bottom section: Reporting, Trials, Issue Levels
        html.Div(style={"display": "flex", "gap": "20px", "marginTop": "20px"}, children=[

            html.Div(className="reporting", style={"flex": 1}, children=[
                html.H3("Reporting"),
                html.P("62 generated"),
                html.P("53 processed"),
                html.P("16 sent to compliance"),
                html.P("9 pending")
            ]),

            html.Div(className="reporting", style={"flex": 1}, children=[
                html.H3("Ongoing Trials"),
                html.Div("DOM Clobbering"),
                html.Div(className="progress-bar", children=[html.Div(className="progress-fill dom-progress", style={"width": "60%"})]),

                html.Div("SSRF"),
                html.Div(className="progress-bar", children=[html.Div(className="progress-fill ssrp-progress", style={"width": "40%"})]),

                html.Div("XML Entities"),
                html.Div(className="progress-bar", children=[html.Div(className="progress-fill xml-progress", style={"width": "30%"})]),

                html.Div("SQL Injections"),
                html.Div(className="progress-bar", children=[html.Div(className="progress-fill sql-progress", style={"width": "25%"})])
            ]),

            html.Div(className="reporting", style={"flex": 1}, children=[
                html.H3("535 Issues Total"),
                html.P("Low - 20%"),
                html.Div(className="bar bar-low", style={"width": "20%"}),
                html.P("Medium - 50%"),
                html.Div(className="bar bar-medium", style={"width": "50%"}),
                html.P("Critical - 12%"),
                html.Div(className="bar bar-critical", style={"width": "12%"})
            ])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
