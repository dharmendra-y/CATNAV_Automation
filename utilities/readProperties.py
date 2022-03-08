

import configparser
config=configparser.RawConfigParser()
config.read("C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserName():
        pcatusername=config.get('userinfo','username')
        return pcatusername

    @staticmethod
    def getPassword():
        pcatpassword=config.get('userinfo','password')
        return pcatpassword

    @staticmethod
    def getFirstName():
        shippingFirstname=config.get('shipping info','ship_firstname')
        return shippingFirstname
