
import os
import math
import pandas as pd
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler
from utils.constant import DATASET_DIRECTORY, FEATURES, LABELS

def fit_dataset(n_files, attck_type, transforms=StandardScaler()):

    # File Paths
    df_sets = [k for k in os.listdir(DATASET_DIRECTORY) if k.endswith('.csv')]
    df_sets.sort()

    # Split
    train_sets = df_sets[:n_files]
    test_sets = df_sets[n_files:math.ceil(n_files*1.3)]

    # Training data
    train_df = pd.DataFrame()
    for train_set in tqdm(train_sets):
        df_set = pd.read_csv(DATASET_DIRECTORY + train_set)
        train_df = train_df._append(df_set, ignore_index=True)

        # Fit scaler
        transforms.fit(df_set[FEATURES])

    # Testing data
    test_df = pd.DataFrame()
    for test_set in tqdm(test_sets):
        df_set = pd.read_csv(DATASET_DIRECTORY + test_set)
        test_df = test_df._append(df_set, ignore_index=True)

    # Clean data
    train_df = train_df.dropna()
    train_df = train_df.drop_duplicates()
    train_df = train_df.reset_index(drop=True)
    test_df = test_df.dropna()
    test_df = test_df.drop_duplicates()
    test_df = test_df.reset_index(drop=True)

    # Scale
    train_df[FEATURES] = transforms.transform(train_df[FEATURES])
    test_df[FEATURES] = transforms.transform(test_df[FEATURES])

    # Encode labels
    train_df[LABELS] = train_df[LABELS].apply(lambda x: attck_type[x])
    test_df[LABELS] = test_df[LABELS].apply(lambda x: attck_type[x])
    
    return train_df, test_df