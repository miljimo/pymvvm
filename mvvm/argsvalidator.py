
class ArgsValidator(object):
    '''
      @ArgValidator : this validate the argument given to make sure
      that unexpected argument is given.
    '''
    def __init__(self,name,  expected_args:list):
        if(type(expected_args) != list):
            raise TypeError("@ArgValidator: expecting a first object of the variable names expected.");
        self.__expected_args  = expected_args
        self.__Name  =  name;

    @property
    def Name(self):
        return self.__Name;

    @property
    def Args(self):
        return self.__expected_args;

    def Valid(self, **kwargs):
        for key in kwargs:
            if( key in self.__expected_args) is not True:
                raise ValueError("{1} : Unknown '{0}' argument provided".format(key, self.Name))
        return True;
