import tkinter as tk
from tkinter import messagebox

class KasirAplikasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Kasir Toko Elektronik")
        self.root.configure(background='white')

        self.barang_harga = {
            "Handphone": 5000000,
            "Laptop": 10000000,
            "Printer": 2000000,
            "Mesin Cuci": 3000000,
            "Scanner": 1500000,
            "Speaker": 1000000
        }

        self.total_harga = 0
        self.items = {}

        # Header
        self.header_label = tk.Label(root, text="Koala Cell", font=("Comic Sans MS", 20), bg="white")
        self.header_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.label_nama_barang = tk.Label(root, text="Pilih Barang:", bg="white")
        self.label_nama_barang.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.option_menu = tk.OptionMenu(root, tk.StringVar(), *self.barang_harga.keys())
        self.option_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_qty_barang = tk.Label(root, text="Quantity:", bg="white")
        self.label_qty_barang.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.qty_frame = tk.Frame(root, bg="white")
        self.qty_frame.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.qty_barang = tk.IntVar()
        self.qty_barang.set(1)
        self.qty_entry = tk.Entry(self.qty_frame, textvariable=self.qty_barang, width=5)
        self.qty_entry.pack(side="left", padx=5)

        self.plus_button = tk.Button(self.qty_frame, text="+", command=self.increment_qty)
        self.plus_button.pack(side="left")

        self.minus_button = tk.Button(self.qty_frame, text="-", command=self.decrement_qty)
        self.minus_button.pack(side="left")

        self.tambah_button = tk.Button(root, text="Tambah", command=self.tambah_item, bg="blue", fg="white")
        self.tambah_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.listbox = tk.Listbox(root)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.label_total = tk.Label(root, text="Total Harga: Rp 0", bg="white")
        self.label_total.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.bayar_button = tk.Button(root, text="Bayar", command=self.bayar, bg="blue", fg="white")
        self.bayar_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Fungsi untuk mengisi layar secara otomatis
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def increment_qty(self):
        self.qty_barang.set(self.qty_barang.get() + 1)

    def decrement_qty(self):
        if self.qty_barang.get() > 1:
            self.qty_barang.set(self.qty_barang.get() - 1)

    def tambah_item(self):
        nama_barang = self.option_menu["text"]
        qty = self.qty_barang.get()
        if nama_barang:
            if nama_barang in self.barang_harga:
                harga_barang = self.barang_harga[nama_barang] * qty
                if nama_barang in self.items:
                    self.items[nama_barang][1] += qty
                    self.items[nama_barang][2] += harga_barang
                    self.listbox.delete(self.items[nama_barang][3])
                    self.listbox.insert(self.items[nama_barang][3],
                                        f"{nama_barang} - {self.items[nama_barang][1]} x Rp {self.barang_harga[nama_barang]}")
                else:
                    index = len(self.items) + 1
                    self.items[nama_barang] = [nama_barang, qty, harga_barang, index]
                    self.listbox.insert(tk.END,
                                        f"{nama_barang} - {qty} x Rp {self.barang_harga[nama_barang]}")
                self.total_harga += harga_barang
                self.label_total.config(text=f"Total Harga: Rp {self.total_harga}")
                self.qty_barang.set(1)
            else:
                messagebox.showerror("Error", "Nama barang tidak valid!")
        else:
            messagebox.showerror("Error", "Nama barang harus dipilih!")

    def bayar(self):
        if self.items:
            messagebox.showinfo("Pembayaran", f"Anda harus membayar total Rp {self.total_harga}")
            self.listbox.delete(0, tk.END)
            self.items.clear()
            self.total_harga = 0
            self.label_total.config(text="Total Harga: Rp 0")
        else:
            messagebox.showerror("Error", "Tambahkan item terlebih dahulu!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KasirAplikasi(root)
    root.geometry("400x400")  # Atur ukuran awal aplikasi
    root.mainloop()
