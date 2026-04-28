import kagglehub, os
from torchvision import datasets, transforms
import tensorflow as tf



path = kagglehub.dataset_download("aklimarimi/8-facial-expressions-for-yolo")
print("Path to dataset files:", path)

