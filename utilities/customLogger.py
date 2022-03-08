import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        FILE_PATH = 'C:/Users/dharmendray/PycharmProjects/CATNAV_Automation/Logsnew/Execution.log'
        fhandler = logging.FileHandler(filename=FILE_PATH, mode='w')
        #Use mode='a' to append the logs and 'w' for only currentt execution
        formatter = logging.Formatter('%(lineno)d | %(asctime)s | %(levelname)s | %(funcName)s | %(message)s', datefmt='%d/%B/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger