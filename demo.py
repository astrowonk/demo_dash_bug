from dash import Output, Dash, Input, html, State, MATCH, ALL, dcc

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Markdown(
        """Type text and refresh, the persistence works. load and refresh, it does not."""
    ),
    dcc.Input(id='the_field',
              placeholder='Type text or hit button...',
              persistence=True),
    html.Button("Load Data", id='load_button')
])


@app.callback(Output('the_field', 'value'),
              Input('load_button', 'n_clicks'),
              prevent_initial_call=True)
def load_text(_):
    print("Loading something into the field via the button")
    return "Here is some text!"


if __name__ == '__main__':
    app.run_server(debug=True)
