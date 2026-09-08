import telebot
import random
import os
import requests
import yt_dlp

TOKEN = "8968311546:AAEJV1sb8o-KIHzqRV3XHbIjUPQU5TRxFFQ"
bot = telebot.TeleBot(TOKEN)

TAK_QUESTIONS = [
    "شنو أكثر تصرف يستفزك بالناس؟", "لو خيروك بين 100 ألف دولار لو ترجع بالزمن 5 سنوات؟",
    "شنو الشيء اللي تسويه من تكون ضايج ومحد يدري عنه؟", "أكثر صفة تحبها بشخصيتك شنو؟",
    "شنو أكبر غلطة سويتها بحياتك وتعلمت منها؟", "لو طلع لك جني وقال لك اطلب أمنية واحدة فقط، شنو تطلب؟",
    "شنو العادة السريّة أو الغريبة اللي تسويها من تكون وحدك بالغرفة؟", "هل تقدر تسامح شخص خأن ثقتك؟",
    "شنو الكلمة اللي إذا أحد قالها لك تعكر مزاجك فوراً؟", "شنو أغرب أكلة جربتها بحياتك وعجبتك؟",
    "منو الشخص اللي مستحيل ترفض له طلب؟", "لو خيروك تعيش بدون موبايل شهر لو بدون أكل تحبه سنة؟",
    "شنو المكان اللي تتمنى تسافر له هسه وعاطفياً محتاجه؟", "هل تعتقد أن الصداقة بين الولد والبنت حقيقية؟",
    "شنو الفوبيا أو الخوف الأكبر عندك؟", "شنو الشيء اللي تتمنى تنحذف ذكرته من عقلك؟",
    "شنو أول شيء تلفت انتباهك بالشخص المقابل؟", "لو نطوك صلاحية تغيير قانون واحد بالعالم شنو تتمنى تغير؟",
    "أكثر موهبة تتمنى تتمرس بيها وتبدع بيها؟", "شنو أفضل حلم حلمته وما ردت تقعد منه؟",
    "شنو الشيء اللي يخليك تضحك من كل قلبك حتى لو كنت ضايج؟", "أيهما أفضل بالنسبة لك: العقل أم العاطفة لاتخاذ القرارات؟",
    "شنو الكلمة اللي تعتقد أنها تعبر عن حياتك حالياً؟", "منو أكثر شخص تؤمن برأيه ونصيحته بالدنيا؟",
    "لو اتيحت لك فرصة تدرس تخصص جديد شنو تختار؟", "هل تؤمن بالحب من أول نظرة؟",
    "شنو الموقف المحرج اللي مستحيل تنساه بطول حياتك؟", "لو كان بإمكانك تعيش في عصر قديم، أي عصر تختار؟",
    "شنو الكلمة أو العبارة اللي تكررها دائماً بكلامك؟", "هل تبكي بسهولة لو تعتبر نفسك قوي ومشاعرك صلبة؟",
    "شنو التطبيق اللي تضيع عليه معظم وقتك بالموبايل؟", "لو نطوك المايك وقالوا لك وجه كلمة للعالم كله، شنو تقول؟",
    "شنو أفضل هدية وصلتك بحياتك ومن منو؟", "أكبرها عيب تشوفه بشخصيتك وتتمنى تتخلص منه؟",
    "شنو الشيء اللي يسعدك مهما كان بسيط؟", "شنو آخر شيء اشتردته وحسيت إنه تسوى كل فلس؟",
    "لو قالوا لك تختار ممثل يمثل قصة حياتك، منو تختار؟", "هل تعتبر نفسك شخص اجتماعي لو انطوائي؟",
    "شنو الصوت اللي يسبب لك توتر أو انزعاج؟", "شنو أول شيء تسويه أول ما تقعد من النوم؟",
    "هل تسامح اللي يظلمك لو تنتظر الزمن يأخذ حقك؟", "شنو أسرع طريقة تقدر بيها تكسب قلبك؟",
    "شنو الشيء اللي تحس إنك مظلوم بيه بحياتك؟", "أيهما تحب أكثر: الهدوء والوحدة لو اللمة والجمعات؟",
    "شنو أكثر فيلم أو مسلسل أثر بيك وبكيت عليه؟", "لو نطوك تذكرة ذهاب بدون إياد لأي مكان بالعالم، تروح وين؟",
    "شنو الميزة اللي تتمنى تمتلكها وما موجودة عندك؟", "شنو أغرب حلم حلمته ومستحيل تنساه؟",
    "هل تقدر تعيش يوم كامل بدون ما تباوع بالموبايل؟", "شنو أكثر شيء يخليك تفقد أعصابك فوراً؟",
    "منو أقرب شخص لإلك بالجروب هنا؟", "لو قالولك تسافر ويا شخص واحد من المحادثة، منو تختار؟",
    "شنو الشي اللي سويته وبقيت ندمان عليه لحد اليوم؟", "هل تعرضت للخيانه من قبل صديق مقرب؟",
    "شنو الصفة اللي اذا شفتها بشخص تبتعد عنه فوراً؟", "شنو أكثر تاريخ بالتقويم تحبه وشنو المناسبة؟",
    "هل تحب تظهر مشاعرك للناس لو تكتمها بقلبك؟", "شنو الأغنية اللي تحسها تعبر عن حياتك بالظبط؟",
    "لو ربحت مليون دولار هسه، شنو أول شي تشتريه؟", "منو الشخص اللي تحسه يفهَمك من عيونك بدون ما تحكي؟"
]

