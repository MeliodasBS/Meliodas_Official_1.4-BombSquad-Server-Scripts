from bsSpaz import *

# Kibone ###################################
t = Appearance("Kibone")
t.colorTexture = "bonesColor"
t.colorMaskTexture = "bonesColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "bonesIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "bonesHead"
t.torsoModel =    "cyborgTorso"
t.pelvisModel =   "cyborgPelvis"
t.upperArmModel = "cyborgUpperArm"
t.foreArmModel =  "cyborgForeArm"
t.handModel =     "cyborgHand"
t.upperLegModel = "cyborgUpperLeg"
t.lowerLegModel = "cyborgLowerLeg"
t.toesModel =     "cyborgToes"
cyborgSounds =    ['cyborg1', 'cyborg2', 'cyborg3', 'cyborg4']
cyborgHitSounds = ['cyborgHit1', 'cyborgHit2']
t.attackSounds = cyborgSounds
t.jumpSounds = cyborgSounds
t.impactSounds = cyborgHitSounds
t.deathSounds=["cyborgDeath"]
t.pickupSounds = cyborgSounds
t.fallSounds=["cyborgFall"]
t.style = 'cyborg'