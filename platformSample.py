import platform
import struct

print ('Running Python version %s (%s bit) on %s' % (platform.python_version(),
       (struct.calcsize('P') * 8), platform.platform()))


