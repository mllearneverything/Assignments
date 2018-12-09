import sys
import argparse
import shutil
import os


def copy(argument):
    sourcedir = argument.source
    destdir = argument.destination

    if not os.path.exists(sourcedir):
        print (sourcedir + " no such file or directory")
        return

    if not os.path.exists(destdir):
        print (destdir + " no such file or directory")
        return

    #if os.path.isfile(destdir) and os.path.isfile(sourcedir):
    #   if not os.path.exists(sourcedir):
    #       shutil.copyfile(sourcedir, destdir)
    #       return
    #   else:
    #       print ("file already exits")
    #       return

    if argument.recursive and os.path.isdir(sourcedir):
        shutil.copytree(sourcedir, destdir)
        return

    shutil.copy(sourcedir, destdir)


def delete(argument):
    sourcedir = argument.dirname

    if not os.path.exists(sourcedir):
        print (sourcedir + " no such file or directory")
        return

    if os.path.isfile(sourcedir):
        os.remove(sourcedir)
        return
    if os.path.isdir(sourcedir) and not argument.recursive:
        print (sourcedir + " is a directory")  
        return

    if argument.recursive and os.path.isdir(sourcedir):
        shutil.rmtree(sourcedir)
        return


def main():

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands')

    #A copy command
    copy_parser = subparsers.add_parser('copy', help = 'Copy file and directory')
    copy_parser.add_argument('source', action='store', help='file or dir to copy')
    copy_parser.add_argument('destination', action='store', help='destination directory')
    copy_parser.add_argument('--recursive','-r', default=False, action='store_true', help='r    ecursive copy to destination directory')
    copy_parser.set_defaults(func=copy)


    # A list command
    list_parser = subparsers.add_parser('list', help='List contents')
    list_parser.add_argument('dirname', action='store', help='Directory to list')

    # A create command
    create_parser = subparsers.add_parser('create', help='Create a directory')
    create_parser.add_argument('dirname', action='store', help='New directory to create')
    create_parser.add_argument('--read-only', default=False, action='store_true',
            help='Set permissions to prevent writing to the directory',
            )

    # A delete command
    delete_parser = subparsers.add_parser('delete', help='Remove a directory')
    delete_parser.add_argument('dirname', action='store', help='The directory to remove')
    delete_parser.add_argument('--recursive', '-r', default=False, action='store_true',
            help='Remove the contents of the directory, too',
            )
    delete_parser.set_defaults(func=delete)

    arguments = parser.parse_args()

    arguments.func(arguments)



if __name__ == '__main__':

    if not len(sys.argv)>1:
        print("arguments required\nType --help")
        sys.exit(0)


    main()

