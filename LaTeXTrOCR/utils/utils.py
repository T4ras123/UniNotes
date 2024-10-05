import torch
import random 
import os

"""All the universal and neceserry functions in one file
"""

def exist(val):
    return val is not None

def get_device(args, no_cuda=False):
    device = 'cpu'
    available_gpus = torch.cuda.device_count()
    args.gpu_devices = args.gpu_devices if args.get('gpu_devices', False) else list(range(available_gpus))
    if available_gpus > 0 and not no_cuda:
        device = 'cuda:%d' % args.gpu_devices[0] if args.gpu_devices else 0
    return device