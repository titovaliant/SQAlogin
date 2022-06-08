import inspect
import logging

class Log_Data:
    @staticmethod
    def custom_logger(logLevel=logging.DEBUG):

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        fh = logging.FileHandler(filename=".\\Logs\\testing_data.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        
        fh.setFormatter(formatter)

        logger.addHandler(fh)
        return logger
        