import bs
import bsInternal
import bsUI
import bsUtils
from bsUtils import *
import random

Messages = ['Rank 1 will get Admin','Rank 2 And 3 will get Vip','Join Our Discord Server By Clicking on The Stats Button','For Any Complaints Join Our Discord Server','Top 10 players will only Get Tag','contact Zyro In discord For Any Queries','join our discord Server Now For Giveaways','You will Not get admin or Vip if You not Joined Our Discord Server even if you are in Top 3']

DelayLength = 65 #Should Be In Seconds

def messager():
	random_msg = random.choice(Messages)
	bsInternal._chatMessage(random_msg)
	return

timer = bs.Timer(DelayLength * 1000, messager, timeType='real', repeat=True)
