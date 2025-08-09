# DNS Resolver Script

This Python script resolves the domain `www.kame.net` to its IPv4 and IPv6 addresses using DNS queries.

## Features

- Queries **A records** (IPv4 addresses)
- Queries **AAAA records** (IPv6 addresses)
- Uses the `dnspython` library for DNS resolution

## Requirements

- Python 3.x
- `dnspython` package

Install the package via pip if you don't have it:

```bash
pip install dnspython
