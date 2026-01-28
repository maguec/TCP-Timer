
## PCAP Fun with Scapy

### Break out each session into it's own file

```bash
for file in `ls *.pcap`; do
  echo "File: ${file}"
  for stream in $(tshark -r $file -T fields -e tcp.stream | sort -n | uniq); do
      tshark -r $file -Y "tcp.stream eq $stream" -w "streams_${file}_stream_$stream.pcap"
  done
done
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
