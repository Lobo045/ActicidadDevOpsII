import os

class CustomerManager:
    def create_customer_file(self, customer_name, details):
        file_name = f"{customer_name}.txt"
        with open(file_name, 'w') as file:
            file.write(details)
        print(f"El cliente '{file_name}' se ha creado.")

    def edit_customer_file(self, customer_name, new_details):
        file_name = f"{customer_name}.txt"
        if os.path.exists(file_name):
            with open(file_name, 'w') as file:
                file.write(new_details)
            print(f"El cliente '{file_name}' ha sido editado.")
        else:
            print(f"El cliente '{file_name}' no existe.")

    def delete_customer_file(self, customer_name):
        file_name = f"{customer_name}.txt"
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"El cliente '{file_name}' se ha borrado")
        else:
            print(f"El cliente '{file_name}' no ha sido encontrado.")

def main():
    customer_manager = CustomerManager()

    while True:
        print("\n1. Crear un cliente")
        print("2. Editar un info sobre cliente")
        print("3. Borrar un cliente")
        print("4. Salir del programa")

        choice = input("Ingrese su eleccion(1-4): ")

        if choice == "1":
            customer_name = input("Favor de poner el nombre del cliente: ")
            details = input("Infromacion sobre el cliente: ")
            customer_manager.create_customer_file(customer_name, details)
        elif choice == "2":
            customer_name = input("Favor de poner el nombre del cliente: ")
            new_details = input("Ingrse la nueva infomacion del cliente: ")
            customer_manager.edit_customer_file(customer_name, new_details)
        elif choice == "3":
            customer_name = input("Favor de poner el nombre del cliente ")
            customer_manager.delete_customer_file(customer_name)
        elif choice == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Favor de ingresar un numero entre el 1 y el 4")

if __name__ == "__main__":
    main()