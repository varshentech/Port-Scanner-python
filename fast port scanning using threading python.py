import socket
import threading
ip=input("enter the target ip:")
start=int(input("enter the starting port:"))
end=int(input("enter the ending port:"))
print("scanning",ip)
def scan_port(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    result=s.connect_ex((ip,port))
    if result==0:
        if port==21:
            service="ftp"
        elif port==22:
            service="ssh"
        elif port==80:
            service="http"
        elif port==443:
            service="https"
        else:
            service="unknown"
        print("[+] port {port} oepn ({service})")
    else:
        print("[-] port {port} closed")
    s.close()
for port in range(start,end+1):
    thread=threading.Thread(target=scan_port,args=(port,))
    thread.start()
