import os, time
from datetime import datetime

class LogLevel:

    OFF = 0
    MIN = 1
    NOR = 2
    DEBUG = 3

class Logger:

    def __init__(self, fullTestName, loglevel=LogLevel.DEBUG):
        testName = os.path.splitext(os.path.basename(fullTestName))[0]
        logName = testName + '.log'

        logsFolder = 'logs'
        if not os.path.exists(logsFolder):
            os.makedirs(logsFolder, exist_ok = True)

        self.log = os.path.join(logsFolder, logName)
        self.createLog()

        self.loggingLevel = loglevel
        self.startTime = time.perf_counter()

    def createLog(self):
        with open(self.log, mode='w', encoding = 'utf-8') as logFile:
            logFile.write(self.getDateTime() + '\t\t*** Starting Test ***\n')
        logFile.close()

    def writeToLog(self, msg='', loglevel=LogLevel.DEBUG):

        if loglevel > self.loggingLevel:
            return

        with open(self.log, mode='a', encoding='utf-8') as logFile:
            msg = str(msg)
            if msg.startswith('\n'):
                msg = msg[1:]
            logFile.write(self.getDataTime() + '\t\t' + msg + '\n')

        logFile.close()

    def getDateTime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.oop.log.writeToLog(utc.strftime(fmtStrZone)),
                                self.oop.level.MIN)

        self.oop.log.writeToLog(utc.strftime(fmtStrZone)),
                                self.oop.level.NOR)
