import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfigClass:
    @staticmethod
    def geta_data_for_email():
        email = config.get('login data', 'email')
        return email

    @staticmethod
    def geta_data_for_password():
        password = config.get('login data', 'password')
        return password

    @staticmethod
    def section1_data():
        section2_data = config.get('section 1', 'key1')
        return section2_data

