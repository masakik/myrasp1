import os


# Return CPU temperature as a character string
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return (res.replace("temp=", "").replace("'C\n", ""))


# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def getRAMinfo():
    p = os.popen('free -h')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:4])


# Return % of CPU used by user as a character string
def getCPUuse():
    return (str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip( \
        )))


# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:5])


# http://iot-projects.com/index.php?id=connect-ds18b20-sensors-to-raspberry-pi
def temp():
    import fnmatch
    ret = {}
    for filename in os.listdir("/sys/bus/w1/devices"):
        if fnmatch.fnmatch(filename, '28-*'):
            with open("/sys/bus/w1/devices/" + filename + "/w1_slave") as fileobj:
                lines = fileobj.readlines()
                if lines[0].find("YES"):
                    pok = lines[1].find('=')
                    temperature = (float(lines[1][pok + 1:pok + 6]) / 1000)
                    id = filename
                else:
                    logger.error("Error reading sensor with ID: %s" % (filename))
                ret[id] = temperature

    if (len(ret) > 0):
        return ret

def arp():
    from python_arptable import get_arp_table
    return get_arp_table()
