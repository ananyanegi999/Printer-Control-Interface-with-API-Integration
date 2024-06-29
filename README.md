# Printer-Control-Interface-with-API-Integration

# Printer Control Interface

This application is a graphical user interface (GUI) for controlling printer hardware. The interface integrates multiple APIs to provide various printer functionalities.

## Features

1. **Select Printer**: Choose a printer from a list of available printers.
2. **Display Printer Status**: View printer status (online/offline), paper status, and ink/toner levels.
3. **Send Print Jobs**: Submit print jobs with options to select the number of copies, page range, and print quality.
4. **Cancel Print Jobs**: Cancel ongoing print jobs.
5. **Display Print Queue**: View the print queue with details of each job. Refresh the queue to see the latest status.
6. **Perform Maintenance Tasks**: Execute maintenance tasks such as cleaning print heads and aligning the printer.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python installations)

## API Functions

The following mock API functions are used in this application:

- `get_printers()`: Returns a list of available printers.
- `get_printer_status(printer_id)`: Returns the status of the specified printer.
- `send_print_job(printer_id, document, options)`: Sends a document to the specified printer with the given options.
- `cancel_print_job(printer_id, job_id)`: Cancels the specified print job.
- `get_print_queue(printer_id)`: Returns the print queue for the specified printer.
- `perform_maintenance(printer_id, task)`: Performs the specified maintenance task on the printer.



## GUI Components

  - `Printer Selection`: Dropdown menu to select the printer.
  - `Printer Status`: Labels to display the status, paper level, and ink level of the 
  selected printer.
    - Online status is displayed in green, and offline status is displayed in red.
  -`Print Job Options`:
    -`Number of Copies`: Spinbox to select the number of copies.
    -`Page Range`: Entry box to specify the page range.
    -`Print Quality`: Combobox to choose the print quality (High, Medium, Low).
  -`Print Job Control`:
    -`Send Print Job`: Button to submit a print job.
    -`Cancel Print Job`: Button to cancel the selected print job from the queue.
  -`Print Queue`:
   -Listbox to display the list of print jobs.
   -`Refresh Queue`: Button to refresh the print queue for the selected printer.
`Maintenance Tasks`:
  -`Clean Heads`: Button to clean the print heads.
  -`Align Printer`: Button to align the printer.
  
![image](https://github.com/ananyanegi999/Printer-Control-Interface-with-API-Integration/assets/117085932/89bdc048-b270-47da-9ce7-2b9125be6a32)


