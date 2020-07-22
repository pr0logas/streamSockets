import os, sys

class Writer:
    def __init__(self, channelname, streamerdata):
        self.streamerData = streamerdata
        self.file = channelname
        self.directory = 'channels'
        self.path = 'channels/' + self.file

    def createEmptyFile(self):
        try:
            print("Creating an empty channel file: " + self.file)
            file = open(self.path, "w")
            file.write('')
            file.close()
        except:
            sys.exit(1)

    def channelWriter(self):
        if os.path.isfile(self.directory + '/' + self.file):
            file = open(self.path, "wb", buffering=0)
            file.write(self.streamerData)
            file.close()
        else:
            try:
                print("WARNING! Creating channels directory...")
                os.makedirs(self.directory)
                self.createEmptyFile()
            except:
                sys.exit(1)