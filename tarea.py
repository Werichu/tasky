#En este archivo se guarda el objeto "tarea", con todas sus propiedades
'''
id: Un identificador único para la tarea

description: Una breve descripción de la tarea

status: El estado de la tarea (Pendiente, En proceso, Hecha)

createdAt: La fecha y hora en que se creó la tarea

updatedAt: La fecha y hora en que se actualizó la tarea por última vez
'''

class Tarea: 
    #CONSTRUCTOR 
    def __init__(self, id, description, status, createdAt, updatedAt):       
#atributos del objeto "_" son variables de instancia privada, se definen mediante lo que reciben fuera del objeto
        self._id = id
        self._description = description
        self._status = status
        self._createdAt = createdAt
        self._updatedAt = updatedAt
        
    #metodos "dame"
    def getId(self):
        return self._id
    
    def getDescription(self):
        return self._description
    
    def getStatus(self):
        return self._status
    
    def getCreatedAt(self):
        return self._createdAt
    
    def getUpdateAt(self):
        return self._updatedAt
    
    #metodos "fija"
    #si se recibe algun valor de una variable publica, esta se fijara en los atributos privados del objeto
    def setId(self,valor):
        self._id = valor
        
    def setDescription(self,valor):
        self._description = valor
    
    def setStatus(self,valor):
        self._status = valor
        
    def setCreatedAt(self,valor):
        self._createdAt = valor
        
    def setUpdateAt(self,valor):
        self._updatedAt = valor
        