import ConfigParser


class ConfigurationService:

    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.twitter = {}
        self.smugmug = {}

        self.read_config()

    def read_config(self):
        try:
            self.config.read('config.cfg')

            return True
        except:
            print 'Error while trying to read the configuration file.'

        return False

    def read_key_value(self, section, key):
        if self.config.has_section(section):
            if self.config.has_option(section, key):
                return self.config.get(section, key)
            else:
                print "Key [{0}] not found.".format(key)
        else:
            print "Section [{0}] not found.".format(section)

        return ""
