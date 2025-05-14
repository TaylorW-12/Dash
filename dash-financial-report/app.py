# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html 
from dash.dependencies import Input, Output, State
from pages import (
    overview,
    pricePerformance,
    portfolioManagement,
    feesMins,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Financial Report"
server = app.server

# Example filter options (move these to a configuration file if needed)
years = [2020, 2021, 2022, 2023, 2024]
categories = ["Equity", "Fixed Income", "Balanced", "Alternative"]
regions = ["North America", "Europe", "Asia", "Emerging Markets"]

# Create the sidebar with filters
def create_sidebar():
    return html.Div(
        [
            html.Div(
                [
                    html.H2("Filters", className="sidebar-title"),
                ],
                className="sidebar-header",
            ),
            
            # Date Range Filter
            html.Div(
                [
                    html.H3("Time Period"),
                    dcc.Dropdown(
                        id="year-dropdown",
                        options=[{"label": str(year), "value": year} for year in years],
                        value=2024,
                        clearable=False,
                    ),
                ],
                className="filter-section",
            ),
            
            # Category Filter
            html.Div(
                [
                    html.H3("Asset Class"),
                    dcc.RadioItems(
                        id="category-radio",
                        options=[{"label": cat, "value": cat.lower().replace(" ", "_")} for cat in categories],
                        value="equity",
                        className="radio-items",
                    ),
                ],
                className="filter-section",
            ),
            
            # Region Filter with Checkboxes
            html.Div(
                [
                    html.H3("Regions"),
                    dcc.Checklist(
                        id="region-checklist",
                        options=[{"label": region, "value": region.lower().replace(" ", "_")} for region in regions],
                        value=["north_america", "europe", "asia", "emerging_markets"],
                        className="checkbox-items",
                    ),
                ],
                className="filter-section",
            ),
            
            # Value Range Filter
            html.Div(
                [
                    html.H3("Performance Range (%)"),
                    dcc.RangeSlider(
                        id="performance-range-slider",
                        min=-20,
                        max=50,
                        step=5,
                        marks={i: str(i) for i in range(-20, 51, 10)},
                        value=[-5, 25],
                    ),
                ],
                className="filter-section",
            ),
            
            # Filter Action Buttons
            html.Div(
                [
                    html.Button("Apply Filters", id="apply-filters", className="btn"),
                    html.Button("Reset Filters", id="reset-filters", className="btn btn-outline"),
                ],
                className="filter-section",
            ),
            
            # Navigation Links - Adding these to sidebar for better UX
            html.Div(
                [
                    html.H3("Navigation"),
                    html.Div(
                        [
                            html.A(
                                "Overview",
                                href="/dash-financial-report/",
                                className="sidebar-nav-link",
                            ),
                            html.A(
                                "Price Performance",
                                href="/dash-financial-report/price-performance",
                                className="sidebar-nav-link",
                            ),
                            html.A(
                                "Portfolio Management",
                                href="/dash-financial-report/portfolio-management",
                                className="sidebar-nav-link",
                            ),
                            html.A(
                                "Fees & Minimums",
                                href="/dash-financial-report/fees",
                                className="sidebar-nav-link",
                            ),
                        ],
                        className="sidebar-nav-links",
                    ),
                ],
                className="filter-section navigation-section",
            ),
        ],
        className="sidebar",
    )

# Describe the layout/ UI of the app with sidebar
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                create_sidebar(),
                html.Div([
                    html.Div(id="page-content"),
                    html.Div(id="apply-filters-status")
                ], className="main-content")
            ],
            className="dashboard-container",
        )
    ]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/price-performance":
        return pricePerformance.create_layout(app)
    elif pathname == "/dash-financial-report/portfolio-management":
        return portfolioManagement.create_layout(app)
    elif pathname == "/dash-financial-report/fees":
        return feesMins.create_layout(app)
    else:
        return overview.create_layout(app)

# Add callback for filter actions (to be implemented based on your data)
@app.callback(
    Output("year-dropdown", "value"),
    [Input("reset-filters", "n_clicks")],
    [State("year-dropdown", "options")]
)
def reset_year_filter(n_clicks, options):
    if n_clicks:
        # Return the most recent year as default
        return max([opt["value"] for opt in options])
    # Return dash.no_update if the button wasn't clicked
    return dash.no_update

# Example filter application callback (implement for your specific data)
@app.callback(
    Output("apply-filters-status", "children"),
    [Input("apply-filters", "n_clicks")],
    [
        State("year-dropdown", "value"),
        State("category-radio", "value"),
        State("region-checklist", "value"),
        State("performance-range-slider", "value")
    ]
)
def apply_filters(n_clicks, year, category, regions, performance_range):
    if n_clicks:
        # Process the filter values and update your data/charts
        # This is a placeholder that would be customized for your specific implementation
        return f"Filters applied: Year={year}, Category={category}, Regions={regions}, Performance Range={performance_range}"
    return ""

if __name__ == "__main__":
    app.run_server(debug=True)