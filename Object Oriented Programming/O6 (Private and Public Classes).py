print('OOP 6')
print('Importing class from other python file, public class, _private class')
print()

from ModPro import pub
var1 = pub('var1')
var1.display()
var1._display()

print ('We can also inport whole ModPro by: \n (but in this we need to put class name everytime)')

import ModPro
var3 = ModPro._pri('var3')
var3.display()

print()
print('OOP 7')