class Tecnologia:
    
    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca
        
    def get_voltaje(self):
        return self.__voltaje
    
    def get_precio(self):
        return self.__precio    
    
    def get_eficiencia(self):
        return self.__eficiencia
    
    def get_marca(self):
        return self.__marca
    
    
    def set_voltaje(self,voltaje):
        self.__voltaje = voltaje
        
    def set_precio(self,precio):
        self.__precio = precio
        
    def set_eficiencia(self,eficiencia):
        self.__eficiencia = eficiencia
        
    def set_marca(self,marca):
        self.__marca = marca           
        
        
    def calcular_descuento(self):
        if self.__eficiencia =="A" or self.__eficiencia=="B":
            des1 = self.__precio * 0.5
            return des1
            
        elif self.__eficiencia =="C" or self.__eficiencia=="D":
            des2 = self.__precio * 0.3
            return des2
            
        elif self.__eficiencia =="E" or self.__eficiencia=="F":
            des3 = self.__precio * 0.1    
            return des3
            
            
    def imprimir_caracteristicas(self):
        return f'\n Marca:{self.__marca} \n Volatje: {self.__voltaje} \n Precio: {self.__precio} \n Eficiencia: {self.__eficiencia}'        

