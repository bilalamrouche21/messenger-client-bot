import os
from dotenv import load_dotenv

# تحميل المتغيرات البيئية من ملف .env
load_dotenv()

# إعدادات Facebook Messenger
PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN')
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')

# إعدادات Google Sheets
GOOGLE_SHEETS_CREDENTIALS = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
SPREADSHEET_ID = os.environ.get('SPREADSHEET_ID')
CUSTOMERS_WORKSHEET = 'العملاء'
ORDERS_WORKSHEET = 'الطلبات'
PRODUCTS_WORKSHEET = 'المنتجات'

# قائمة الكلمات العامية الجزائرية ومقابلها بالفصحى
ALGERIAN_DIALECT_MAPPING = {
    'واش': 'ماذا',
    'كيفاش': 'كيف',
    'وين': 'أين',
    'شحال': 'كم',
    'بزاف': 'كثير',
    'دروك': 'الآن',
    'شوية': 'قليل',
    'مليح': 'جيد',
    'خدمة': 'عمل',
    'حاجة': 'شيء',
    'بصح': 'لكن',
    'كاش': 'هل يوجد',
    'ماكاش': 'لا يوجد',
    'نبغي': 'أريد',
    'نشري': 'أشتري',
    'نحوس': 'أبحث',
    'نسقسي': 'أسأل',
    'راني': 'أنا',
    'كاين': 'يوجد',
    'ماكاينش': 'لا يوجد',
}

# أنماط الرسائل الشائعة
MESSAGE_PATTERNS = {
    'product_inquiry': [
        'منتج', 'سلعة', 'بضاعة', 'سعر', 'متوفر', 'كم ثمن', 'كم سعر', 'شحال', 'واش كاين', 'عندكم'
    ],
    'order_request': [
        'طلب', 'شراء', 'اشتري', 'نشري', 'نبغي', 'أريد', 'أطلب', 'حجز', 'نحجز'
    ],
    'order_status': [
        'حالة الطلب', 'وين وصل', 'متى يصل', 'وصل الطلب', 'طلبي', 'طلبية', 'تتبع'
    ],
    'greeting': [
        'سلام', 'مرحبا', 'أهلا', 'صباح الخير', 'مساء الخير', 'السلام عليكم'
    ]
}

# رسائل البوت
BOT_MESSAGES = {
    'welcome': "مرحبًا {name}، أنا مساعدك الذكي! كيف يمكنني مساعدتك اليوم؟ من فضلك تواصل معنا باللغة العربية حتى أتمكن من فهم طلبك بشكل أفضل. شكرًا لتفهمك!",
    'menu': "يمكنني مساعدتك في:",
    'not_understood': "عذرًا، لم أفهم طلبك. هل يمكنك توضيح ما تريد؟",
    'product_inquiry_response': "شكرًا لاهتمامك بمنتجاتنا! يمكنني مساعدتك في معرفة المزيد عن {product}. هل تريد معرفة السعر أو المواصفات أو التوفر؟",
    'order_request_response': "رائع! لإتمام طلبك لـ {product}، أحتاج إلى بعض المعلومات. هل يمكنك تزويدي برقم هاتفك وعنوان التوصيل؟",
    'order_status_response': "طلبك رقم {order_id} حالته: {status}. {additional_info}",
    'order_confirmation': "تم تسجيل طلبك بنجاح! رقم الطلب: {order_id}. سنتواصل معك قريبًا لتأكيد التفاصيل.",
    'contact_human': "سأقوم بتحويلك إلى أحد ممثلي خدمة العملاء للمساعدة. شكرًا لصبرك!"
}

# خيارات سريعة (Quick Replies)
QUICK_REPLIES = {
    'main_menu': [
        {
            'content_type': 'text',
            'title': 'المنتجات المتوفرة',
            'payload': 'PRODUCTS_PAYLOAD'
        },
        {
            'content_type': 'text',
            'title': 'تقديم طلب',
            'payload': 'ORDER_PAYLOAD'
        },
        {
            'content_type': 'text',
            'title': 'حالة طلبي',
            'payload': 'STATUS_PAYLOAD'
        },
        {
            'content_type': 'text',
            'title': 'التواصل مع الدعم',
            'payload': 'SUPPORT_PAYLOAD'
        }
    ]
} 