
def calcular_progreso(total, completadas):
    if total == 0:
        return 0
    return (completadas / total) * 100


def mostrar_tareas(tareas):
    for tarea in tareas:
        print("Tarea:", tarea["nombre"])
        print("Estado:", tarea["estado"])


def agregar_tarea(tareas, nombre):
    tarea = {"nombre": nombre, "estado": "Pendiente"}
    tareas.append(tarea)
    return tareas


if __name__ == "__main__":
    tareas = []
    agregar_tarea(tareas, "Leer el material")
    agregar_tarea(tareas, "Entregar actividad")

    mostrar_tareas(tareas)
    print("Progreso:", calcular_progreso(2, 1), "%")
