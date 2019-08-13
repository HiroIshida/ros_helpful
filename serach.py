import os
import sys

def search(folder_type): # e.g. `folder_type` may be `launch`, src, script, srv ...
    max_itr = 4
    itr = 0
    dir_relative = "./"
    for itr in range(max_itr):
        lst_filename = os.listdir(dir_relative)

        for filename in lst_filename:
            #print filename
            if filename == "CMakeLists.txt":
                path_root_relative = dir_relative + folder_type
                path_root_absolute = os.path.abspath(path_root_relative)
                if not os.path.exists(path_root_absolute):
                    error_statement = "found a CMakeLists.txt, but " + folder_type + " does not exist" 
                    return (False, error_statement)
                return (True, path_root_absolute)
        dir_relative += "../"

    error_statement = "couln't find a CMakeLists.txt in the specified iteration times."
    return (False, error_statement)

def main():
    args = sys.argv
    folder_type = args[1]
    ret = search(folder_type)
    isSuccess = ret[0]
    sys.exit(ret[1])

main()








