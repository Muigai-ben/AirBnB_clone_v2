#!/usr/bin/python3
""" a module for fabric script script that generates a .tgz archive."""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    try:
"""Create the 'versions' folder if it doesn't exist"""
        local("mkdir -p versions")

"""Generate the current timestamp for the archive name"""
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")

"""Define the archive name"""
        archive_name = "web_static_{}.tgz".format(timestamp)

"""Compress the contents of the 'web_static' folder into the archive"""
        local("tar -cvzf versions/{} web_static".format(archive_name))

"""Return the archive path if successfully generated"""
        return os.path.join("versions", archive_name)

    except Exception as e:
"""Print an error message and return None if an exception occurs"""
        print("Error packing: {}".format(e))
        return None

# Example usage
archive_path = do_pack()
if archive_path:
    print("Archive created successfully at: {}".format(archive_path))
else:
    print("Failed to create the archive.")

