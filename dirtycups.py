#/usr/bin/python3
import socket
import sys

# CVE-2024-47176 CUPS UDP Scanner
# This is a socket only CUPS scanner based off of MalwareTech's cups_scanner.py:
# https://github.com/MalwareTech/CVE-2024-47176-Scanner/blob/master/cups_scanner.py

def help_me():
    print ("\n💩💩💩  ERROR!!  💩💩💩\n")
    print ("Usage:   python dirtycups.py SRC_IP SRC_LISTENER_PORT TARGET_IP")
    print ("Example: python dirtycups.py 10.10.10.11 4444 127.0.0.1\n")
    print ("    .-=GAME OVER=-.\n")
    sys.exit()

try:
    src_ip = sys.argv[1]
    tcp_port = sys.argv[2]
    target_ip = sys.argv[3]
except:
    help_me()

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
        except:
            pass
        if not data:
            break
        try:
            print(data.decode())            
        except:
            pass
    client_socket.shutdown(socket.SHUT_RDWR)
    client_socket.close()

def start_server(tcp_port):
    tcp_port = int(tcp_port)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', tcp_port))
    server_socket.listen()
    while True:
        client_socket, addr = server_socket.accept()
        addr1 = str(addr)
        newaddr = addr1.split(",")
        addr = newaddr[0].strip("('") + ":" + newaddr[1].strip(")").strip()
        print("\n🖨️ ⚠️ 🖨️  Incoming connection from " + addr + " 🖨️ ⚠️ 🖨️")
        try:
            handle_client(client_socket)
        except:
            pass
            print ("\nShutting down listener (client socket error)...goodbye!\n")
            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()
            sys.exit()
        print ("-"*58)
        print ("🖨️ ☕💩  CUPS SERVICE IS VULNERABLE TO CVE-2024-47176! 🖨️ ☕💩\n🖨️ ☕💩  CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N  🖨️ ☕💩")
        print ("\nMore info:\nhttps://github.com/OpenPrinting/cups-browsed/security/advisories/GHSA-rj88-6mr5-rcw8\n")
        sys.exit()

def send_udp(target_ip,tcp_port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_callback = f'0 3 http://{src_ip}:{tcp_port}/printers/LRLPrinter'.encode('utf-8')
    udp_socket.sendto(udp_callback, (target_ip, 631))


if __name__ == "__main__":
    try:
        print("\n░█▀▄░▀█▀░█▀▄░▀█▀░█░█░░░█▀▀░█░█░█▀█░█▀▀ ")
        print("░█░█░░█░░█▀▄░░█░░░█░░░░█░░░█░█░█▀▀░▀▀█ ")
        print("░▀▀░░▀▀▀░▀░▀░░▀░░░▀░░░░▀▀▀░▀▀▀░▀░░░▀▀▀ ")
        print(" 🖨️ 🖨️  LRL Dirty CUPS Scanner v1.0 🖨️ 🖨️\n")
        print ("Sending CUPS UDP PDU & listening on 0.0.0.0:" + tcp_port)
        print ("-"*58)
        send_udp(target_ip,tcp_port)
        start_server(tcp_port)
    except KeyboardInterrupt:
        print ("\nShutting down, goodbye. More LRL tools at https://gitlab.com/lostrabbitlabs.")
        sys.exit()
