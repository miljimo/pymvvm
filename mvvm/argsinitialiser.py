

class ArgsInitialiser(object):

    def __init__(self, **kwargs):
        self.__Kwargs  =  kwargs;
        
    def Initial(self, field , value):
        if(type(field) != str):
            raise TypeError("@Initial: expecting a string field")
        else:
            if(field in self.__Kwargs) is not True:
                self.__Kwargs[field] = value;
    @property
    def Arguments(self):
        return self.__Kwargs;
