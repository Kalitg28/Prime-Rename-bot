from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot, update):
    text = """<b>Free Plan User</b>
Daily Upload limit: 5GB
Price: 0

<b>🪙 Basic</b>
Daily Upload limit: 20GB
Price: 50₹ /🌎 0.59$ per Month

<b>⚡ Standard</b>
Daily Upload limit: 50GB
Price: 100₹ /🌎 1.19$ per Month

<b>💎 Pro</b>
Daily Upload limit: 100GB
Price: 150₹ /🌎 2.16$ per Month

Payment Details:
<b>➜ <a href="https://envs.sh/kpL.jpg">Click Here To Scan</a></b>

💵 𝗔𝗡𝗬 𝗖𝗢𝗨𝗡𝗧𝗥𝗬 𝗔𝗟𝗟 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗠𝗘𝗧𝗛𝗢𝗗 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘. 
যদি বিকাশ বা 𝗤𝗥 কোড ছাড়া অথবা অন্য কিছু মাধ্যমে পেমেন্ট করতে চাইলে অথবা আরো কিছু জানার থাকলে 
𝗖𝗢𝗡𝗡𝗘𝗖𝗧 𝗔𝗗𝗠𝗜𝗡 ➠ <a href="https://t.me/Indian_MV_Admin_Bot">🇮🇳 𝐀𝐝𝐦𝐢𝐧 🧑🏻‍💻</a> \n\n
👇Send Payment Receipt 🧾 Screenshot"""
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Click Here To Send Payment Receipt 🧾", url="https://t.me/Indian_MV_Admin_Bot")],
        [InlineKeyboardButton("✖️ Cancel ✖️", callback_data="cancel")]
    ])
    
    await bot.send_photo(
        chat_id=update.message.chat.id,
        photo="https://envs.sh/AR9.jpg",
        caption=text,
        reply_markup=keyboard
    )

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot, message):
    text = """<b>Free Plan User</b>
Daily Upload limit: 5GB
Price: 0

<b>🪙 Basic</b>
Daily Upload limit: 20GB
Price: 50₹ /🌎 0.59$ per Month

<b>⚡ Standard</b>
Daily Upload limit: 50GB
Price: 100₹ /🌎 1.19$ per Month

<b>💎 Pro</b>
Daily Upload limit: 100GB
Price: 150₹ /🌎 2.16$ per Month

Payment Details:
<b>➜ <a href="https://envs.sh/kpL.jpg">Click Here To Scan</a></b>

💵 𝗔𝗡𝗬 𝗖𝗢𝗨𝗡𝗧𝗥𝗬 𝗔𝗟𝗟 𝗣𝗔𝗬𝗠𝗘𝗡𝗧 𝗠𝗘𝗧𝗛𝗢𝗗 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘. 
যদি বিকাশ বা 𝗤𝗥 কোড ছাড়া অথবা অন্য কিছু মাধ্যমে পেমেন্ট করতে চাইলে অথবা আরো কিছু জানার থাকলে 
𝗖𝗢𝗡𝗡𝗘𝗖𝗧 𝗔𝗗𝗠𝗜𝗡 ➠ <a href="https://t.me/Indian_MV_Admin_Bot">🇮🇳 𝐀𝐝𝐦𝐢𝐧 🧑🏻‍💻</a> \n\n
👇(Admin)👇Send Payment Receipt 🧾 Screenshot"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url="https://t.me/Indian_MV_Admin_Bot"),
         InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
    ])
    
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://envs.sh/AR9.jpg",
        caption=text,
        reply_markup=keyboard
                  )
