# Defining the model:

import torch
from torch import nn # allows you to access custom layers, such as Linear, Sigmoid etc..
class LogisticRegression(nn.Module):
    def __init__(self, in): # define the model as a class
        super().__init__() # initialization method with parameters
        self.log_reg = nn.Sequential( # define the architecture
            # note that nn.Sequential is to build your custom order and set of functions
            nn.Linear(in, 1),
            nn.Sigmoid()
        )
    def forward(self, x):
        return self.log_reg(x) # forward pass of the model using inputs x

model = LogisticRegression(16) # initialization of your model

criterion = nn.BCELoss() # loss function

optimizer = torch.optim.SGD(model.paramters(), lr = 0.01) # optimizer

for t in range(n_epochs):
    y_pred = model(x)
    loss = criterion(y_pred, y)
    optimizer.zero_grad() #zeroes the gradients
    loss.backward()
    optimizer.step()




