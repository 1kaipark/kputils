import shutil
import os

dev_path = '/Users/applelaptop/dev/kputils'
wd = '/Users/applelaptop/CODE/kputils'

os.chdir(wd)
scripts = os.listdir()
scripts = [s for s in scripts if s.endswith('.py') and s != 'sync.py']
for s in scripts:
    shutil.copyfile(
        s,
        os.path.join(dev_path, s)
    )
    print(f'successfully copied {s} to {dev_path}')