from bsSpaz import *

###############  SPAZ   ##################
t = Appearance("Spaz1")

t.colorTexture = "neoSpazColor"
t.colorMaskTexture = "neoSpazColorMask"

t.iconTexture = "neoSpazIcon"
t.iconMaskTexture = "neoSpazIconColorMask"

t.headModel = "neoSpazHead"
t.torsoModel = "neoSpazTorso"
t.pelvisModel = "neoSpazPelvis"
t.upperArmModel = "neoSpazUpperArm"
t.foreArmModel = "neoSpazForeArm"
t.handModel = "neoSpazHand"
t.upperLegModel = "neoSpazUpperLeg"
t.lowerLegModel = "neoSpazLowerLeg"
t.toesModel = "neoSpazToes"

t.jumpSounds=["spazJump01",
              "spazJump02",
              "spazJump03",
              "spazJump04"]
t.attackSounds=["spazAttack01",
                "spazAttack02",
                "spazAttack03",
                "spazAttack04"]
t.impactSounds=["spazImpact01",
                "spazImpact02",
                "spazImpact03",
                "spazImpact04"]
t.deathSounds=["spazDeath01"]
t.pickupSounds=["spazPickup01"]
t.fallSounds=["spazFall01"]

t.style = 'spaz'


###############  Zoe   ##################
t = Appearance("Zoe1")

t.colorTexture = "zoeColor"
t.colorMaskTexture = "zoeColorMask"

t.defaultColor = (0.6, 0.6, 0.6)
t.defaultHighlight = (0, 1, 0)

t.iconTexture = "zoeIcon"
t.iconMaskTexture = "zoeIconColorMask"

t.headModel = "zoeHead"
t.torsoModel = "zoeTorso"
t.pelvisModel = "zoePelvis"
t.upperArmModel = "zoeUpperArm"
t.foreArmModel = "zoeForeArm"
t.handModel = "zoeHand"
t.upperLegModel = "zoeUpperLeg"
t.lowerLegModel = "zoeLowerLeg"
t.toesModel = "zoeToes"

t.jumpSounds=["zoeJump01",
              "zoeJump02",
              "zoeJump03"]
t.attackSounds=["zoeAttack01",
                "zoeAttack02",
                "zoeAttack03",
                "zoeAttack04"]
t.impactSounds=["zoeImpact01",
                "zoeImpact02",
                "zoeImpact03",
                "zoeImpact04"]
t.deathSounds=["zoeDeath01"]
t.pickupSounds=["zoePickup01"]
t.fallSounds=["zoeFall01"]

t.style = 'female'


###############  Ninja   ##################
t = Appearance("Snake Shadow1")

t.colorTexture = "ninjaColor"
t.colorMaskTexture = "ninjaColorMask"

t.defaultColor = (1, 1, 1)
t.defaultHighlight = (0.55, 0.8, 0.55)

t.iconTexture = "ninjaIcon"
t.iconMaskTexture = "ninjaIconColorMask"

t.headModel = "ninjaHead"
t.torsoModel = "ninjaTorso"
t.pelvisModel = "ninjaPelvis"
t.upperArmModel = "ninjaUpperArm"
t.foreArmModel = "ninjaForeArm"
t.handModel = "ninjaHand"
t.upperLegModel = "ninjaUpperLeg"
t.lowerLegModel = "ninjaLowerLeg"
t.toesModel = "ninjaToes"

ninjaAttacks = ['ninjaAttack'+str(i+1)+'' for i in range(7)]
ninjaHits = ['ninjaHit'+str(i+1)+'' for i in range(8)]
ninjaJumps = ['ninjaAttack'+str(i+1)+'' for i in range(7)]

t.jumpSounds=ninjaJumps
t.attackSounds=ninjaAttacks
t.impactSounds=ninjaHits
t.deathSounds=["ninjaDeath1"]
t.pickupSounds=ninjaAttacks
t.fallSounds=["ninjaFall1"]

t.style = 'ninja'


###############  Kronk   ##################
t = Appearance("Kronk1")

t.colorTexture = "kronk"
t.colorMaskTexture = "kronkColorMask"

t.defaultColor = (0.4, 0.5, 0.4)
t.defaultHighlight = (1, 0.5, 0.3)

t.iconTexture = "kronkIcon"
t.iconMaskTexture = "kronkIconColorMask"

