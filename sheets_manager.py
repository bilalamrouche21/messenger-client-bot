import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config

# إعداد الاتصال بـ Google Sheets
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_SHEETS_CREDENTIALS, scope)
client = gspread.authorize(credentials)

# فتح جداول البيانات
customers_sheet = client.open_by_key(config.SPREADSHEET_ID).worksheet(config.CUSTOMERS_WORKSHEET)
orders_sheet = client.open_by_key(config.SPREADSHEET_ID).worksheet(config.ORDERS_WORKSHEET)
products_sheet = client.open_by_key(config.SPREADSHEET_ID).worksheet(config.PRODUCTS_WORKSHEET)

# وظائف للتعامل مع Google Sheets

def add_order(customer_name, phone_number, product, status='قيد المعالجة'):
    orders_sheet.append_row([customer_name, phone_number, product, status])

def get_order_status(order_id):
    orders = orders_sheet.get_all_records()
    for order in orders:
        if order['رقم الطلب'] == order_id:
            return order['الحالة']
    return None 