from tkinter import *
from googletrans import Translator

# إنشاء نافذة التطبيق
window = Tk()
window.title("Alomtarjem")

# إنشاء مثيل المترجم
translator = Translator(service_urls=['translate.google.com'])

# وظيفة لتنفيذ عملية الترجمة
def translate_text():
    # الحصول على النص المراد ترجمته من مربع النص
    text = input_text.get("1.0", END).strip()

    # تحديد اللغة الأصلية
    src_lang = translator.detect(text).lang

    # الترجمة إلى اللغة المستهدفة
    if src_lang == 'ar':
        translation = translator.translate(text, dest='en').text
    else:
        translation = translator.translate(text, dest='ar').text

    # عرض النتيجة في مربع النتيجة
    output_text.delete("1.0", END)
    output_text.insert(END, translation)

# إنشاء مربع النص المدخل
input_label = Label(window, text="اكتب الجملة المراد ترجمتها:")
input_label.pack()
input_text = Text(window, height=5)
input_text.pack()

# إنشاء زر الترجمة
translate_button = Button(window, text="ترجم", command=translate_text)
translate_button.pack()

# إنشاء مربع النص الناتج
output_label = Label(window, text="النتيجة:")
output_label.pack()
output_text = Text(window, height=5)
output_text.pack()

# تشغيل التطبيق
window.mainloop()
