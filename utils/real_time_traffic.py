import sys
sys.path.append('../')

import pandas as pd
from scapy.all import *
from joblib import load
from constant import FEATURES
from sklearn.preprocessing import StandardScaler
from features.feature_extraction import Feature_extraction

def print_pkt(pkt):

    # Declare global variables
    global total
    global ip
    global model
    global attacker
    global TP, FP, TN, FN

    total += 1
    print(total)

    try:
        if pkt[IP].src == ip:
            attacker += 1

        wrpcap('../inputs/sniffed.pcap', pkt)
        
        pcapfiles = [
        '../inputs/sniffed.pcap',
        ]
        destination_directory = '../outputs/'
        df = pd.DataFrame()
        for i in range(len(pcapfiles)):
            pcap_file = pcapfiles[i]
            fe = Feature_extraction()
            df = fe.pcap_evaluation(pcap_file,destination_directory + pcap_file)

        scaler = StandardScaler()
        scaler.fit(df[FEATURES])
        df[FEATURES] = scaler.transform(df[FEATURES])

        pred = model.predict(df[FEATURES])
        
        if pred[0] == 1 and pkt[IP].src == ip:
            TP += 1
        elif pred[0] == 1 and pkt[IP].src != ip:
            FP += 1
        elif pred[0] == 0 and pkt[IP].src == ip:
            FN += 1
        elif pred[0] == 0 and pkt[IP].src != ip:
            TN += 1

    except:
        pass


if __name__ == '__main__':

    # Declare global variables
    global total, attacker
    global model
    global ip
    global TP, FP, TN, FN

    # Initialize variables
    total, attacker, TP, FP, TN, FN = 0, 0, 0, 0, 0, 0
    print('Loading model...')
    model = load('../outputs/best_model_syn_attacks.joblib')
    count = 1000
    ip = "192.168.75.221"

    # Sniff
    print('Sniffing...\n')
    pkt = sniff(prn=print_pkt, count=count)

    # Annalyze results
    recall = TP/(TP+FN)
    precision = TP/(TP+FP)
    accuracy = (TP+TN)/(TP+TN+FP+FN)

    # Prints
    print('Packets read: ', total)
    print('Packets from Attacker (Ground Truth)', attacker)
    print('recall:', recall)
    print('precision:', precision)
    print('accuracy:', accuracy)