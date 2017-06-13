import os
import sys
import glob
import re
import getopt


# old names that will be replaced
PROJ_NAME = 'demoproject'
APP_NAME = 'demoapp'
CAP_APP_NAME = APP_NAME.capitalize()
# list of files that should be modified
FILES = [
    PROJ_NAME + '/celery.py',
    PROJ_NAME + '/settings.py',
    PROJ_NAME + '/urls.py',
    PROJ_NAME + '/wsgi.py',
    APP_NAME + '/apps.py',
    APP_NAME + '/urls.py'
]
# # list of dirs that should be renamed
# DIRS = [
#     PROJ_NAME,
#     APP_NAME
# ]


# Start with renaming files
def modify_files(project_name, app_name):
    """
    Replace proj/app name occurences with new names.
    """
    cap_app_name = app_name.capitalize()
    for elem in FILES:
        print('> > > ', elem)
        with open(elem, 'r') as fp:
            temp = fp.read()
            print(
                re.subn(PROJ_NAME, project_name, temp)[1],
                re.subn(APP_NAME, app_name, temp)[1],
                re.subn(CAP_APP_NAME, cap_app_name, temp)[1]
            )
            temp = temp.replace(PROJ_NAME, project_name).replace(
                APP_NAME, app_name).replace(CAP_APP_NAME, cap_app_name)
        with open(elem, 'w') as fp:
            fp.write(temp)

def modify_dirs(project_name, app_name):
    """
    Renames folders.
    """
    os.rename(PROJ_NAME, project_name)
    os.rename(APP_NAME, app_name)


def main(argv):
    project_name, app_name = '', ''
    try:
        opts, args = getopt.getopt(argv, 'p:a:')
    except getopt.GetoptError:
        print('-p project_name -a app_name')
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-p':
            project_name = arg
        elif opt == '-a':
            app_name = arg

    if project_name and app_name:
        modify_files(project_name, app_name)
        modify_dirs(project_name, app_name)
        print('Project has been successfully renamed.')
        sys.exit(0)
    print('-p project_name -a app_name')
    sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])
