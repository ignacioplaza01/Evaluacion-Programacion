from Tecnologia import Tecnologia


class Consola(Tecnologia):
    
    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str,nomConsola:str,version:str):
        super().__init__(voltaje,precio,eficiencia,marca)
        self.__nomConsola = nomConsola
        self.__version = version
        
    def get_nomConsola(self):
        return self.__nomConsola
    
    def get_version(self):
        return self.__version
    
    
    def set_nomConsola(self,nomConsola):
        self.__nomConsola = nomConsola
        
    def set_version(self,version):
        self.__version = version
        
        
    def calcular_descuento(self):
        
        if self.__version=="lite":
            descuentoLite = self.get_precio() * 0.05
            costoDescuento = self.get_precio()- descuentoLite     
            costo_total =  costoDescuento - super().calcular_descuento()
            print(f'El costo total es: ${costo_total}')
        
        elif self.__version=="normal":
            descuento = self.get_precio() - super().calcular_descuento()
            print(f'El costo total es: {descuento}')

        else:
            print("Valor no valido")    

       
                 
                    
                    
    def imprimir_carecteristicas(self):
        return f'\n Consola: {super().__str__()} \n Nombre consola:{self.__nomConsola} \n Version:{self.__version}'                