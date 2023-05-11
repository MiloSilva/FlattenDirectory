import sys, os, shutil

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

def help() -> None:
   """
   Print out the help dialogue listing possible arguments
   """

   print("""
   Thanks for using my script! :D
   
   To correctly use this script it is vital to pass the folder to flatten and optionally
   include a target folder and how many levels to flatten in this manner:
   
   py ./path_to_script [optional: -t ./path_to_target -l levels to flatten] ./path_to_source_directory
   
   The optional arguments can be provided in any order.
   """)

def flatten(source: str, target: str, levels: int) -> None:
  """
  Flatten the given directory from the CLI to the executed directory
  """

  # Iterate through present files in source folder to identify files or folders
  for path in os.scandir(source):
     if not os.path.isfile(path):
         folder = path
         if(levels > 1):
           flatten(folder, target, levels-1)
           shutil.rmtree(folder)
         else:
           shutil.move(folder, target)
            
     else:
        file = path
        shutil.move(file, target)


if __name__ == '__main__':
    CLI_ARGUMENTS = sys.argv
    CLI_ARGUMENTS.pop(0)
    modifiers = []

    # Exit if invalid number of arguments
    if (len(CLI_ARGUMENTS) % 2 == 0 or CLI_ARGUMENTS[0] == '-h'):
       help()
       sys.exit()

    SOURCE_DIRECTORY = CLI_ARGUMENTS.pop()

    while len(CLI_ARGUMENTS) > 0:
       modifiers.append((CLI_ARGUMENTS.pop(0), CLI_ARGUMENTS.pop(0)))
       
    target = [tuple[1] for tuple in modifiers if tuple[0] == '-t']
    levels = [tuple[1] for tuple in modifiers if tuple[0] == '-l']

    target = target[0] if len(target) > 0 else FILE_PATH
    levels = levels[0] if len(levels) > 0 else '1'

    flatten(SOURCE_DIRECTORY, target, int(levels))