import bs
import bsInternal
import bsUI
import bsUtils
from bsUtils import *
import random

Messages = ['Rank 1 will get Admin','Rank 2 And 3 will get Vip']

DelayLength = 65 #Should Be In Seconds

def messager():
	random_msg = random.choice(Messages)
	bsInternal._chatMessage(random_msg)
	return

timer = bs.Timer(DelayLength * 1000, messager, timeType='real', repeat=True)
