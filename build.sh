python -m PyInstaller --name Klausrix --onefile --noconsole --hidden-import test1 --hidden-import test1.urls --hidden-import test2 --hidden-import test2.urls --add-data templates/:templates --collect-all whitenoise --collect-all waitress gui.py