class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        initial_energy, current_energy = 0, 0
        for task in tasks:
            if current_energy < task[1]:
                initial_energy += task[1] - current_energy
                current_energy += task[1] - current_energy

            current_energy -= task[0]
            
        return initial_energy