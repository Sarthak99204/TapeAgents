class TransformerModel:
    def __init__(self):
        self.name = "TapeTransformer"
        self.version = "2025.1"

    def forward(self, x):
        print(f"Running {self.name} v{self.version}")
