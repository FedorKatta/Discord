import logging

logger = logging.getLogger("Ашибки")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("Ашибки.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)
