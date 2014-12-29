import macutil.dropbox_photos_rename
import os
import subprocess
import time
import datetime

_tmp = os.path.join(os.environ['PWD'], 'tmp')
subprocess.call(['rm', '-rf', _tmp])
os.mkdir(_tmp)
_dropbox = os.path.join(_tmp, 'Dropbox')
os.mkdir(_dropbox)
_photos = os.path.join(_dropbox, 'Photos')
os.mkdir(_photos)
_camera_uploads = os.path.join(_dropbox, 'Camera Uploads')
os.mkdir(_camera_uploads)

os.environ["HOME"] = _tmp

def create_file(f,mtime=None):
    p = os.path.join(_camera_uploads, f)
    fh = open(p, 'w')
    fh.write('')
    fh.close()
    if mtime:
        mtime = time.mktime(datetime.datetime.strptime(mtime, "%Y%m%d").timetuple())
        os.utime(p, (mtime, mtime))
    return p
    
def test_1():
    p = create_file('x.txt', '20141223')
    macutil.dropbox_photos_rename.move_one(p)
    assert os.path.isfile(os.path.join(_photos, '2014-12-23', 'x.txt'))
    p = create_file('2014-12-16-hello.txt', '20141223')
    macutil.dropbox_photos_rename.move_one(p)
    assert os.path.isfile(os.path.join(_photos, '2014-12-16', '2014-12-16-hello.txt'))
    p = create_file('2014-12-16-hello.txt', '20141223')
    macutil.dropbox_photos_rename.move_one(p)
    assert os.path.isfile(os.path.join(_photos, '2014-12-16', '2014-12-16-hello.txt'))
    p = create_file('2014-12-11-UPPER.JPEG')
    macutil.dropbox_photos_rename.move_one(p)
    assert os.path.isfile(os.path.join(_photos, '2014-12-11', '2014-12-11-upper.jpg'))
