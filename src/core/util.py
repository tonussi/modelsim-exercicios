import re


class Util(object):

    @staticmethod
    def convert_to_brazilian_fraction_style(val):
        return re.sub("(\d).(?=(\d{3})+(?!\d))", r"\1,", "%.3f" % val)
