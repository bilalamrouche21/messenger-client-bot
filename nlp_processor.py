from fuzzywuzzy import fuzz
import config

# معالجة الرسائل باستخدام اللغة الطبيعية

def process_message(message):
    # تحويل الكلمات العامية إلى فصحى
    for dialect, standard in config.ALGERIAN_DIALECT_MAPPING.items():
        message = message.replace(dialect, standard)
    
    # تصنيف الرسالة
    for message_type, patterns in config.MESSAGE_PATTERNS.items():
        for pattern in patterns:
            if fuzz.partial_ratio(message, pattern) > 80:
                return message_type, pattern
    return 'not_understood', None 