from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost, estimate_completion):
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y')
        self.priority = priority
        self.cost = cost
        self.estimate_completion = estimate_completion

    def __str__(self):
        return f"Project: {self.name}\nStart Date: {self.start_date.strftime('%d/%m/%Y')}\nPriority: {self.priority}\nCost: {self.cost}\nEstimate Completion: {self.estimate_completion}%"

    def update_completion(self, new_completion):
        self.estimate_completion = new_completion

    def update_priority(self, new_priority):
        self.priority = new_priority
