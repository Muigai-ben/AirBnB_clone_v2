#!/usr/bin/python3
from fabric.api import env, put, run
import os

env.user = 'ubuntu'
env.hosts = ['<	100.26.136.91>', '<34.229.49.49>']


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>
        filename = os.path.basename(archive_path)
        folder_name = '/data/web_static/releases/{}'.format(os.path.splitext(filename)[0])
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Delete the symbolic link /data/web_static/current
        current_link = '/data/web_static/current'
        run('rm -f {}'.format(current_link))

        # Create a new symbolic link /data/web_static/current
        run('ln -s {} {}'.format(folder_name, current_link))

        print('New version deployed!')
        return True

    except Exception as e:
        print('Deployment failed: {}'.format(e))
        return False
