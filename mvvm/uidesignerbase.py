import os;
from localisation import  ResourceParser, Resource


class UIDesignerBase(object):

    def __init__(self, window: object, filename : str  =  None):
        if(hasattr(window, '__class__') is not True):
            raise TypeError("@UIDesignerBase: expecting an object for parent but {0} given".format(type(window)));
        self.__Window      =  window;
        self.__Filename    =  filename;
        self.__Resource    =  None
        if(self.__Filename is  not None):
            if(type(self.__Filename) != str):
                raise TypeError("@Expecting a filename of type string");
            else:
                if(os.path.exists(self.__Filename) is not True):
                     raise TypeError("@Resource file {0} does not exists".format(self.__Filename));
                    
        if(os.path.exists(self.__Filename)):
            uiparser  =  ResourceParser(filename  =  self.__Filename);
            self.__Resource  =  uiparser.Parse();
        
            
        # Load the RAII
        self.InitialiseUI(self.__Window);
        self.ReTranslateUI();

    @property
    def Resource(self):
        return self.__Resource;

    @property
    def Window(self):
        return self.__Window;

    def Localise(self, key:str , default_value:object):
        result =  default_value;
        if(type(key) != str):
            raise TypeError("@Localise: key must be a string type");
        if( self.__Resource is  not None):
             result  = self.__Resource.Get(key, default_value);
        return result;

    def InitialiseUI(self , window: object):
        raise NotImplementedError("@InitialiseUI must be implemented");

    def ReTranslateUI(self):
        '''
            Localisation of the UI
            Call this everything the UI resource change
        '''
        raise NotImplementedError("@ReTranslateUI must be implemented");
        
        

if(__name__ =="__main__"):
    RESOURCE_FILE ="../bin/res.js"
    class TestUIDesigner(UIDesignerBase):
        def __init__(self, filename =  RESOURCE_FILE):
            super().__init__( object(), filename);

        def InitialiseUI(self , window: object):
            pass;

        def ReTranslateUI(self):
            print(self.Resource.Get("application.text", "Nothing"));
            print("Retranslated UI");
            
            
    ui  =  TestUIDesigner();