t.headModel = "kronkHead"
t.torsoModel = "kronkTorso"
t.pelvisModel = "kronkPelvis"
t.upperArmModel = "kronkUpperArm"
t.foreArmModel = "kronkForeArm"
t.handModel = "kronkHand"
t.upperLegModel = "kronkUpperLeg"
t.lowerLegModel = "kronkLowerLeg"
t.toesModel = "kronkToes"

kronkSounds = ["kronk1",
              "kronk2",
              "kronk3",
              "kronk4",
              "kronk5",
              "kronk6",
              "kronk7",
              "kronk8",
              "kronk9",
              "kronk10"]
t.jumpSounds=kronkSounds
t.attackSounds=kronkSounds
t.impactSounds=kronkSounds
t.deathSounds=["kronkDeath"]
t.pickupSounds=kronkSounds
t.fallSounds=["kronkFall"]

t.style = 'kronk'


###############  MEL   ##################
t = Appearance("Mel1")

t.colorTexture = "melColor"
t.colorMaskTexture = "melColorMask"

t.defaultColor = (1, 1, 1)
t.defaultHighlight = (0.1, 0.6, 0.1)

t.iconTexture = "melIcon"
t.iconMaskTexture = "melIconColorMask"

t.headModel =     "melHead"
t.torsoModel =    "melTorso"
t.pelvisModel = "kronkPelvis"
t.upperArmModel = "melUpperArm"
t.foreArmModel =  "melForeArm"
t.handModel =     "melHand"
t.upperLegModel = "melUpperLeg"
t.lowerLegModel = "melLowerLeg"
t.toesModel =     "melToes"

melSounds = ["mel01",
              "mel02",
              "mel03",
              "mel04",
              "mel05",
              "mel06",
              "mel07",
              "mel08",
              "mel09",
              "mel10"]

t.attackSounds = melSounds
t.jumpSounds = melSounds
t.impactSounds = melSounds
t.deathSounds=["melDeath01"]
t.pickupSounds = melSounds
t.fallSounds=["melFall01"]

t.style = 'mel'


###############  Jack Morgan   ##################

t = Appearance("Jack Morgan1")

t.colorTexture = "jackColor"
t.colorMaskTexture = "jackColorMask"

t.defaultColor = (1, 0.2, 0.1)
t.defaultHighlight = (1, 1, 0)

t.iconTexture = "jackIcon"
t.iconMaskTexture = "jackIconColorMask"

t.headModel =     "jackHead"
t.torsoModel =    "jackTorso"
t.pelvisModel = "kronkPelvis"
t.upperArmModel = "jackUpperArm"
t.foreArmModel =  "jackForeArm"
t.handModel =     "jackHand"
t.upperLegModel = "jackUpperLeg"
t.lowerLegModel = "jackLowerLeg"
t.toesModel =     "jackToes"

hitSounds = ["jackHit01",
             "jackHit02",
             "jackHit03",
             "jackHit04",
             "jackHit05",
             "jackHit06",
             "jackHit07"]

sounds = ["jack01",
          "jack02",
          "jack03",
          "jack04",
          "jack05",
          "jack06"]

t.attackSounds = sounds
t.jumpSounds = sounds
t.impactSounds = hitSounds
t.deathSounds=["jackDeath01"]
t.pickupSounds = sounds
t.fallSounds=["jackFall01"]

t.style = 'pirate'


###############  SANTA   ##################

t = Appearance("Santa Claus1")

t.colorTexture = "santaColor"
t.colorMaskTexture = "santaColorMask"

t.defaultColor = (1, 0, 0)
t.defaultHighlight = (1, 1, 1)

t.iconTexture = "santaIcon"
t.iconMaskTexture = "santaIconColorMask"

t.headModel =     "santaHead"
t.torsoModel =    "santaTorso"
t.pelvisModel = "kronkPelvis"
t.upperArmModel = "santaUpperArm"
t.foreArmModel =  "santaForeArm"
t.handModel =     "santaHand"
t.upperLegModel = "santaUpperLeg"
t.lowerLegModel = "santaLowerLeg"
t.toesModel =     "santaToes"

hitSounds = ['santaHit01', 'santaHit02', 'santaHit03', 'santaHit04']
sounds = ['santa01', 'santa02', 'santa03', 'santa04', 'santa05']

t.attackSounds = sounds
t.jumpSounds = sounds
t.impactSounds = hitSounds
t.deathSounds=["santaDeath"]
t.pickupSounds = sounds
t.fallSounds=["santaFall"]

t.style = 'santa'

###############  FROSTY   ##################

t = Appearance("Frosty1")

t.colorTexture = "frostyColor"
t.colorMaskTexture = "frostyColorMask"

