import config
from nlp_processor import process_message
from sheets_manager import add_order, get_order_status

# معالجة الرسائل الواردة

def handle_message(sender_id, message_text):
    # معالجة الرسالة باستخدام معالج اللغة الطبيعية
    message_type, details = process_message(message_text)
    
    if message_type == 'greeting':
        return config.BOT_MESSAGES['welcome'].format(name=sender_id)
    elif message_type == 'product_inquiry':
        return config.BOT_MESSAGES['product_inquiry_response'].format(product=details)
    elif message_type == 'order_request':
        # إضافة الطلب إلى Google Sheets
        add_order(sender_id, details['phone'], details['product'])
        return config.BOT_MESSAGES['order_confirmation'].format(order_id=details['order_id'])
    elif message_type == 'order_status':
        status = get_order_status(details['order_id'])
        if status:
            return config.BOT_MESSAGES['order_status_response'].format(order_id=details['order_id'], status=status, additional_info='')
        else:
            return config.BOT_MESSAGES['not_understood']
    else:
        return config.BOT_MESSAGES['not_understood'] 