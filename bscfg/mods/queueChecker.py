import bs,bsInternal
from getPermissionsHashes import ownerHashes

def getNoOfPlayers():
	return len(bsInternal._getGameRoster())

def _onQueueQueryResult(result):
    #print result
    inQueue = result['e']
    if inQueue != []:
	for queue in inQueue:
	    if queue[2] in ownerHashes:
		currentSize = bsInternal._getPublicPartyMaxSize()
		noOfPlayers = getNoOfPlayers()
		#print currentSize, noOfPlayers
		if currentSize <= noOfPlayers:
			bsInternal._chatMessage('Making space for king...')
			setsize = noOfPlayers +1
			print 'setting >>>', setsize
			bsInternal._setPublicPartyMaxSize(setsize)
			bsInternal._getForegroundHostSession()._maxPlayers = setsize
			#timer = bs.realTimer(5000,start)
		
		
def start():
        bsInternal._addTransaction(
                {'type': 'PARTY_QUEUE_QUERY', 'q': "Your Server Queue Id here"},
                callback=bs.Call(_onQueueQueryResult))
        bsInternal._runTransactions()

timer= bs.Timer(7000,start,timeType='real',repeat=True)
print 'Queue Checker is enabled'
