from tasks.test import pouet


def trigger_task_service(a: int, b: int):
    result = pouet.delay(a, b)  # Déclenche la tâche de manière asynchrone
    return {"message": f"Tâche démarrée avec ID {result.id}"}
