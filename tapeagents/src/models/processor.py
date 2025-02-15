import torch
import numpy as np

class DataProcessor:
    def __init__(self):
        self.version = "2025.2"

    def process_batch(self, data):
        print(f"Processing data with version {self.version}")
