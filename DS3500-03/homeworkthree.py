from dash.dependencies import Input, Output
import plotly.graph_objects as go
from dash import html, dcc
from datetime import date
import pandas as pd
import dash

# load data
df_stock = pd.read_csv("data/stockdata2.csv", index_col = 0, parse_dates = True)
df_stock.index = pd.to_datetime(df_stock["Date"])

# initialize app
app = dash.Dash(__name__)

# create a list of dictionaries, which have the keys "label" and "value"
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({"label": i, "value": i})

    return dict_list

# design dashboard layout
app.layout = html.Div(
    children = [
        html.Div(className = "row",
                 children = [
                     html.Div(className = "four columns div-user-controls",
                              children = [
                                  html.H2("STOCK PRICES - DASH"),
                                  html.P("Select one or more stocks from the dropdown below"),
                                  html.Div(className = "div-for-dropdown",
                                            children = [
                                                  dcc.Dropdown(id = "stockselector",
                                                               options = get_options(df_stock["stock"].unique()),
                                                               multi = True,
                                                               value = [df_stock["stock"].sort_values().iloc[0]],
                                                               style = {"width": "100%", "backgroundColor": "#1E1E1E"},
                                                               className = "stockselector")
                                                        ],
                                              style = {"color": "#1E1E1E"}),
                                  html.Div([
                                        dcc.DatePickerRange(
                                            id = "date-picker-range",
                                            start_date = date(2007, 1, 3),
                                            end_date_placeholder_text = "Select a date!",
                                            style = {"width": "100%", "font-size": "0.9em", "padding": "10px", "border-radius": "5px"},
                                            className = "dateselector")
                                            ],
                                      style = {"color": "#1E1E1E"}),
                                  html.Div([
                                        dcc.Textarea(
                                            placeholder = "Enter notes...",
                                            value = "",
                                            style = {"width": "100%"})
                                    ])
                              ]
                     ),
                     html.Div(className = "eight columns div-for-charts bg-grey",
                              children = [
                                  dcc.Graph(id = "timeseries",
                                        config = {"displayModeBar": False},
                                        animate = True),
                                  dcc.Graph(id = "change",
                                        config = {"displayModeBar": False})
                              ])
                 ]
        )
    ]
)

# callback for timeseries price
@app.callback(Output("timeseries", "figure"),
              [Input("stockselector", "value"),
               Input("date-picker-range", "start_date"),
               Input("date-picker-range", "end_date")])
def update_timeseries(selected_dropdown_value, start_date, end_date):
    ''' draw traces of the feature 'value' based one the currently selected stocks '''
    trace = []
    df_sub = df_stock[(df_stock["Date"] >= start_date) & (df_stock["Date"] <= end_date)]

    # draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x = df_sub[df_sub["stock"] == stock].index,
                                 y = df_sub[df_sub["stock"] == stock]["value"],
                                 mode = "lines",
                                 opacity = 0.7,
                                 name = stock,
                                 textposition = "bottom center"))
    traces = [trace]
    data = [val for sublist in traces for val in sublist]

    # define figure
    figure = {"data": data,
              "layout": go.Layout(
                  colorway=["#5E0DAC", "#FF4F00", "#375CB1", "#FF7400", "#FFF400", "#FF0056"],
                  template = "plotly_dark",
                  paper_bgcolor = "rgba(0, 0, 0, 0)",
                  plot_bgcolor = "rgba(0, 0, 0, 0)",
                  margin = {"b": 15},
                  hovermode = "x",
                  autosize = True,
                  title = {"text": "Stock Prices", "font": {"color": "white"}, "x": 0.5},
                  xaxis = {"range": [df_sub.index.min(), df_sub.index.max()]},
              ),
              }
    return figure

# callback for daily price change
@app.callback(Output("change", "figure"),
              [Input("stockselector", "value"),
               Input("date-picker-range", "start_date"),
               Input("date-picker-range", "end_date")])
def update_change(selected_dropdown_value, start_date, end_date):
    ''' draw traces of the feature 'change' based one the currently selected stocks '''
    trace = []
    df_sub = df_stock[(df_stock["Date"] >= start_date) & (df_stock["Date"] <= end_date)]

    # draw and append traces for each stock
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x = df_sub[df_sub["stock"] == stock].index,
                                 y = df_sub[df_sub["stock"] == stock]["change"],
                                 mode = "lines",
                                 opacity = 0.7,
                                 name = stock,
                                 textposition = "bottom center"))
    traces = [trace]
    data = [val for sublist in traces for val in sublist]

    # define figure
    figure = {"data": data,
              "layout": go.Layout(
                  colorway = ["#5E0DAC", "#FF4F00", "#375CB1", "#FF7400", "#FFF400", "#FF0056"],
                  template = "plotly_dark",
                  paper_bgcolor = "rgba(0, 0, 0, 0)",
                  plot_bgcolor = "rgba(0, 0, 0, 0)",
                  margin = {"t": 50},
                  height = 250,
                  hovermode = "x",
                  autosize = True,
                  title = {"text": "Daily Change", "font": {"color": "white"}, "x": 0.5},
                  xaxis = {"showticklabels": False, "range": [df_sub.index.min(), df_sub.index.max()]},
              ),
              }
    return figure

if __name__ == "__main__":
    app.run_server(debug = True)