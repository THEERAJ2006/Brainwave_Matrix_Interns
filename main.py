from database import init_db
from gui import start_gui

init_db()        # create DB tables if not exist
start_gui()      # launch the app
