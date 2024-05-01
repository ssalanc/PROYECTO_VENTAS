class Product:
    next_id = 0  # Inicializamos el contador de IDs en 0
    
    def __init__(self, descrip="Ninguno", preci=0, stock=0):
        # Incrementamos el contador de IDs en 1 para cada nueva instancia
        Product.next_id += 1
        self.__id = Product.next_id  # Asignamos el ID único
        self.descrip = descrip
        self.preci = preci
        self.__stock = stock
    
    @property
    def id(self):
        return self.__id
    
    @property
    def stock(self):
        return self.__stock
    
    def getJson(self):
        return {"id": self.id, "descripcion": self.descrip, "precio": self.preci, "stock": self.stock}
    
