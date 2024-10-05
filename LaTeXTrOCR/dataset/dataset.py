import torch 
import torch.nn as nn 
import torch.functional as F
import os
from typing import Tuple
import argparse
import numpy 
import imagesize 
import logging
import glob
import cv2
from tqdm.auto import tqdm
from os.path import join
from collections import defaultdict


from LaTeXTrOCR.utils.utils import *
from LaTeXTrOCR.dataset.transforms import train_transform, test_transform


class Img2LaTeXDataset:
    """Dataset class for the model that converts input data to torch vectors
    """

    data = defaultdict(lambda:[]) 
    
    def __init__(self, equations=None, images=None, tokenkizer=None, shuffle=True, batchsize=16, max_seq_len=1024,
                 max_dimentions=(1024, 512), min_dimentions=(32,32), pad = False, keep_smaller_batches=False, test=False):
        
        if images is not None and equations is not None:
            assert tokenkizer is not None
            self.images = [path.replace("\\", "/") for path in glob.glob(join(images, '*.png'))]
            self.sample_size = len(self.images)
            eqs = os.open(equations, 'r').read().split('\n')
            self.shuffle = shuffle
            self.batch_size = batchsize
            self.max_seq_len = max_seq_len
            self.max_dimentions = max_dimentions
            self.min_dimentions = min_dimentions
            self.pad = pad
            self.keep_smaller_batches = keep_smaller_batches
            self.test = test
            try:
                for i, im in tqdm(enumerate(self.images), total=len(self.images)):
                    H, W = imagesize.get(im)
                    if min_dimentions[0] <= H <= max_dimentions[0] and min_dimentions[1] <= W <= max_dimentions[1]:
                        self.data[(W, H)].append((eqs[self.indices[i]], im))
            except KeyboardInterrupt:
                pass
            self.data = dict(self.data)
            self._get_size()
            iter(self)
                    
    def __len__(self):
        return self.size