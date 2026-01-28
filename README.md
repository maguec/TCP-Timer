
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

```usage
usage: response_timer [-h] --pcap-file PCAP_FILE --client-ip CLIENT_IP [--filter FILTER] [--format FORMAT]

Given the client get me the server response times

options:
  -h, --help            show this help message and exit
  --pcap-file PCAP_FILE
                        The pcap file
  --client-ip CLIENT_IP
                        The client ip address
  --filter FILTER       If greater than or equal to this value keep packet otherwise discard
  --format FORMAT       The output format fancy_grid or tsv default is fancy_grid
```

### Specify the Client IP

```bash
uv run main.py --pcap-file stream1.pcap --client-ip 10.11.3.5
```

### Script returns 



| Field | Description |
|--|--|
| time_ms | Elapsed Time of the request/response cycle |
| bytes | Predicted bytes of each response frame summed |
| packets | The number of packets in the response |
| server_ip | The IP address of the server |
| server_port | The port of the server |
| offset | The offset to check in Wireshark for the response |


```bash
╒═══════════╤═════════╤═══════════╤═══════════════╤═══════════════╤══════════╕
│   time_ms │   bytes │   packets │ server_ip     │   server_port │   offset │
╞═══════════╪═════════╪═══════════╪═══════════════╪═══════════════╪══════════╡
│      9.81 │    1024 │         2 │ 10.0.0.4      │         11038 │      221 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│     10.56 │     256 │         2 │ 10.0.0.4      │         11038 │      716 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│      9.69 │     256 │         2 │ 10.0.0.4      │         11038 │     1512 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│     11.63 │    1024 │         2 │ 10.0.0.4      │         11038 │     1745 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│      9.7  │    1024 │         2 │ 10.0.0.4      │         11038 │     2129 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│      9.8  │     256 │         2 │ 10.0.0.4      │         11038 │     2145 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│     11.7  │    1024 │         2 │ 10.0.0.4      │         11038 │     2212 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│     10.37 │     256 │         2 │ 10.0.0.4      │         11038 │     2645 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│     10.39 │    1024 │         2 │ 10.0.0.4      │         11038 │     2712 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│      9.96 │    1024 │         2 │ 10.0.0.4      │         11038 │    11508 │
├───────────┼─────────┼───────────┼───────────────┼───────────────┼──────────┤
│     10.7  │    1024 │         2 │ 10.0.0.4      │         11038 │    11791 │
╘═══════════╧═════════╧═══════════╧═══════════════╧═══════════════╧══════════╛
```
