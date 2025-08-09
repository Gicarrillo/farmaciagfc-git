class Paciente:
    def __init__(self, paciente_id, nombre, edad):
        self.paciente_id = paciente_id
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        return f"Paciente {self.nombre} (ID: {self.paciente_id}), edad: {self.edad}"

if __name__ == "__main__":
    p = Paciente(501, "Yoselin",18)
    print(p.datos())
