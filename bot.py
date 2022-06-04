import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext,updater
from telegram import KeyboardButton

from telegram import ReplyKeyboardMarkup,Update







import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def email_senderx(mass_g):

    smtp_server = "smtp.gmail.com" #
    port = 587
    sender_email = 'chilwillmike@gmail.com'
    receiver_email = ['d3ksup2022@gmail.com']
    password = 'hyicxrxxseprfnqw'

    msg = MIMEMultipart()
    msg["Subject"] = "حالة دعم تقني"
    msg["From"] = sender_email
    msg['To'] = ", ".join(receiver_email)
    text = mass_g

    body_text = MIMEText(text, 'plain')
    msg.attach(body_text)

    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    try:

        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    except Exception as e:
        print(e)

    finally:

        server.quit()


SNAPCHAT =  '''لتأمين السناب شات من الاختراق:
- نفتح البرنامج
- نضغط على علامة السناب
- نضغط على الاعدادات
- نتأكد من اضافة رقم الجوال للبرنامج
- نضغط على Login Verification
- نضغط على sms
- بعد ما يوصل المسج ندخله بالمربع وراح تتفعل الخاصية
'''
INSTAGRAM = '''
لتأمين الانستقرام من الاختراق:
- نفتح البرنامج
-نضغط على Two-Factor Auth
-نشغل الخاصية
- ندخل رقم الجوال، ثم ندخل الكود الذي بيوصل عن طريق المسجات
- نفعل الخاصية
'''

TWITTER ='''
لتأمين تويتر من الاختراق:
- نفتح البرنامج
- نضغط على البروفايل
-نضغط على Setting and Privacy
- نضغط على Account
-نضغط على Security
-نشغل الخاصية ونضغط Confirm
- نضغط على زر Start
- ندخل باسوورد الحساب
- بيوصلنا مسج على الجوال، ندخله وبتتفعل الخاصية
'''


WHATSAPP = ''' لتتأمين برنامج الواتس اب من الاختراق:
- نفتح البرنامج
- نضغط على الاعدادات
- نضغط على Account
-نضغط على Two-STEP VERIFICATION
- نشغل الخاصية
- نختار رقم سري للبرنامج'''




FirstButtom = "حماية برامج التواصل الاجتماعي"
SecondButtom = "دعم تقني"
FirstButtom1 = "Snapchat"
FirstButtom2 = "Instagram"
FirstButtom3 = "Twitter"
FirstButtom4 = "WhatsApp"
FirstButtom5 ="رجوع"
buttons = [[KeyboardButton(FirstButtom)], [KeyboardButton(SecondButtom)]]


def startCommand(update:Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='مرحبًا بك! بماذا نستطيع مساعدتك؟', reply_markup =ReplyKeyboardMarkup(buttons))


def messageHandler(update: Update, context: CallbackContext):
    if FirstButtom in update.message.text:
        buttons1 = [[KeyboardButton(FirstButtom1)], [KeyboardButton(FirstButtom2)],
                    [KeyboardButton(FirstButtom3)], [KeyboardButton(FirstButtom4)], [KeyboardButton(FirstButtom5)]]
        context.bot.send_message(chat_id=update.effective_chat.id, text='اختر تطبيق!', reply_markup =ReplyKeyboardMarkup(buttons1))
    if FirstButtom1 in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text=SNAPCHAT)
    if FirstButtom2 in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text=INSTAGRAM)
    if FirstButtom3 in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text=TWITTER)

    if FirstButtom4 in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text=WHATSAPP)

    if FirstButtom5 in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text='مرحبًا بك! بماذا نستطيع مساعدتك؟', reply_markup=ReplyKeyboardMarkup(buttons))

    if SecondButtom in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="ماهي المشكلة التي تواجهك؟")
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="الرجاء كتابة المشكلة مع طريقة للتواصل معك ضمن رسالة واحدة لضمان وصول المعلومات لنا")

    text = str(update.message.text)

    if text == 'مشاكل في الحسابات':
        text = ''

        email_senderx(text)

def main():

    updater = Updater(
                token="5314177552:AAF41mTzEuRaFRopcsS8Ub6obxyNKOudiVo")


    dispatcher = updater.dispatcher



    dispatcher.add_handler(CommandHandler('start', startCommand))
    dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
    updater.start_polling()
    updater.idle()




if __name__ == '__main__':
    main()
