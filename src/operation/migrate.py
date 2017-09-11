# coding: UTF-8
import shutil
import traceback
from fabric.api import env, put


def local(srcpath, dstpath):
    result = True
    try:
        shutil.move(srcpath, dstpath)
    except:
        result = str(traceback.print_exc())
    return result


def host(srcpath, dstip, dstpath):
    result = True
    env.hosts = [dstip]
    env.user = 'vagrant'
    env.password = 'vagrant'
    put(srcpath, dstpath)
    return result
