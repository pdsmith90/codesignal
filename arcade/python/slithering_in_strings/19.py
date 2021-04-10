import re
def newStyleFormatting(s):
        sn = re.sub("%%", "{%}", s)
        snn = re.sub("(?!%%)%[a-z]", "{}", sn)
        return re.sub("{%}", "%", snn)
