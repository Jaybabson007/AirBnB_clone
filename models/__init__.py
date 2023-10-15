#!/usr/bin/python3
"""This python script creates a unique file storage for the web app.
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
