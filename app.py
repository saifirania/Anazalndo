from views.layout import make_layout
from maindash import app

# That's our Dash application :
if __name__ == '__main__':
    app.layout = make_layout()
    app.run_server(debug=True)