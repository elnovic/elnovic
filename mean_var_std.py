import numpy as np

def calculate(list):
    # Vérification du nombre d’éléments
    if len(list) != 9:
        raise ValueError("La liste doit contenir neuf numéros")
    
    # Conversion en tableau numpy 3x3
    arr = np.array(list).reshape(3, 3)
    
    # Calculs
    calculations = {
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean().item()],
        'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var().item()],
        'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std().item()],
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max().item()],
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min().item()],
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum().item()]
    }
    
    return calculations
