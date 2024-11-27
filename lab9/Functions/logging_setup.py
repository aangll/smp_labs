import logging

def setup_logging():
    """Налаштування конфігурації логування для програми"""
    logging.basicConfig(
        filename='runner.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Логування налаштовано")
