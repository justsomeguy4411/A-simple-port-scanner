import tkinter as tk
from tkinter import messagebox
import python_port_gui as port_scannner 

def scan():
    ip = ip_entry.get()
    from_port = int(from_port_entry.get())
    to_port = int(to_port_entry.get())
    for port in range(from_port, to_port + 1):
        result = port_scannner.scan_ports(ip, port)
        if result:
            messagebox.showinfo("Result", f"Port {port} is OPEN on {ip}")
        else:
            messagebox.showinfo("Result", f"Port {port} is CLOSED on {ip}")

root = tk.Tk()
root.title("Port Scanner GUI")

tk.Label(root, text="Target IP:").pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

from_port_entry = tk.Entry(root)
from_port_entry.pack()

tk.Label(root, text="Target to Port:").pack()
to_port_entry = tk.Entry(root)
to_port_entry.pack()

tk.Button(root, text="Scan Port", command=scan).pack()

root.mainloop()