t.defaultColor = (0.5, 0.5, 1)
t.defaultHighlight = (1, 0.5, 0)

t.iconTexture = "frostyIcon"
t.iconMaskTexture = "frostyIconColorMask"

t.headModel =     "frostyHead"
t.torsoModel =    "frostyTorso"
t.pelvisModel = "frostyPelvis"
t.upperArmModel = "frostyUpperArm"
t.foreArmModel =  "frostyForeArm"
t.handModel =     "frostyHand"
t.upperLegModel = "frostyUpperLeg"
t.lowerLegModel = "frostyLowerLeg"
t.toesModel =     "frostyToes"

frostySounds = ['frosty01', 'frosty02', 'frosty03', 'frosty04', 'frosty05']
frostyHitSounds = ['frostyHit01', 'frostyHit02', 'frostyHit03']

t.attackSounds = frostySounds
t.jumpSounds = frostySounds
t.impactSounds = frostyHitSounds
t.deathSounds=["frostyDeath"]
t.pickupSounds = frostySounds
t.fallSounds=["frostyFall"]

t.style = 'frosty'

###############  BONES  ##################

t = Appearance("Bones1")

t.colorTexture = "bonesColor"
t.colorMaskTexture = "bonesColorMask"

t.defaultColor = (0.6, 0.9, 1)
t.defaultHighlight = (0.6, 0.9, 1)

t.iconTexture = "bonesIcon"
t.iconMaskTexture = "bonesIconColorMask"

t.headModel =     "bonesHead"
t.torsoModel =    "bonesTorso"
t.pelvisModel =   "bonesPelvis"
t.upperArmModel = "bonesUpperArm"
t.foreArmModel =  "bonesForeArm"
t.handModel =     "bonesHand"
t.upperLegModel = "bonesUpperLeg"
t.lowerLegModel = "bonesLowerLeg"
t.toesModel =     "bonesToes"

bonesSounds =    ['bones1', 'bones2', 'bones3']
bonesHitSounds = ['bones1', 'bones2', 'bones3']

t.attackSounds = bonesSounds
t.jumpSounds = bonesSounds
t.impactSounds = bonesHitSounds
t.deathSounds=["bonesDeath"]
t.pickupSounds = bonesSounds
t.fallSounds=["bonesFall"]

t.style = 'bones'

# bear ###################################

t = Appearance("Bernard1")

t.colorTexture = "bearColor"
t.colorMaskTexture = "bearColorMask"

t.defaultColor = (0.7, 0.5, 0.0)
#t.defaultHighlight = (0.6, 0.5, 0.8)

t.iconTexture = "bearIcon"
t.iconMaskTexture = "bearIconColorMask"

t.headModel =     "bearHead"
t.torsoModel =    "bearTorso"
t.pelvisModel =   "bearPelvis"
t.upperArmModel = "bearUpperArm"
t.foreArmModel =  "bearForeArm"
t.handModel =     "bearHand"
t.upperLegModel = "bearUpperLeg"
t.lowerLegModel = "bearLowerLeg"
t.toesModel =     "bearToes"

bearSounds =    ['bear1', 'bear2', 'bear3', 'bear4']
bearHitSounds = ['bearHit1', 'bearHit2']

t.attackSounds = bearSounds
t.jumpSounds = bearSounds
t.impactSounds = bearHitSounds
t.deathSounds=["bearDeath"]
t.pickupSounds = bearSounds
t.fallSounds=["bearFall"]

t.style = 'bear'

# Penguin ###################################

t = Appearance("Pascal1")

t.colorTexture = "penguinColor"
t.colorMaskTexture = "penguinColorMask"

t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)

t.iconTexture = "penguinIcon"
t.iconMaskTexture = "penguinIconColorMask"

t.headModel =     "penguinHead"
t.torsoModel =    "penguinTorso"
t.pelvisModel =   "penguinPelvis"
t.upperArmModel = "penguinUpperArm"
t.foreArmModel =  "penguinForeArm"
t.handModel =     "penguinHand"
t.upperLegModel = "penguinUpperLeg"
t.lowerLegModel = "penguinLowerLeg"
t.toesModel =     "penguinToes"

penguinSounds =    ['penguin1', 'penguin2', 'penguin3', 'penguin4']
penguinHitSounds = ['penguinHit1', 'penguinHit2']

t.attackSounds = penguinSounds
t.jumpSounds = penguinSounds
t.impactSounds = penguinHitSounds
t.deathSounds=["penguinDeath"]
t.pickupSounds = penguinSounds
t.fallSounds=["penguinFall"]

