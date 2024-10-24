from flaskwebgui import FlaskUI
from klausurix.wsgi import application as app

if __name__ == "__main__":
    FlaskUI(app=app, server="django").run()


# OLD: python -m PyInstaller --name DjangoTest --onefile --noconsole --add-data="templates/;templates" --collect-all whitenoise --collect-all waitress gui.py

# OLD: python -m PyInstaller --name DjangoTest --hidden-import test1 --hidden-import test1.urls --hidden-import test2 --hidden-import test2.urls --add-data="templates/;templates" --collect-all whitenoise --collect-all waitress gui.py

# python -m PyInstaller --name DjangoTest --onefile --noconsole --hidden-import test1 --hidden-import test1.urls --hidden-import test2 --hidden-import test2.urls --add-data="templates/;templates" --collect-all whitenoise --collect-all waitress gui.py