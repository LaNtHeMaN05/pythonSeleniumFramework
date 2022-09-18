import logging


class LogGen:
    @staticmethod
    def logsGenerator():
        logging.basicConfig(filename=".\\Logs\\logs.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',force=True)

        log = logging.getLogger()
        log.setLevel(logging.INFO)
        return log
