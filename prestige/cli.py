from argparse import ArgumentParser

parser = ArgumentParser(description='prestige')
parser.add_argument(
  '--upload',
  action='store_true',
  )
parser.add_argument(
  '-o', '--optimize',
  type=int 
  )
parser.add_argument(
  '-b', '--bucket',  
  )
parser.add_argument(
  '-v', '--version', 
  action='version', 
  version="0.1", 
  )
ARGS = parser.parse_args()