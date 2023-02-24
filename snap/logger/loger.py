from loguru import logger


# Dodaj logger do pliku
logger.add("logi.log", )

# Użyj loggera
log = logger.info
debug = logger.debug
warning = logger.warning
