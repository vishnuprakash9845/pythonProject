class A:
    i=10            #public
    __j=20          #private-- to hide it from outside

    def getJ(self):
        return self.__j
