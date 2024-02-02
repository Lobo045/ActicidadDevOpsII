import os

class FileManager:
    def __init__(self):
        self.hash_table = {}

    def create_file(self, file_type, name, details, associated_customer=None):
        file_name = f"{name}_{file_type}.txt"
        with open(file_name, 'w') as file:
            file.write(details)
        print(f"{file_type} archivo '{file_name}' ha sido creado!")

        if associated_customer:
            self.associate_customer_project(associated_customer, name)

    def edit_file(self, file_type, name, new_details):
        file_name = f"{name}_{file_type}.txt"
        if os.path.exists(file_name):
            with open(file_name, 'w') as file:
                file.write(new_details)
            print(f"{file_type} archivo '{file_name}' ha sido editado.")
        else:
            print(f"{file_type} archivo '{file_name}' no encontrado.")

    def delete_file(self, file_type, name):
        file_name = f"{name}_{file_type}.txt"
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_type} archivo '{file_name}' ha sido borrado")
        else:
            print(f"{file_type} archivo '{file_name}' no ha sido encontrado.")

    def associate_customer_project(self, customer_name, project_name):
        if customer_name not in self.hash_table:
            self.hash_table[customer_name] = [project_name]
        else:
            self.hash_table[customer_name].append(project_name)
        print(f"El Cliente '{customer_name}' ahora esta asociado con el proyecto '{project_name}'.")

    def display_associations(self):
        print("\nCustomer-Project Associations:")
        for customer, projects in self.hash_table.items():
            print(f"{customer}: {projects}")


def main():
    file_manager = FileManager()

    while True:
        print("\n1. Crear un cliente")
        print("2. Editar archvio del cliente")
        print("3. Borrar archivo del cliente")
        print("4. Crear proyecto")
        print("5. Editar archivo del proyecto")
        print("6. Borrar archivo")
        print("7. Ver poyectos y clientes")
        print("8. Salir")

        choice = input("Escoja una opcion (1-8): ")

        if choice == "1":
            file_type = "customer"
            name = input("Cual es el nombre del cliente: ")
            details = input("Ingresa detalles sobre el cliente: ")
            file_manager.create_file(file_type, name, details)
        elif choice == "2":
            file_type = "customer"
            name = input("Ingrese el nombre del cliente: ")
            new_details = input("Ingrese el nuevo detalle del client: ")
            file_manager.edit_file(file_type, name, new_details)
        elif choice == "3":
            file_type = "customer"
            name = input("Ingrse el nombre del cliente que desea borrar: ")
            file_manager.delete_file(file_type, name)
        elif choice == "4":
            file_type = "project"
            name = input("Ingrese el nombre del proyecto: ")
            details = input("Ingrese detalles sobre el proyecto: ")
            customer_name = input("Ingrese el nombre del cliente asociado con el proyecto: ")
            file_manager.create_file(file_type, name, details, customer_name)
        elif choice == "5":
            file_type = "project"
            name = input("Ingrese en el proyecto: ")
            new_details = input("Ingrese el nuevo detalle del proyecto: ")
            file_manager.edit_file(file_type, name, new_details)
        elif choice == "6":
            file_type = "project"
            name = input("Ingrese el nombre del proyecto que desea borrar: ")
            file_manager.delete_file(file_type, name)
        elif choice == "7":
            file_manager.display_associations()
        elif choice == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Favor de elegir un numero del 1 al 8!")

if __name__ == "__main__":
    main()
    
