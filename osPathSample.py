import ardublocklyserver
import os

# print (ardublocklyserver.local_package_path)
# print(os.path.isdir(ardublocklyserver.local_package_path))

if os.path.isdir(ardublocklyserver.local_package_path):
    print ('Local package: %s' % ardublocklyserver.local_package_path)
else:
    print ('Not using local-package, likely running packaged.')









