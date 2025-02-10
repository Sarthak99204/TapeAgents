import torch

class ModelTrainer:
    def __init__(self):
        self.version = "2025.2.1"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def train(self, model, data):
        print(f"Training model on {self.device} with version {self.version}")
