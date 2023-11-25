## Constant variables used in the project

DATASET_DIRECTORY = 'data/'

FEATURES = [
    'flow_duration', 'Header_Length', 'Protocol Type', 'Duration',
       'Rate', 'Srate', 'Drate', 'fin_flag_number', 'syn_flag_number',
       'rst_flag_number', 'psh_flag_number', 'ack_flag_number',
       'ece_flag_number', 'cwr_flag_number', 'ack_count',
       'syn_count', 'fin_count', 'urg_count', 'rst_count', 
    'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 'SSH', 'IRC', 'TCP',
       'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 'LLC', 'Tot sum', 'Min',
       'Max', 'AVG', 'Std', 'Tot size', 'IAT', 'Number', 'Magnitue',
       'Radius', 'Covariance', 'Variance', 'Weight', 
]

LABELS = 'label'

# Attacks to dictionary
ATTACKS = {
    'DDoS-RSTFINFlood': 0,
    'DDoS-PSHACK_Flood': 1,
    'DDoS-SYN_Flood': 2,
    'DDoS-UDP_Flood': 3,
    'DDoS-TCP_Flood': 4,
    'DDoS-ICMP_Flood': 5,
    'DDoS-SynonymousIP_Flood': 6,
    'DDoS-ACK_Fragmentation': 7,
    'DDoS-UDP_Fragmentation': 8,
    'DDoS-ICMP_Fragmentation': 9,
    'DDoS-SlowLoris': 10,
    'DDoS-HTTP_Flood': 11,
    'DoS-UDP_Flood': 12,
    'DoS-SYN_Flood': 13,
    'DoS-TCP_Flood': 14,
    'DoS-HTTP_Flood': 15,
    'Mirai-greeth_flood': 16,
    'Mirai-greip_flood': 17,
    'Mirai-udpplain': 18,
    'Recon-PingSweep': 19,
    'Recon-OSScan': 20,
    'Recon-PortScan': 21,
    'VulnerabilityScan': 22,
    'Recon-HostDiscovery': 23,
    'DNS_Spoofing': 24,
    'MITM-ArpSpoofing': 25,
    'BenignTraffic': 26,
    'BrowserHijacking': 27,
    'Backdoor_Malware': 28,
    'XSS': 29,
    'Uploading_Attack': 30,
    'SqlInjection': 31,
    'CommandInjection': 32,
    'DictionaryBruteForce': 33
}

## 