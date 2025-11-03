
## PCAP Fun with Scapy

### Break out each session into it's own file

```bash
tshark -r my.pcap -Y "tcp.stream eq 1" -w stream1.pcap
```

### Specify the Client IP

```bash
uv run main.py --pcap-file stream1.pcap --client-ip 10.11.3.5
```

### Script returns 



| Field | Description |
|--|--|
| Time(ms) | Elapsed Time of the request/response cycle |
| Bytes | Predicted bytes of each response frame summed |
| Packets | The number of packets in the response |


```bash
```
╒════════════╤═════════╤═══════════╕
│   Time(ms) │   Bytes │   Packets │
╞════════════╪═════════╪═══════════╡
│       0.38 │   89262 │         7 │
├────────────┼─────────┼───────────┤
│       0.24 │    1949 │         2 │
├────────────┼─────────┼───────────┤
│       0.92 │  391248 │        12 │
├────────────┼─────────┼───────────┤
│       1.41 │  556968 │        48 │
├────────────┼─────────┼───────────┤
│       0.35 │   38159 │         4 │
╘════════════╧═════════╧═══════════╛
```
