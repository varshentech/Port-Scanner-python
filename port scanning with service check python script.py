import socket

ip = input("Enter target IP: ")
start = int(input("Enter start port: "))
end = int(input("Enter end port: "))

for port in range(start, end+1):
    print("\nChecking port", port)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((ip, port))

        if result == 0:
            print("Port OPEN")

        
            banner = s.recv(1024)
            print("Service:", banner)

        else:
            print("Port CLOSED")

        s.close()

    except:
        pass