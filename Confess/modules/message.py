from Confess.config import *
from pyrogram import *
from pyrogram.types import *

START_TEXT = """
👋Hallo!

@SendConfessBot Adalah <b>Bot yang akan membantu</b> Kalian mengirim menfess crush mu langsung.

<b>👉Kurir Saya</b> @KangKurirMenfess Dia akan mengantarkan pesan menfess mu.

<b>❓ APA SAJA PERINTAHNYA ❓</b>
Tekan /help untuk melihat semua daftar perintah dan cara kerjanya.

[📃Rules Confess](http://t.me/SendConfessBot?start=rules)
"""

COMMANDS = """
<b>Bantuan Untuk Confess</b>

<b>✘ Perintah:</b> `/send_text [username target]`
<b>• Keterangan:</b> Mengirim confess dengan teks saja.
<b>💰Point:</b> -{PRICE_TEXT}

<b>✘ Perintah:</b> `/send_photo [username target]`
<b>• Keterangan:</b> Mengirim confess dengan foto dan teks
<b>💰Point:</b> -{PRICE_PHOTO}

<b>✘ Perintah:</b> `/send_spoiler [username target]`
<b>• Keterangan:</b> Mengirim confess dengan foto dan spoiler dan teks
<b>💰Point:</b> -{PRICE_SPOILER}

<b>✘ Perintah:</b> /addblacklist
<b>• Keterangan:</b> Akunmu tidak akan bisa dikirim menfess oleh pengguna. lain.

<b>✘ Perintah:</b> /delblacklist
<b>• Keterangan:</b> Akunmu akan bebas dikirim menfess oleh pengguna lain.

© Confess
"""

REGULATION = """
<b>Peraturan Confess:</b>

• Dilarang menggunakan kata rasisme atau bullying.
• Dilarang mengirimkan foto pornografi.
• Dilarang promosi kepada siapapun.
• Dilarang membuat keributan.

<b>Terganggu Dikirim Menfess?</b>
• /addblacklist - Agar akunmu tidak dikirimkan menfess oleh pengguna lain.
• /delblacklist - Pengguna lain bebas mengirimmu menfess.

<b>NB:</b>Perintah ini juga dapat dikirim melalui kolom chat diakun @KangKurirMenfess dengan menggunakan perintah yang sama seperti diatas.

<b>Melanggar?</b>
⛔Banned Permanen
"""

PRICE = """
<b>Daftar Harga 💰Point Confess:</b>

<b>+1💰Point</b> | Rp.500perak
• Berlaku Kelipatan

<b>💳Membership</b>
<b>+1💰Point</b> per hari
• Selama 1 Minggu 
]> Harga : Rp.3.000

<b>+2💰Point</b> per hari
• Selama 1 Bulan 
]> Harga : Rp.25.000

<b>👉 PENGGUNA BARU</b>
<b>+2💰Point</b> 
"""

