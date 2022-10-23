from Tecnologia import Tecnologia


class TV(Tecnologia):
    
    def __init__(self,voltaje:str,precio:float,eficiencia:str,marca:str,tamano:float):
      super().__init__(voltaje,precio,eficiencia,marca)
      self.__tamano = tamano
    
      
    def get_tamano(self):
        return self.__tamano
    
    def set_tamano(self,tamano):
        self.__tamano = tamano
        
    def imprimir_caracteristicas(self):
      return f'\n TV: {super().__str__()} \n Tamaño:{self.__tamano}' 

    def valor_total(self):
      total = self.get_precio() - super().calcular_descuento()
      print(f'El valor con descueto es de: {total}')

