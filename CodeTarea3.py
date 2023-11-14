allocated_memory = []
try:
    while True:
        # Asigna y retiene 1 MB de memoria
        allocated_memory.append(' ' * (1024 * 1024))
        print(f"Asignados {len(allocated_memory)} MB de memoria")
        time.sleep(1)
except MemoryError:
    print("Error: No se pudo asignar más memoria")
