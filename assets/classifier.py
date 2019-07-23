import torch
from torch import nn, optim
from torchvision import datasets, transforms
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

# Load the data
transform = transforms.Compose([transforms.ToTensor(),  transforms.Normalize([0.5], [0.5])])
trainset = datasets.MNIST("~/.pytorch/MNIST_data/", download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# define your neural network
model = nn.Sequential(nn.Linear(784, 128), nn.ReLU(), nn.Linear(128, 64), nn.ReLU(), nn.Linear(64, 10), nn.LogSoftmax(dim = 1))
criterion = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr = 0.01)

# Train the neural network
epochs = 5
for e in range(epochs):
    running_loss = 0
    for images, lables in trainloader:
        # images, lables = images.to(device), lables.to(device)
        images = images.view(images.shape[0], -1)
        optimizer.zero_grad()
        output = model.forward(images)
        loss = criterion(output, lables)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    else:
        print(f"Training loss: {running_loss/len(trainloader)}")