def is_exact(message, target_words):
    if not message.text:
        return False
    text = message.text.strip()
    if isinstance(target_words, str):
        return text == target_words
    return text in target_words

@bot.message_handler(func=lambda message: message.text and message.text.startswith("يوف "))
def download_youtube_video(message):
    query = message.text.replace("يوف ", "").strip()
    if not query:
        bot.reply_to(message, "اكتب اسم المقطع بعد كلمة **يوف**، مثال:\n`يوف اغنية حسام الرسام`", parse_mode="Markdown")
        return

    wait_msg = bot.reply_to(message, "⚡ جاري البحث وتحميل الفيديو بأعلى دقة HD...", parse_mode="Markdown")
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'video_{message.from_user.id}.%(ext)s',
        'default_search': 'ytsearch1:',
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)
            if 'entries' in info and len(info['entries']) > 0:
                video_data = info['entries'][0]
                filename = ydl.prepare_filename(video_data)
                title = video_data.get('title', 'فيديو')
            else:
                filename = ydl.prepare_filename(info)
                title = info.get('title', 'فيديو')

        if os.path.exists(filename):
            with open(filename, 'rb') as video_file:
                bot.send_video(
                    message.chat.id,
                    video_file,
                    caption=f"🎬 **{title}**\n\n⚡ تم التحميل بدقة عالية بطلب من: [{message.from_user.first_name}](tg://user?id={message.from_user.id})",
                    reply_to_message_id=message.message_id,
                    parse_mode="Markdown"
                )
            bot.delete_message(message.chat.id, wait_msg.message_id)
            os.remove(filename)
        else:
            bot.edit_message_text("❌ حدث خطأ أثناء تنزيل الفيديو، حاول مجدداً!", message.chat.id, wait_msg.message_id)
            
    except Exception as e:
        print(f"Error: {e}")
        bot.edit_message_text("❌ تعذر جلب الفيديو، تأكد من الاسم وحاول مجدداً!", message.chat.id, wait_msg.message_id)

@bot.message_handler(func=lambda message: is_exact(message, ["اختصارات", "الاختصارات", "/start", "الاوامر"]))
def reply_shortcuts(message):
    shortcuts_text = (
        "هلا بيك يا بعد روحي! 🖤🔥\n\n"
        "🎬 **تحميل الفيديو بدقة عالية:** `يوف` + اسم المقطع\n"
        "🎲 **فعاليات:** `تك` | `ت`\n"
        "👑 **الشخصيات:** `ايدا` | `يوسف` | `الكسندر` | `راح اطفيج`\n"
        "📊 **الحساب:** `ايدي` | `بروفايلي`"
    )
    bot.reply_to(message, shortcuts_text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: is_exact(message, ["تك", "ت"]))
def reply_tak(message):
    bot.reply_to(message, f"🎯 **فعالية:**\n\n{random.choice(TAK_QUESTIONS)}", parse_mode="Markdown")

@bot.message_handler(func=lambda message: is_exact(message, ["راح اطفيج", "راح اطفيك"]))
def reply_turn_off(message):
    bot.reply_to(message, "تدلل بابا ❤️")

@bot.message_handler(func=lambda message: is_exact(message, "ايدا"))
def reply_ada(message):
    bot.reply_to(message, "روح ويوميات ايدا! نعم يويو ❤️✨")

bot.skip_pending = True
bot.infinity_polling(skip_pending=True)
