"""
Entry point for the application
"""

import os
from app import create_app, setup_database

app = create_app()
if not os.path.isfile('instance/discount.db'):
    setup_database(app)
app.run()
