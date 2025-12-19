import torch 
from torch import nn

class ParametricModel(nn.Module):

    def __init__(self):
        super(ParametricModel, self).__init__()
        # 0° < theta < 50°
        # -0.05 < M < 0.05
        # 0 < X < 100
        theta = torch.tensor(25, dtype=torch.float32)
        M = torch.tensor(0, dtype=torch.float32)
        X = torch.tensor(50, dtype=torch.float32)
        self.theta = nn.Parameter(theta)
        self.M = nn.Parameter(M)
        self.X = nn.Parameter(X)

    def clamp_params(self):
        self.theta.clamp_(0, 50)
        self.M.clamp_(-0.05, 0.05)
        self.X.clamp_(0, 100)
    
    def print_params(self):
        print(f'Theta: {self.theta}\nM: {self.m}\nX: {self.X}')
        return self.theta, self.M, self.X
    
    def forward(self, t):
        """
        Compute x and y values for given t values
        x = (t * cos(θ) - e^(M|t|) * sin(0.3t) * sin(θ) + X)
        y = (42 + t * sin(θ) + e^(M|t|) * sin(0.3t) * cos(θ))
        """
        cos_t = torch.cos(torch.deg2rad(self.theta))
        sin_t = torch.sin(torch.deg2rad(self.theta))
        sin_3t = torch.sin(0.3 * t)
        exp_term = torch.exp(self.M * torch.abs(t))

        x = t * cos_t - exp_term * sin_3t * sin_t + self.X
        y = 42 + t * sin_t + exp_term * sin_3t * cos_t

        return x, y
        
