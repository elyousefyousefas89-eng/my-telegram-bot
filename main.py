import os
import random
import telebot

TOKEN = "8968311546:AAEJV1sb8o-KIHzqRV3XHbIjUPQU5TRxFFQ"
bot = telebot.TeleBot(TOKEN)

# 🎯 قائمة الـ 500 سؤال للفعاليات
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

def check_match(message, target_list):
    if not message.text:
        return False
    text = message.text.strip().lower()
    return text in [w.lower() for w in target_list]

# 🤫 نظام الهمسات السرية
@bot.message_handler(func=lambda message: message.text and message.text.strip().startswith("همسة "))
def secret_whisper(message):
    whisper_text = message.text.replace("همسة ", "").strip()
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass
    bot.send_message(message.chat.id, f"🤫 **همسة سرية:**\n{whisper_text}", parse_mode="Markdown")

# 📋 الأوامر والاختصارات العامة
@bot.message_handler(func=lambda message: check_match(message, ["اختصارات", "الاختصارات", "/start", "الاوامر", "اوامر"]))
def reply_shortcuts(message):
    shortcuts_text = (
        "هلا بيك يا بعد روحي وتاج راسِي! 🖤🔥 إليك كل الاختصارات المتاحة:\n\n"
        "🔹 **الأوامر العامة:** اختصارات، الاختصارات، /start، الاوامر، اوامر\n"
        "🎲 **الفعاليات:** تك، ت (500 سؤال صراحة وجرأة)\n"
        "👋 **الترحيب:** هلو، هلا، السلام عليكم، الوو، حي الله\n"
        "💬 **السوالف:** شلونك، شخبارك، شكو ماكو، اخبارك\n"
        "🍔 **الأكل:** جوعان، جوع، ريد أكل، ناكل\n"
        "🌧️ **التعب والملل:** تعبان، ضايج، ملل، خنكة\n"
        "✨ **المديح:** منور، منور البوت\n"
        "👋 **الوداع:** تصبح على خير، أشوفكم على خير، باي\n"
        "👑 **الشخصيات والتحكم:** راح اطفيج، راح اطفيك، ايدا، الكسندر، يوسف\n"
        "🆔 **معلومات الحساب:** ايدي، بروفايلي\n"
        "🤫 **الهمسات:** همسة + النص"
    )
    bot.reply_to(message, shortcuts_text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: check_match(message, ["تك", "ت"]))
def reply_tak(message):
    bot.reply_to(message, f"🎯 **فعالية:**\n\n{random.choice(TAK_QUESTIONS)}", parse_mode="Markdown")

@bot.message_handler(func=lambda message: check_match(message, ["هلو", "هلا", "السلام عليكم", "الوو", "حي الله"]))
def reply_hello(message):
    bot.reply_to(message, "هلا بيك يالغالي، منور البوت والقروب كله! 🖤✨")

@bot.message_handler(func=lambda message: check_match(message, ["شلونك", "شخبارك", "شكو ماكو", "اخبارك"]))
def reply_howareyou(message):
    bot.reply_to(message, "الحمد لله عايشين، إنت شلونك عساك بخير؟ 😎")

@bot.message_handler(func=lambda message: check_match(message, ["جوعان", "جوع", "ريد أكل", "ناكل"]))
def reply_hungry(message):
    bot.reply_to(message, "قوم اطلب صاج أو لفات فلافل وسد حلگك، لا تخليني أجوع وياك! 😂🍔")

@bot.message_handler(func=lambda message: check_match(message, ["تعبان", "ضايج", "ملل", "خنكة"]))
def reply_tired(message):
    bot.reply_to(message, "فداك تعبك وضوجتك، اطلب لك لعبة `تك` وخلينا نغير جو! 🎵🖤", parse_mode="Markdown")

@bot.message_handler(func=lambda message: check_match(message, ["منور", "منور البوت"]))
def reply_mnoor(message):
    bot.reply_to(message, "بوجودك يا غالي، النور نور عيونك ✨")

@bot.message_handler(func=lambda message: check_match(message, ["تصبح على خير", "أشوفكم على خير", "باي"]))
def reply_bye(message):
    bot.reply_to(message, "وأنت من أهل الخير، دير بالك على نفسك ونشوفك على خير 👋🖤")

@bot.message_handler(func=lambda message: check_match(message, ["راح اطفيج", "راح اطفيك"]))
def reply_turn_off(message):
    bot.reply_to(message, "تدلل بابا، السيرفر شغال 24 ساعة وما أنطفي أبداً ❤️")

@bot.message_handler(func=lambda message: check_match(message, ["ايدا"]))
def reply_ada(message):
    bot.reply_to(message, "روح ويوميات ايدا! نعم يويو الملكة بدون منازع ❤️✨")

@bot.message_handler(func=lambda message: check_match(message, ["الكسندر"]))
def reply_alexander(message):
    bot.reply_to(message, "حاضر، الكسندر وياكم! الأسطورة حاضرة 😎🔥")

@bot.message_handler(func=lambda message: check_match(message, ["يوسف"]))
def reply_yousef(message):
    bot.reply_to(message, "ذكره لا يذكر، عوفك من يوسف وخلينا بالسوالف الزينة! 😂")

@bot.message_handler(func=lambda message: check_match(message, ["ايدي", "بروفايلي"]))
def reply_id(message):
    bot.reply_to(message, f"🆔 ايدك يا بطل: `{message.from_user.id}`\n👤 اسمك: {message.from_user.first_name}", parse_mode="Markdown")

bot.skip_pending = True
bot.infinity_polling(skip_pending=True)
