import sys
import getopt

# print (sys.argv)
# print (len("Hello World!"))
# print (len(sys.argv))
try:
    opt, argv = getopt.getopt(
        sys.argv[1:],
        'hs:bf',
        ['help', 'serverroot', 'nobrowser', 'findprojectroot'])
except getopt.GetoptError as e:
    print ('These was a problem parsing the command line arguments:')
    print ('\t%s' % e)
    sys.exit(1)

# print (opt)
