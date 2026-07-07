'''
En este archivo se guarda el objeto "tarea" contando con metodos getters y setters
para que el uso de los metodos sea mas comodo entre archivos

atributos del objeto: 
- id: Un identificador único para la tarea

- description: Una breve descripción de la tarea

- status: El estado de la tarea (Pendiente, En proceso, Hecha)

- createdAt: La fecha y hora en que se creó la tarea

- updatedAt: La fecha y hora en que se actualizó la tarea por última vez
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

    #getters, metodos "dame"
    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def status(self):
        return self._status

    @property
    def createdAt(self):
        return self._createdAt

    @property
    def updatedAt(self):
        return self._updatedAt
                 
    #setters, metodos "fija"
    @id.setter
    def id(self,nuevoId):
        self._id = nuevoId

    @description.setter
    def description(self,nuevaDescripcion):
        self._description = nuevaDescripcion

    @status.setter
    def status(self,nuevoStatus):
        self._status = nuevoStatus

    @createdAt.setter
    def createdAt(self, nuevafecha):
        self._createdAt = nuevafecha

    @updatedAt.setter
    def updatedAt(self, actualizacionFecha):
        self._updatedAt = actualizacionFecha