t.style = 'penguin'


# Ali ###################################
t = Appearance("Taobao Mascot1")
t.colorTexture = "aliColor"
t.colorMaskTexture = "aliColorMask"
t.defaultColor = (1, 0.5, 0)
t.defaultHighlight = (1, 1, 1)
t.iconTexture = "aliIcon"
t.iconMaskTexture = "aliIconColorMask"
t.headModel =     "aliHead"
t.torsoModel =    "aliTorso"
t.pelvisModel =   "aliPelvis"
t.upperArmModel = "aliUpperArm"
t.foreArmModel =  "aliForeArm"
t.handModel =     "aliHand"
t.upperLegModel = "aliUpperLeg"
t.lowerLegModel = "aliLowerLeg"
t.toesModel =     "aliToes"
aliSounds =    ['ali1', 'ali2', 'ali3', 'ali4']
aliHitSounds = ['aliHit1', 'aliHit2']
t.attackSounds = aliSounds
t.jumpSounds = aliSounds
t.impactSounds = aliHitSounds
t.deathSounds=["aliDeath"]
t.pickupSounds = aliSounds
t.fallSounds=["aliFall"]
t.style = 'ali'

# cyborg ###################################
t = Appearance("B-90001")
t.colorTexture = "cyborgColor"
t.colorMaskTexture = "cyborgColorMask"
t.defaultColor = (0.5, 0.5, 0.5)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cyborgIcon"
t.iconMaskTexture = "cyborgIconColorMask"
t.headModel =     "cyborgHead"
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

# Agent ###################################
t = Appearance("Agent Johnson1")
t.colorTexture = "agentColor"
t.colorMaskTexture = "agentColorMask"
t.defaultColor = (0.3, 0.3, 0.33)
t.defaultHighlight = (1, 0.5, 0.3)
t.iconTexture = "agentIcon"
t.iconMaskTexture = "agentIconColorMask"
t.headModel =     "agentHead"
t.torsoModel =    "agentTorso"
t.pelvisModel =   "agentPelvis"
t.upperArmModel = "agentUpperArm"
t.foreArmModel =  "agentForeArm"
t.handModel =     "agentHand"
t.upperLegModel = "agentUpperLeg"
t.lowerLegModel = "agentLowerLeg"
t.toesModel =     "agentToes"
agentSounds =    ['agent1', 'agent2', 'agent3', 'agent4']
agentHitSounds = ['agentHit1', 'agentHit2']
t.attackSounds = agentSounds
t.jumpSounds = agentSounds
t.impactSounds = agentHitSounds
t.deathSounds=["agentDeath"]
t.pickupSounds = agentSounds
t.fallSounds=["agentFall"]
t.style = 'agent'

# Jumpsuit ###################################
t = Appearance("Lee1")
t.colorTexture = "jumpsuitColor"
t.colorMaskTexture = "jumpsuitColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "jumpsuitIcon"
t.iconMaskTexture = "jumpsuitIconColorMask"
t.headModel =     "jumpsuitHead"
t.torsoModel =    "jumpsuitTorso"
t.pelvisModel =   "jumpsuitPelvis"
t.upperArmModel = "jumpsuitUpperArm"
t.foreArmModel =  "jumpsuitForeArm"
t.handModel =     "jumpsuitHand"
t.upperLegModel = "jumpsuitUpperLeg"
t.lowerLegModel = "jumpsuitLowerLeg"
t.toesModel =     "jumpsuitToes"
jumpsuitSounds = ['jumpsuit1', 'jumpsuit2', 'jumpsuit3', 'jumpsuit4']
jumpsuitHitSounds = ['jumpsuitHit1', 'jumpsuitHit2']
t.attackSounds = jumpsuitSounds
t.jumpSounds = jumpsuitSounds
t.impactSounds = jumpsuitHitSounds
t.deathSounds=["jumpsuitDeath"]
t.pickupSounds = jumpsuitSounds
t.fallSounds=["jumpsuitFall"]
t.style = 'spaz'

