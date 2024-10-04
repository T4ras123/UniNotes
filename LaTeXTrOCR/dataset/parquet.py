import parquet
import torch
import os
import PIL
import imagesize
import io
import base64
import pandas as pd

ds = pd.DataFrame()

def parquet_to_tuple(path=None) -> pd.DataFrame:
    """Convert parquet file to pandas dataframe 
    and convert bytes to a string of pixel values (H,W,C)

    Args:
        path (str, optional): path to the parquet file. Defaults to None.

    Returns:
        pd.DataFrame: str of pixel values in the "image" column and LaTex in the "text" one
    """
    ds = pd.DataFrame(columns=['image', 'text'])
    if path is not None:
        dataset = pd.read_parquet(path)
        for i in range(len(dataset.index)):
            try:
                base64_bytes = dataset['image'][i]["bytes"]
                base64_string = base64_bytes.decode('latin1') 
                missing_padding = len(base64_string) % 4
                if missing_padding:
                    base64_string += '=' * (4 - missing_padding)
                
                image_data = base64.b64decode(base64_string)
                
                ds = pd.concat([ds, pd.DataFrame({'image': [image_data], 'text': [dataset['text'][i]]})], ignore_index=True)
            except (base64.binascii.Error, KeyError, UnicodeDecodeError) as e:
                print(f"Error decoding base64 or missing key: {e}")
    
    return ds

ds1 = parquet_to_tuple('/home/vover/Vova/Github/UniNotes/data/external/LaTeXOCR-val-human_handwrite_print.parquet')