from dash.testing.application_runners import import_app


def test_header_is_present(dash_duo):
    """The app should display the main header."""
    app = import_app("app")
    dash_duo.start_server(app)

    # Wait for the H1 to appear and check its text
    dash_duo.wait_for_element("h1", timeout=10)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"


def test_visualisation_is_present(dash_duo):
    """The app should display the line chart."""
    app = import_app("app")
    dash_duo.start_server(app)

    # The dcc.Graph renders with id="sales-line-chart"
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    chart = dash_duo.find_element("#sales-line-chart")
    assert chart is not None


def test_region_picker_is_present(dash_duo):
    """The app should display the region radio button group."""
    app = import_app("app")
    dash_duo.start_server(app)

    # The dcc.RadioItems renders with id="region-filter"
    dash_duo.wait_for_element("#region-filter", timeout=10)
    picker = dash_duo.find_element("#region-filter")
    assert picker is not None
