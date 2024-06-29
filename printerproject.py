import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

# Mock API functions
def get_printers():
    return ["Printer1", "Printer2", "Printer3"]

def get_printer_status(printer_id):
    return {"status": "online", "paper": "full", "ink": "75%"}

def send_print_job(printer_id, document, options):
    return {"job_id": 123, "status": "queued"}

def cancel_print_job(printer_id, job_id):
    return {"status": "cancelled"}

def get_print_queue(printer_id):
    return [{"job_id": 123, "document": "test.pdf", "status": "queued"}]

def perform_maintenance(printer_id, task):
    return {"status": "success"}

class PrinterControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Printer Control Interface")
        self.printers = get_printers()
        self.selected_printer = tk.StringVar()
        self.selected_printer.set(self.printers[0])
        self.create_styles()
        self.create_widgets()
        self.update_printer_status()
        self.update_print_queue()

    def create_styles(self):
        style = ttk.Style()
        style.theme_use('default')
        
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', background='#007fff', foreground='white', font=('Arial', 10, 'bold'))
        style.configure('TEntry', font=('Arial', 10))
        style.configure('TOptionMenu', background='#f0f0f0', font=('Arial', 10))
        style.configure('TCombobox', font=('Arial', 10))
        style.configure('TLabelframe', background='#f0f0f0', font=('Arial', 12, 'bold'))
        style.configure('TLabelframe.Label', background='#f0f0f0', font=('Arial', 12, 'bold'))

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="EW")

        # Printer selection
        printer_frame = ttk.Labelframe(main_frame, text="Printer Selection", padding="10")
        printer_frame.grid(row=0, column=0, sticky="EW")
        ttk.Label(printer_frame, text="Select Printer:").grid(row=0, column=0, padx=10, pady=10)
        self.printer_menu = ttk.OptionMenu(printer_frame, self.selected_printer, *self.printers)
        self.printer_menu.grid(row=0, column=1, padx=10, pady=10)
        self.selected_printer.trace("w", lambda *args: self.update_printer_status())

        # Printer status
        status_frame = ttk.Labelframe(main_frame, text="Printer Status", padding="10")
        status_frame.grid(row=1, column=0, sticky="EW")
        self.status_label = ttk.Label(status_frame, text="Status: N/A")
        self.status_label.grid(row=0, column=0, padx=10, pady=10)
        self.paper_label = ttk.Label(status_frame, text="Paper: N/A")
        self.paper_label.grid(row=0, column=1, padx=10, pady=10)
        self.ink_label = ttk.Label(status_frame, text="Ink: N/A")
        self.ink_label.grid(row=0, column=2, padx=10, pady=10)

        # Print job options
        job_frame = ttk.Labelframe(main_frame, text="Print Job Options", padding="10")
        job_frame.grid(row=2, column=0, sticky="EW")
        ttk.Label(job_frame, text="Number of Copies:").grid(row=0, column=0, padx=10, pady=10)
        self.copies_spinbox = tk.Spinbox(job_frame, from_=1, to=100, width=5)
        self.copies_spinbox.grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(job_frame, text="Page Range:").grid(row=1, column=0, padx=10, pady=10)
        self.page_range_entry = ttk.Entry(job_frame)
        self.page_range_entry.grid(row=1, column=1, padx=10, pady=10)
        ttk.Label(job_frame, text="Print Quality:").grid(row=2, column=0, padx=10, pady=10)
        self.quality_options = ttk.Combobox(job_frame, values=["High", "Medium", "Low"])
        self.quality_options.grid(row=2, column=1, padx=10, pady=10)
        self.quality_options.current(1)  # Set default to Medium

        # Print and Cancel buttons
        button_frame = ttk.Frame(job_frame)
        button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.print_button = ttk.Button(button_frame, text="Send Print Job", command=self.send_print_job)
        self.print_button.pack(side="left", padx=5)
        self.cancel_button = ttk.Button(button_frame, text="Cancel Print Job", command=self.cancel_print_job)
        self.cancel_button.pack(side="left", padx=5)

        # Print queue
        queue_frame = ttk.Labelframe(main_frame, text="Print Queue", padding="10")
        queue_frame.grid(row=3, column=0, sticky="EW")
        self.queue_listbox = tk.Listbox(queue_frame, height=5)
        self.queue_listbox.grid(row=0, column=0, padx=10, pady=10)
        self.refresh_button = ttk.Button(queue_frame, text="Refresh Queue", command=self.update_print_queue)
        self.refresh_button.grid(row=1, column=0, padx=10, pady=10)

        # Maintenance tasks
        maintenance_frame = ttk.Labelframe(main_frame, text="Maintenance Tasks", padding="10")
        maintenance_frame.grid(row=4, column=0, sticky="EW")
        self.clean_heads_button = ttk.Button(maintenance_frame, text="Clean Heads", command=lambda: self.perform_maintenance("clean_heads"))
        self.clean_heads_button.grid(row=0, column=0, padx=10, pady=10)
        self.align_printer_button = ttk.Button(maintenance_frame, text="Align Printer", command=lambda: self.perform_maintenance("align_printer"))
        self.align_printer_button.grid(row=0, column=1, padx=10, pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(main_frame, orient="horizontal", length=200, mode="determinate")
        self.progress.grid(row=5, column=0, padx=10, pady=10)

    def update_printer_status(self):
        status = get_printer_status(self.selected_printer.get())
        status_text = f"Status: {status['status']}"
        if status['status'] == "online":
            self.status_label.config(text=status_text, foreground="green")
        else:
            self.status_label.config(text=status_text, foreground="red")
        self.paper_label.config(text=f"Paper: {status['paper']}")
        self.ink_label.config(text=f"Ink: {status['ink']}")
        self.update_print_queue()

    def send_print_job(self):
        options = {
            "copies": self.copies_spinbox.get(),
            "page_range": self.page_range_entry.get(),
            "quality": self.quality_options.get()
        }
        document = filedialog.askopenfilename()
        if document:
            result = send_print_job(self.selected_printer.get(), document, options)
            messagebox.showinfo("Print Job", f"Print job {result['job_id']} queued")
            self.update_print_queue()

    def cancel_print_job(self):
        selected_job = self.queue_listbox.get(tk.ACTIVE)
        if selected_job:
            job_id = int(selected_job.split()[0])
            result = cancel_print_job(self.selected_printer.get(), job_id)
            messagebox.showinfo("Cancel Job", f"Print job {job_id} {result['status']}")
            self.update_print_queue()

    def update_print_queue(self):
        self.queue_listbox.delete(0, tk.END)
        queue = get_print_queue(self.selected_printer.get())
        for job in queue:
            self.queue_listbox.insert(tk.END, f"{job['job_id']} - {job['document']} - {job['status']}")

    def perform_maintenance(self, task):
        result = perform_maintenance(self.selected_printer.get(), task)
        messagebox.showinfo("Maintenance", f"Maintenance {task} {result['status']}")
        self.update_printer_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = PrinterControlApp(root)
    root.mainloop()
