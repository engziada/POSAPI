from flask import Flask, request, jsonify
from escpos.printer import Usb

app = Flask(__name__)

@app.route('/print_invoice', methods=['POST'])
def print_invoice():
    try:
        # Get invoice data from the request
        invoice_data = request.json

        # Connect to the USB printer
        # p = Usb(0x0456, 0x0808, 0)
        p = Usb(0x0456, 0x0808, 0, backend='libusb1')


        # Print the invoice
        p.text("Invoice Details:\n")
        p.text("================\n")
        p.text(f"Customer: {invoice_data['customer_name']}\n")
        p.text(f"Amount: {invoice_data['amount']}\n")
        # Add more details as needed

        # Cut the paper and close the connection
        p.cut()
        return jsonify({"status": "success", "message": "Invoice printed successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