# ActionHero ###################################
t = Appearance("Todd McBurton1")
t.colorTexture = "actionHeroColor"
t.colorMaskTexture = "actionHeroColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "actionHeroIcon"
t.iconMaskTexture = "actionHeroIconColorMask"
t.headModel =     "actionHeroHead"
t.torsoModel =    "actionHeroTorso"
t.pelvisModel =   "actionHeroPelvis"
t.upperArmModel = "actionHeroUpperArm"
t.foreArmModel =  "actionHeroForeArm"
t.handModel =     "actionHeroHand"
t.upperLegModel = "actionHeroUpperLeg"
t.lowerLegModel = "actionHeroLowerLeg"
t.toesModel =     "actionHeroToes"
actionHeroSounds = ['actionHero1', 'actionHero2', 'actionHero3', 'actionHero4']
actionHeroHitSounds = ['actionHeroHit1', 'actionHeroHit2']
t.attackSounds = actionHeroSounds
t.jumpSounds = actionHeroSounds
t.impactSounds = actionHeroHitSounds
t.deathSounds=["actionHeroDeath"]
t.pickupSounds = actionHeroSounds
t.fallSounds=["actionHeroFall"]
t.style = 'spaz'

# Assassin ###################################
t = Appearance("Zola1")
t.colorTexture = "assassinColor"
t.colorMaskTexture = "assassinColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "assassinIcon"
t.iconMaskTexture = "assassinIconColorMask"
t.headModel =     "assassinHead"
t.torsoModel =    "assassinTorso"
t.pelvisModel =   "assassinPelvis"
t.upperArmModel = "assassinUpperArm"
t.foreArmModel =  "assassinForeArm"
t.handModel =     "assassinHand"
t.upperLegModel = "assassinUpperLeg"
t.lowerLegModel = "assassinLowerLeg"
t.toesModel =     "assassinToes"
assassinSounds = ['assassin1', 'assassin2', 'assassin3', 'assassin4']
assassinHitSounds = ['assassinHit1', 'assassinHit2']
t.attackSounds = assassinSounds
t.jumpSounds = assassinSounds
t.impactSounds = assassinHitSounds
t.deathSounds=["assassinDeath"]
t.pickupSounds = assassinSounds
t.fallSounds=["assassinFall"]
t.style = 'spaz'

# Wizard ###################################
t = Appearance("Grumbledorf1")
t.colorTexture = "wizardColor"
t.colorMaskTexture = "wizardColorMask"
t.defaultColor = (0.2, 0.4, 1.0)
t.defaultHighlight = (0.06, 0.15, 0.4)
t.iconTexture = "wizardIcon"
t.iconMaskTexture = "wizardIconColorMask"
t.headModel =     "wizardHead"
t.torsoModel =    "wizardTorso"
t.pelvisModel =   "wizardPelvis"
t.upperArmModel = "wizardUpperArm"
t.foreArmModel =  "wizardForeArm"
t.handModel =     "wizardHand"
t.upperLegModel = "wizardUpperLeg"
t.lowerLegModel = "wizardLowerLeg"
t.toesModel =     "wizardToes"
wizardSounds =    ['wizard1', 'wizard2', 'wizard3', 'wizard4']
wizardHitSounds = ['wizardHit1', 'wizardHit2']
t.attackSounds = wizardSounds
t.jumpSounds = wizardSounds
t.impactSounds = wizardHitSounds
t.deathSounds=["wizardDeath"]
t.pickupSounds = wizardSounds
t.fallSounds=["wizardFall"]
t.style = 'spaz'

# Cowboy ###################################
t = Appearance("Butch1")
t.colorTexture = "cowboyColor"
t.colorMaskTexture = "cowboyColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "cowboyIcon"
t.iconMaskTexture = "cowboyIconColorMask"
t.headModel =     "cowboyHead"
t.torsoModel =    "cowboyTorso"
t.pelvisModel =   "cowboyPelvis"
t.upperArmModel = "cowboyUpperArm"
t.foreArmModel =  "cowboyForeArm"
t.handModel =     "cowboyHand"
t.upperLegModel = "cowboyUpperLeg"
t.lowerLegModel = "cowboyLowerLeg"
t.toesModel =     "cowboyToes"
cowboySounds =    ['cowboy1', 'cowboy2', 'cowboy3', 'cowboy4']
cowboyHitSounds = ['cowboyHit1', 'cowboyHit2']
t.attackSounds = cowboySounds
t.jumpSounds = cowboySounds
t.impactSounds = cowboyHitSounds
t.deathSounds=["cowboyDeath"]
t.pickupSounds = cowboySounds
t.fallSounds=["cowboyFall"]
t.style = 'spaz'

