class M(object):
    
    def public(self):
        print('Use Tab to see me!')
        
    def _private(self):#Nonpupblic
        print("You won't be able to Tab to see me!")



m = M()
m.public()

m._private()
