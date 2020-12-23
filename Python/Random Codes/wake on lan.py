from wakeonlan import send_magic_packet




mac_address  = 'xxxxx'
ip_or_domain = 'xxxx'
port_no      = 4343


x=send_magic_packet(mac_address,ip_address=ip_or_domain,port=port_no)
print(x)
