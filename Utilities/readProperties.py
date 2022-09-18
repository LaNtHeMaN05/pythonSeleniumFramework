import configparser

config = configparser.RawConfigParser()

config.read(".\\Configs\\config.ini")


class readConfig():
    @staticmethod
    def naveenUrl():
        url = config.get('naveenTest', 'url')
        return url

    @staticmethod
    def naveenUser():
        user = config.get('naveenTest', 'user')
        return user

    @staticmethod
    def naveenPswd():
        pswd = config.get('naveenTest', 'pswd')
        return pswd

    @staticmethod
    def sauceLabsUrl():
        url = config.get('saucelabs', 'url')
        return url
