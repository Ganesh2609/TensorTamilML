import pandas as pd
import torch 
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split


class ParametricDataset(Dataset):

    def __init__(self, csv_path):
        super(ParametricDataset, self).__init__()
        data = pd.read_csv(csv_path)
        self.x = torch.tensor(data.loc[:, ['x']].to_numpy(), dtype=torch.float32).reshape(1500)
        self.y = torch.tensor(data.loc[:, ['y']].to_numpy(), dtype=torch.float32).reshape(1500)
        self.t = torch.linspace(6, 60, 1500+2)[1:-1]

    def __len__(self):
        return self.x.shape[0]
    
    def __getitem__(self, idx):
        return {
            't' : self.t[idx],
            'x' : self.x[idx],
            'y' : self.y[idx]
        }
    

def get_dataloaders(csv_path:str, batch_size:int=32, train_size=0.8, num_workers:int=12, prefetch_factor:int=2):

    data = ParametricDataset(csv_path=csv_path)
    train_size = int(train_size * len(data))
    test_size = len(data) - train_size
    train_data, test_data = random_split(data, [train_size, test_size])

    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True, drop_last=True)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False, drop_last=True)
    
    # train_loader = DataLoader(
    #     train_data,
    #     batch_size=batch_size,
    #     shuffle=True,
    #     num_workers=num_workers, 
    #     pin_memory=True, 
    #     persistent_workers=True, 
    #     prefetch_factor=prefetch_factor
    # )
    # test_loader = DataLoader(
    #     test_data,
    #     batch_size=batch_size,
    #     shuffle=False,
    #     num_workers=num_workers, 
    #     pin_memory=True, 
    #     persistent_workers=True, 
    #     prefetch_factor=prefetch_factor
    # )

    return train_loader, test_loader