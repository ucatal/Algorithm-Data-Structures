class M(object):
    
    def public(self):
        print ('Use Tab to see me!')
        
    def _private(self):
        print ("You won't be able to Tab to see me!")

if __name__=="__main__":
    m = M()
    m.public()
    m._private()