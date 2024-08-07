import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.backends.cudnn.version())
print(torch.version.cuda)
quit()