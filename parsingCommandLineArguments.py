import getopt
import sys


def parsing_cl_args():
    findprojectroot = False
    launchbrowser = True
    serverroot = None
    if len(sys.argv) == 1:
        print("No command line arguments found.")
    else:
        try:
            opts, args = getopt.getopt(
                sys.argv[1:],
                'hs:bf',
                ['help', 'serverroot', 'nobrowser', 'findprojectroot'])
        except getopt.GetoptError as e:
            print ('These was a problem parsing the command line arguments:')
            print ('\t%s' % e)
            sys.exit(1)

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print ('Help flag parsed, these are the current options:\n')
                print ('\t-s <folder>\tSets the server working directory.')
                print('\t-b\t\tSuppresses opening the local browser.')
                sys.exit(0)
            if opt in ('-s', '--serverroot'):
                print ('')
            elif opt in ('-b', '--nobrowser'):
                launchbrowser = False
                print ('Parsed "%s" flag. No browser will be opened.' % opt)
            elif opt in ('-f', '--findprojectroot'):
                findprojectroot = True
                print('Parsed "%s" flag. The ardublockly project root will be '
                      'set as the server root directory.' % opt)
            else:
                print ('Flag "%s" not recognised.' % opt)

    return findprojectroot, launchbrowser, serverroot

find_project_root, launch_browser, server_root = parsing_cl_args()

print ('%s\n %s\n %s' % (find_project_root, launch_browser, server_root))
