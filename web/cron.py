# arquivo para ser rodado no cron e coletar dados para ser armazenado e posteriormente exibido
import sysinfo, time, json

ret = {}
ret['datetime'] = time.strftime('%Y/%m/%d %H:%M:%S')
ret['temperatures'] = {}
i = 1
labels = {1: 'External', 2: 'Room', 3: 'Pool'}
for key, val in sysinfo.temp().items():
    ret['temperatures'][i] = {}
    ret['temperatures'][i]['id'] = key
    ret['temperatures'][i]['label'] = labels[i]
    ret['temperatures'][i]['value'] = val
    i = i + 1

ret['sysinfo'] = {'cpuTemp': sysinfo.getCPUtemperature(),
                  'diskInfo': sysinfo.getDiskSpace(),
                  'ramInfo': sysinfo.getRAMinfo(),
                  'cpuUsage': sysinfo.getCPUuse()
                  }
f = open('combined.json', 'w')
json.dump(ret,f)
f.close()
