@app.callback(
    Output("css-page-content", "children"),
    [Input("url", "pathname"), Input("url", "search"), Input("url", "href")],
    State("page-content", "children")
)
def display_page(pathname, search, fullPath, stateContent):
    pageContent = None
    p, l = dash_helper.getParams(search)
    if pathname:
        if pathname == '/bu/val/sampleDashboard':
            pageContent = dashboard.sampleDashboard(p, l)
        
        return pageContent
    else:
        return stateContent
