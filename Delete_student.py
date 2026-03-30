def Delete_student(students_list):
    if not students_list:
        print('The student list is empty.')
        return

    # 1. Mostramos la lista con sus IDs para que el usuario sepa cuál elegir
    print("\n--- Current List ---")
    for i, student in enumerate(students_list):
        print(f"{i + 1}. {student['name']}")

    try:
        # 2. Convertimos el input a número y restamos 1 (porque las listas empiezan en 0)
        student_id = int(input('\nEnter the ID (number) of the student to delete: ')) - 1
        
        # 3. Validamos que el ID exista en el rango de la lista
        if 0 <= student_id < len(students_list):
            # Usamos .pop() para eliminar por posición
            removed_student = students_list.pop(student_id)
            print(f"Student '{removed_student['name']}' successfully deleted.")
        else:
            print("Error: That ID number does not exist.")
            
    except ValueError:
        print('Error: Please enter a valid NUMBER, not text.')
