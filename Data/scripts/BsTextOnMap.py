# -- coding: utf-8 --
texts = [u'']
import bs
from bsMap import *
import bsMap
from random import randrange
#from settings import *
#count = len(texts)
i=0

def __init__(self, vrOverlayCenterOffset=None):
        """
        Instantiate a map.
        """
        import bsInternal
        bs.Actor.__init__(self)
        self.preloadData = self.preload(onDemand=True)
        def text(): 
                t = bs.newNode('text',
                       attrs={ 'text':u'👑|OWNER : <Your Name>\n🌿|EDITOR : MELIODAS\n⚡|SCRIPT BY SPARXTN',
                             
'scale':0.5,
                              'maxWidth':0,
                              'position':(-640,50),
                              'shadow':1,
                              'flatness':0.9,
                              'color':(1,1,1),
                              'hAlign':'left',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0:0.8})
                t = bs.newNode('text',
                       attrs={ 'text':u'<Your Server Name>',
                              'scale':0.72,
                              'maxWidth':0,
                              'position':(11,648),
                              'shadow':0.9,
                              'flatness':1.0,
                              'color':(1,1,1),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0:1.3})
                
                t = bs.newNode('text',
                       attrs={ 'text':'Welcome To Our Server',
                              'scale':0.52,
                              'maxWidth':0,
                              'position':(11,633),
                              'shadow':0.9,
                              'flatness':1.0,
                              'color':(0,255,191),
                              'hAlign':'center',
                              'vAttach':'bottom'})                                
                bs.animate(t,'opacity',{0:0.7})

                t = bs.newNode('text',
                       attrs={ 'text':u'',
                              'scale':0.5,
                              'maxWidth':0,
                              'position':(-570,90),
                              'shadow':0.9,
                              'flatness':1,
                              'color':(1,1,1),
                              'hAlign':'left',
                              'vAttach':'top'})
                bs.animate(t,'opacity',{0:0.5})
	def recurringText():
		global i
		if i>len(texts)-2:
			i=0
		else:
			i+=1
                t = bs.newNode('text',
                       attrs={ 'text':random.choice([u'\ue048WELCOME TO <YOUR SERVER NAME>\ue048',u'👾RESPECT EVERYONE👾',u'JOIN OUR DISCORD SERVER BY CLICKING ON STATS BUTTON',u'[👑]OWNER - <YOUR NAME>[👑]']),
                              'scale':0.72,
                              'maxWidth':0,
                              'position':(0,138),
                              'shadow':0.9,
                              'flatness':1.0,
                              'color':(0.2,1,1,),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t, 'scale', {0: 0.0, 500: 0.7, 4500: 0.7, 5000: 0.0}, loop=False)                     
                multiColor = {0:(1,1,1)}
                bsUtils.animateArray(t,'color',3,multiColor,True)
                bs.gameTimer(7000,t.delete)
	import settings
	if settings.enableCoinSystem:
		texts.append(settings.coinTexts)
	bs.gameTimer(10,bs.Call(text))
	bs.gameTimer(0,bs.Call(recurringText))
	bs.gameTimer(7000,bs.Call(recurringText),repeat = True)
        
        # set some defaults
        bsGlobals = bs.getSharedObject('globals')
        # area-of-interest bounds
        aoiBounds = self.getDefBoundBox("areaOfInterestBounds")
        if aoiBounds is None:
            print 'WARNING: no "aoiBounds" found for map:',self.getName()
            aoiBounds = (-1,-1,-1,1,1,1)
        bsGlobals.areaOfInterestBounds = aoiBounds
        # map bounds
        mapBounds = self.getDefBoundBox("levelBounds")
        if mapBounds is None:
            print 'WARNING: no "levelBounds" found for map:',self.getName()
            mapBounds = (-30,-10,-30,30,100,30)
        bsInternal._setMapBounds(mapBounds)
        # shadow ranges
        try: bsGlobals.shadowRange = [
                self.defs.points[v][1] for v in 
                ['shadowLowerBottom','shadowLowerTop',
                 'shadowUpperBottom','shadowUpperTop']]
        except Exception: pass
        # in vr, set a fixed point in space for the overlay to show up at..
        # by default we use the bounds center but allow the map to override it
        center = ((aoiBounds[0]+aoiBounds[3])*0.5,
                  (aoiBounds[1]+aoiBounds[4])*0.5,
                  (aoiBounds[2]+aoiBounds[5])*0.5)
        if vrOverlayCenterOffset is not None:
            center = (center[0]+vrOverlayCenterOffset[0],
                      center[1]+vrOverlayCenterOffset[1],
                      center[2]+vrOverlayCenterOffset[2])
        bsGlobals.vrOverlayCenter = center
        bsGlobals.vrOverlayCenterEnabled = True
        self.spawnPoints = self.getDefPoints("spawn") or [(0,0,0,0,0,0)]
        self.ffaSpawnPoints = self.getDefPoints("ffaSpawn") or [(0,0,0,0,0,0)]
        self.spawnByFlagPoints = (self.getDefPoints("spawnByFlag")
                                  or [(0,0,0,0,0,0)])
        self.flagPoints = self.getDefPoints("flag") or [(0,0,0)]
        self.flagPoints = [p[:3] for p in self.flagPoints] # just want points
        self.flagPointDefault = self.getDefPoint("flagDefault") or (0,1,0)
        self.powerupSpawnPoints = self.getDefPoints("powerupSpawn") or [(0,0,0)]
        self.powerupSpawnPoints = \
            [p[:3] for p in self.powerupSpawnPoints] # just want points
        self.tntPoints = self.getDefPoints("tnt") or []
        self.tntPoints = [p[:3] for p in self.tntPoints] # just want points
        self.isHockey = False
        self.isFlying = False
        self._nextFFAStartIndex = 0
        
bsMap.Map.__init__ = __init__
