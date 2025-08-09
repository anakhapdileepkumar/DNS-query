import socket
import dns.resolver

domain = 'www.kame.net'

def get_dns_records(domain, record_type):
    try:
        answers = ip.resolver.resolve(domain, record_type)
        return [rdata.to_text() for rdata in answers]
    except Exception:
        return []


ipv4 = get_dns_records(domain, 'A')
if not ipv4:
    
    try:
        ipv4 = socket.gethostbyname_ex(domain)[2]
    except Exception:
        ipv4 = []

ipv6 = get_dns_records(domain, 'AAAA')

print("IPv4 addresses:", ipv4)
print("IPv6 addresses:", ipv6)
