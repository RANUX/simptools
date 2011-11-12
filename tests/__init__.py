import os
import sys


parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
os.path.join(parent_dir, 'simptools')
sys.path.append(parent_dir)
