import torch

import utilities.utils as utils


def mse(input_tensor: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """TODO: implement this method"""
    squared_error = torch.square(input_tensor - target)
    return torch.mean(squared_error)