# Witch ###################################
t = Appearance("Witch1")
t.colorTexture = "witchColor"
t.colorMaskTexture = "witchColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "witchIcon"
t.iconMaskTexture = "witchIconColorMask"
t.headModel =     "witchHead"
t.torsoModel =    "witchTorso"
t.pelvisModel =   "witchPelvis"
t.upperArmModel = "witchUpperArm"
t.foreArmModel =  "witchForeArm"
t.handModel =     "witchHand"
t.upperLegModel = "witchUpperLeg"
t.lowerLegModel = "witchLowerLeg"
t.toesModel =     "witchToes"
witchSounds =    ['witch1', 'witch2', 'witch3', 'witch4']
witchHitSounds = ['witchHit1', 'witchHit2']
t.attackSounds = witchSounds
t.jumpSounds = witchSounds
t.impactSounds = witchHitSounds
t.deathSounds=["witchDeath"]
t.pickupSounds = witchSounds
t.fallSounds=["witchFall"]
t.style = 'spaz'

# Warrior ###################################
t = Appearance("Warrior1")
t.colorTexture = "warriorColor"
t.colorMaskTexture = "warriorColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "warriorIcon"
t.iconMaskTexture = "warriorIconColorMask"
t.headModel =     "warriorHead"
t.torsoModel =    "warriorTorso"
t.pelvisModel =   "warriorPelvis"
t.upperArmModel = "warriorUpperArm"
t.foreArmModel =  "warriorForeArm"
t.handModel =     "warriorHand"
t.upperLegModel = "warriorUpperLeg"
t.lowerLegModel = "warriorLowerLeg"
t.toesModel =     "warriorToes"
warriorSounds =    ['warrior1', 'warrior2', 'warrior3', 'warrior4']
warriorHitSounds = ['warriorHit1', 'warriorHit2']
t.attackSounds = warriorSounds
t.jumpSounds = warriorSounds
t.impactSounds = warriorHitSounds
t.deathSounds=["warriorDeath"]
t.pickupSounds = warriorSounds
t.fallSounds=["warriorFall"]
t.style = 'agent'

# Superhero ###################################
t = Appearance("Middle-Man1")
t.colorTexture = "superheroColor"
t.colorMaskTexture = "superheroColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "superheroIcon"
t.iconMaskTexture = "superheroIconColorMask"
t.headModel =     "superheroHead"
t.torsoModel =    "superheroTorso"
t.pelvisModel =   "superheroPelvis"
t.upperArmModel = "superheroUpperArm"
t.foreArmModel =  "superheroForeArm"
t.handModel =     "superheroHand"
t.upperLegModel = "superheroUpperLeg"
t.lowerLegModel = "superheroLowerLeg"
t.toesModel =     "superheroToes"
superheroSounds =    ['superhero1', 'superhero2', 'superhero3', 'superhero4']
superheroHitSounds = ['superheroHit1', 'superheroHit2']
t.attackSounds = superheroSounds
t.jumpSounds = superheroSounds
t.impactSounds = superheroHitSounds
t.deathSounds=["superheroDeath"]
t.pickupSounds = superheroSounds
t.fallSounds=["superheroFall"]
t.style = 'spaz'

# Alien ###################################
t = Appearance("Alien1")
t.colorTexture = "alienColor"
t.colorMaskTexture = "alienColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "alienIcon"
t.iconMaskTexture = "alienIconColorMask"
t.headModel =     "alienHead"
t.torsoModel =    "alienTorso"
t.pelvisModel =   "alienPelvis"
t.upperArmModel = "alienUpperArm"
t.foreArmModel =  "alienForeArm"
t.handModel =     "alienHand"
t.upperLegModel = "alienUpperLeg"
t.lowerLegModel = "alienLowerLeg"
t.toesModel =     "alienToes"
alienSounds =    ['alien1', 'alien2', 'alien3', 'alien4']
alienHitSounds = ['alienHit1', 'alienHit2']
t.attackSounds = alienSounds
t.jumpSounds = alienSounds
t.impactSounds = alienHitSounds
t.deathSounds=["alienDeath"]
t.pickupSounds = alienSounds
t.fallSounds=["alienFall"]
t.style = 'spaz'

# OldLady ###################################
t = Appearance("OldLady1")
t.colorTexture = "oldLadyColor"
t.colorMaskTexture = "oldLadyColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "oldLadyIcon"
t.iconMaskTexture = "oldLadyIconColorMask"
t.headModel =     "oldLadyHead"
t.torsoModel =    "oldLadyTorso"
t.pelvisModel =   "oldLadyPelvis"
t.upperArmModel = "oldLadyUpperArm"
t.foreArmModel =  "oldLadyForeArm"
t.handModel =     "oldLadyHand"
t.upperLegModel = "oldLadyUpperLeg"
t.lowerLegModel = "oldLadyLowerLeg"
t.toesModel =     "oldLadyToes"
oldLadySounds =    ['oldLady1', 'oldLady2', 'oldLady3', 'oldLady4']
oldLadyHitSounds = ['oldLadyHit1', 'oldLadyHit2']
t.attackSounds = oldLadySounds
t.jumpSounds = oldLadySounds
t.impactSounds = oldLadyHitSounds
t.deathSounds=["oldLadyDeath"]
t.pickupSounds = oldLadySounds
t.fallSounds=["oldLadyFall"]
t.style = 'spaz'

