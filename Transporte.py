class Transporte:
    
    def __init__(self):
        self.__COSTODESPACHOBASE = 4000
        
    def get_COSTODESPACHOBASE(self):
        return self.__COSTODESPACHOBASE    
    
    
    def set_COSTODESPACHOBASE(self,COSTODESPACHOBASE):
        self.__COSTODESPACHOBASE = COSTODESPACHOBASE
        
        
    def calcularDespacho(self):
        self.__COSTODESPACHOBASE = 4000 
        return self.__COSTODESPACHOBASE    