from events import Event, EventHandler;
from dispatchers import DispatcherObject;
from localisation import Resource, ResourceParser;

class PropertyChangedEventArgs(Event):

    def __init__(self, source,  propertyName:str):
        super().__init__("property.changed.event.args")
        if hasattr(source , "__class__") is not True:
           raise TypeError("@Expecting an  class object but {0} given",format(type(source)));           
        if(type(propertyName) != str):
            raise TypeError("@Expecting a string value on parameter 2");
        self.__Source        =  source;
        self.__PropertyName  =  propertyName;
        self.__Type  =  type(getattr(self.__Source, self.__PropertyName))

    @property
    def Type(self):
        return self.__Type;                             
                             
    @property
    def Source(self):
        return self.__Source;

    @property
    def PropertyName(self):
        return self.__PropertyName;
    
    @property
    def Value(self):
        result = None    
        if(hasattr(self.Source, self.PropertyName) is True):
            result =  getattr(self.Source, self.PropertyName);
        return result;

    @Value.setter
    def Value(self, value:object):
        if(type(value) !=  self.Type):
            raise TypeError("@Property: expecting a type of {0} ".format(self.Type));
        if(value != self.Value):
            setattr(self.Source, self.PropertyName, value);
            
        
            

class ViewModelBase(DispatcherObject):

    def __init__(self, parent:DispatcherObject, resource: Resource):
        if(parent is not None):
            if(isinstance(parent , ViewModelBase) is not True):
                raise TypeError("@ViewModelbase: paremeter 1 expecting a ViewModelBase as a parameter");
        if(resource is not None):
            if(isinstance(resource, Resource) is not True):
                raise TypeError("@ViewModelBase: paramerter 2 expecting a resource object");
        self.__Parent   =  parent;
        self.__Resource =  resource;
        self.__PropertyChanged = EventHandler();

    @property
    def PropertyChanged(self):
        return self.__PropertyChanged;

    @PropertyChanged.setter
    def PropertyChanged(self, handler:EventHandler):
        if(handler != self.__PropertyChanged):
            raise TypeError("@PropertyChanged: you can not set the propertychanged object")
        self.__PropertyChanged  = handler;

    @property
    def Parent(self):
        return self.__Parent;

    @property
    def Resource(self):
        return self.__Resource;

    
    def Localise(self, key:str, default_value =  None):
        result  =  default_value;

        if type(key) == str:
            if self.Resource is not None:
               result =  self.Resource.Get(key, default_value);
        return result;

    def _RaisePropertyChanged(self, propertyName:str):
        if(type(propertyName) != str):
            raise TypeError("@propertyName : must be a string type");
        if(self.PropertyChanged is not None):
            self.PropertyChanged(PropertyChangedEventArgs(self, propertyName));


if __name__ =="__main__":
    
    def NameChanged(evt):
        print(evt.Value)
        evt.Value ="12"
        print(evt);

    class PersonViewModel(ViewModelBase):

        def __init__(self, resource):
            super().__init__(None, resource);
            self.__Name  ="";

        @property
        def Name(self):
            return self.__Name;

        @Name.setter
        def Name(self, name):
            if(name != self.__Name):
                self.__Name =  name;
                self._RaisePropertyChanged("Name");

            
    RESOURCE_FILE ="../bin/res.js"
    parser      =  ResourceParser(filename  = RESOURCE_FILE)
    resource    =  parser.Parse();
    viewmodel   =  PersonViewModel(resource);
    viewmodel.PropertyChanged += NameChanged;
    viewmodel.Name  =  viewmodel.Localise("application.text","no test");
    print(viewmodel);
    print(viewmodel.Name);
    