# Gladiator ###################################
t = Appearance("Gladiator1")
t.colorTexture = "gladiatorColor"
t.colorMaskTexture = "gladiatorColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "gladiatorIcon"
t.iconMaskTexture = "gladiatorIconColorMask"
t.headModel =     "gladiatorHead"
t.torsoModel =    "gladiatorTorso"
t.pelvisModel =   "gladiatorPelvis"
t.upperArmModel = "gladiatorUpperArm"
t.foreArmModel =  "gladiatorForeArm"
t.handModel =     "gladiatorHand"
t.upperLegModel = "gladiatorUpperLeg"
t.lowerLegModel = "gladiatorLowerLeg"
t.toesModel =     "gladiatorToes"
gladiatorSounds =    ['gladiator1', 'gladiator2', 'gladiator3', 'gladiator4']
gladiatorHitSounds = ['gladiatorHit1', 'gladiatorHit2']
t.attackSounds = gladiatorSounds
t.jumpSounds = gladiatorSounds
t.impactSounds = gladiatorHitSounds
t.deathSounds=["gladiatorDeath"]
t.pickupSounds = gladiatorSounds
t.fallSounds=["gladiatorFall"]
t.style = 'spaz'

# Wrestler ###################################
t = Appearance("Wrestler1")
t.colorTexture = "wrestlerColor"
t.colorMaskTexture = "wrestlerColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "wrestlerIcon"
t.iconMaskTexture = "wrestlerIconColorMask"
t.headModel =     "wrestlerHead"
t.torsoModel =    "wrestlerTorso"
t.pelvisModel =   "wrestlerPelvis"
t.upperArmModel = "wrestlerUpperArm"
t.foreArmModel =  "wrestlerForeArm"
t.handModel =     "wrestlerHand"
t.upperLegModel = "wrestlerUpperLeg"
t.lowerLegModel = "wrestlerLowerLeg"
t.toesModel =     "wrestlerToes"
wrestlerSounds =    ['wrestler1', 'wrestler2', 'wrestler3', 'wrestler4']
wrestlerHitSounds = ['wrestlerHit1', 'wrestlerHit2']
t.attackSounds = wrestlerSounds
t.jumpSounds = wrestlerSounds
t.impactSounds = wrestlerHitSounds
t.deathSounds=["wrestlerDeath"]
t.pickupSounds = wrestlerSounds
t.fallSounds=["wrestlerFall"]
t.style = 'spaz'

# OperaSinger ###################################
t = Appearance("Gretel1")
t.colorTexture = "operaSingerColor"
t.colorMaskTexture = "operaSingerColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "operaSingerIcon"
t.iconMaskTexture = "operaSingerIconColorMask"
t.headModel =     "operaSingerHead"
t.torsoModel =    "operaSingerTorso"
t.pelvisModel =   "operaSingerPelvis"
t.upperArmModel = "operaSingerUpperArm"
t.foreArmModel =  "operaSingerForeArm"
t.handModel =     "operaSingerHand"
t.upperLegModel = "operaSingerUpperLeg"
t.lowerLegModel = "operaSingerLowerLeg"
t.toesModel =     "operaSingerToes"
operaSingerSounds =    ['operaSinger1', 'operaSinger2',
                        'operaSinger3', 'operaSinger4']
operaSingerHitSounds = ['operaSingerHit1', 'operaSingerHit2']
t.attackSounds = operaSingerSounds
t.jumpSounds = operaSingerSounds
t.impactSounds = operaSingerHitSounds
t.deathSounds=["operaSingerDeath"]
t.pickupSounds = operaSingerSounds
t.fallSounds=["operaSingerFall"]
t.style = 'spaz'

