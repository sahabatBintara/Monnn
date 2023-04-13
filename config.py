# (©)Codexbotz
# Recode by @MOnthana201


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6262290227:AAFd6zO_A1fQ_O6TEOp9tTV8y95ZjsUDGkY"")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28593246""))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "7829cbe888e4ffd939d9f11af1ef43f1")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001904985143"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5918575107"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "monthana201")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://pwxhiljj:dRiVCmRDdvaPlnVMxK85g9ZCppExK1Kj@lallah.db.elephantsql.com/pwxhiljj")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "MonthanaLokal")
GROUP = os.environ.get("GROUP", "MonthanaAsing")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001890074356"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001967698548")))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Diriku Membagikan Koleksi Dari Montana Grup</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(5918575107)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
