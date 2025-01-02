"""
import uasyncio as asyncio
async def task_function(name):
    while True:
        print('Task', name, 'is running')
        await asyncio.sleep(1)

async def main():
    # Planifier l'exécution des tâches
    task1 = asyncio.create_task(task_function('A'))
    task2 = asyncio.create_task(task_function('B'))

# Attendre la complétion des tâches (ici elles bouclent indéfiniment)
    await task1
    await task2

# Démarrer la boucle d'événements
asyncio.run(main())
"""
