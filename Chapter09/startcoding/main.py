# 1. import 패키지.모듈
import unit.character
unit.character.test()

# 2. from 패키지 import 모듈
from unit import item
item.test()

# 3. import 패키지 *
from unit import *
character.test()

# 4. import 패키지
import unit
unit.character.test()
unit.item.test()
unit.monster.test()