# Pixie ###################################
t = Appearance("Pixel1")
t.colorTexture = "pixieColor"
t.colorMaskTexture = "pixieColorMask"
t.defaultColor = (0, 1, 0.7)
t.defaultHighlight = (0.65, 0.35, 0.75)
t.iconTexture = "pixieIcon"
t.iconMaskTexture = "pixieIconColorMask"
t.headModel =     "pixieHead"
t.torsoModel =    "pixieTorso"
t.pelvisModel =   "pixiePelvis"
t.upperArmModel = "pixieUpperArm"
t.foreArmModel =  "pixieForeArm"
t.handModel =     "pixieHand"
t.upperLegModel = "pixieUpperLeg"
t.lowerLegModel = "pixieLowerLeg"
t.toesModel =     "pixieToes"
pixieSounds =    ['pixie1', 'pixie2', 'pixie3', 'pixie4']
pixieHitSounds = ['pixieHit1', 'pixieHit2']
t.attackSounds = pixieSounds
t.jumpSounds = pixieSounds
t.impactSounds = pixieHitSounds
t.deathSounds=["pixieDeath"]
t.pickupSounds = pixieSounds
t.fallSounds=["pixieFall"]
t.style = 'pixie'

# Robot ###################################
t = Appearance("Robot1")
t.colorTexture = "robotColor"
t.colorMaskTexture = "robotColorMask"
t.defaultColor = (0.3, 0.5, 0.8)
t.defaultHighlight = (1, 0, 0)
t.iconTexture = "robotIcon"
t.iconMaskTexture = "robotIconColorMask"
t.headModel =     "robotHead"
t.torsoModel =    "robotTorso"
t.pelvisModel =   "robotPelvis"
t.upperArmModel = "robotUpperArm"
t.foreArmModel =  "robotForeArm"
t.handModel =     "robotHand"
t.upperLegModel = "robotUpperLeg"
t.lowerLegModel = "robotLowerLeg"
t.toesModel =     "robotToes"
robotSounds =    ['robot1', 'robot2', 'robot3', 'robot4']
robotHitSounds = ['robotHit1', 'robotHit2']
t.attackSounds = robotSounds
t.jumpSounds = robotSounds
t.impactSounds = robotHitSounds
t.deathSounds=["robotDeath"]
t.pickupSounds = robotSounds
t.fallSounds=["robotFall"]
t.style = 'spaz'

# Bunny ###################################
t = Appearance("Easter Bunny1")
t.colorTexture = "bunnyColor"
t.colorMaskTexture = "bunnyColorMask"
t.defaultColor = (1, 1, 1)
t.defaultHighlight = (1, 0.5, 0.5)
t.iconTexture = "bunnyIcon"
t.iconMaskTexture = "bunnyIconColorMask"
t.headModel =     "bunnyHead"
t.torsoModel =    "bunnyTorso"
t.pelvisModel =   "bunnyPelvis"
t.upperArmModel = "bunnyUpperArm"
t.foreArmModel =  "bunnyForeArm"
t.handModel =     "bunnyHand"
t.upperLegModel = "bunnyUpperLeg"
t.lowerLegModel = "bunnyLowerLeg"
t.toesModel =     "bunnyToes"
bunnySounds =    ['bunny1', 'bunny2', 'bunny3', 'bunny4']
bunnyHitSounds = ['bunnyHit1', 'bunnyHit2']
t.attackSounds = bunnySounds
t.jumpSounds = ['bunnyJump']
t.impactSounds = bunnyHitSounds
t.deathSounds=["bunnyDeath"]
t.pickupSounds = bunnySounds
t.fallSounds=["bunnyFall"]
t.style = 'bunny'



###############  SPAZ   ##################
t = Appearance("S-117edited")

t.colorTexture = "warriorColor"
t.colorMaskTexture = "warriorColorMask"
t.iconTexture = "warriorIcon"
t.iconMaskTexture = "warriorIconColorMask"

t.defaultColor = (0.55, 0.55, 0.55)
t.defaultHighlight = (0.5, 0.5, 0.5)

t.headModel = "warriorHead"
t.torsoModel = "warriorTorso"
t.pelvisModel = "kronkPelvis"
t.upperArmModel = "warriorUpperArm"
t.foreArmModel = "warriorForeArm"
t.handModel = "warriorHand"
t.upperLegModel = "warriorUpperLeg"
t.lowerLegModel = "warriorLowerLeg"
t.toesModel = "warriorToes"

t.jumpSounds = ["warrior1","warrior2","warrior3"]
t.attackSounds = ["warrior1","warrior2","warrior3"]
t.impactSounds = ["warriorhit1",
                  "warriorhit2",]
t.deathSounds = ["warriorDeath","warrior4"]
t.pickupSounds = ["warrior3"]
t.fallSounds = ["warriorDeath","warrior4","warriorFall"]

t.style = 'agent'

