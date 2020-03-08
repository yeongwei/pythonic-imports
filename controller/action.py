#!/usr/bin/python3

from system import utils
from controller import base
from model import database

utils.printSysPaths(__file__)

base.init();

def do():
	print("action.do")
	print(database.create())
	print(database.update())
	print(database.delete())
