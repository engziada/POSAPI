from flask import Flask, request
from escpos.printer import Usb

app = Flask(__name__)

@app.route('/print_invoice', methods=['POST'])
def print_invoice():
    # استلام البيانات من العميل
    invoice_data = request.json

    # اتصال بالطابعة
    p = Usb(0x0456, 0x0808, 0)

    # طباعة الفاتورة بدون عرضها
    p.text("Invoice Details:\n")
    p.text("================\n")
    p.text(f"Customer: {invoice_data['customer_name']}\n")
    p.text(f"Amount: {invoice_data['amount']}\n")
    # قم بإضافة المزيد من المعلومات حسب حاجتك

    # اغلاق الاتصال بالطابعة
    p.cut()

    return "Invoice printed successfully!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
