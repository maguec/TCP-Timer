
## PCAP Fun with Scapy

### Break out each session into it's own file

```bash
tshark -r my.pcap -Y "tcp.stream eq 10" -w stream10.pcap
```

### Specify the Client IP

```bash
uv run main.py --client-ip 192.168.0.1
```




