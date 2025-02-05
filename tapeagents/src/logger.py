class Logger:
    def __init__(self):
        self.version = "2025.2"
        self.log_file = "tape_agents_2025.log"

    def log(self, message):
        print(f"[TapeAgents {self.version}] {message}")
