#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""
from datetime import datetime
from os.path import exists, isdir
from fabric.api import put, run, env, local
env.hosts = ['54.145.39.140', '23.22.141.108']
env.user = "ubuntu"


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        noExtension = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, noExtension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, noExtension))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, noExtension))
        run('rm -rf {}{}/web_static'.format(path, noExtension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noExtension))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
