from mvvm.argsvalidator import ArgsValidator


class ArgsInitialiser(object):

    def __init__(self, **kwargs):
        self.__Kwargs     =  kwargs;
        expected_args =  self.__GetExpectedArguments(kwargs);
        self.__Validator  =  ArgsValidator("args",expected_args);
        
    def Initial(self, field , value):
        if(type(field) != str):
            raise TypeError("@Initial: expecting a string field")
        else:
            if(field in self.__Kwargs) is not True:
                self.__Kwargs[field] = value;
    @property
    def Arguments(self):
        return self.__Kwargs;
    
    @property
    def Validator(self):
        return self.__Validator;


    def __GetExpectedArguments(self, args:dict):
         return  list(args.keys());


if __name__ =="__main__":

    initialiser  =  ArgsInitialiser(name  =  "Obaro", age =87)
    print(initialiser.Arguments)
    print(initialiser.Validator.Valid(status  = False));
    
