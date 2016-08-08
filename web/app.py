from bottle import route, run, template, static_file, hook, request
import daemon, json, time


rp = '/root/web'

@route('/api')
def index():
    ret = ['sysinfo',
           'temperature'
           ]
    return json.dumps(ret)


@route('/api/combined')
def combined():
    f = open(rp+'/combined.json','r')
    return json.load(f)

@route('/api/temperature')
def temperature():
    import sysinfo
    return json.dumps(sysinfo.temp())


@route('/api/arp')
def arp():
    import sysinfo
    return json.dumps(sysinfo.arp())


@route('/api/sysinfo')
def sysinfo():
    import sysinfo
    ret = {'cpuTemp': sysinfo.getCPUtemperature(),
           'diskInfo': sysinfo.getDiskSpace(),
           'ramInfo': sysinfo.getRAMinfo(),
           'cpuUsage': sysinfo.getCPUuse()
           }
    return ret




@route('/')
def index():
    return static_file('index.html', root=rp + '/html')


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=rp + '/html')


@hook('before_request')
def strip_path():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')


# log = open('./error.log','a')
# with daemon.DaemonContext(stderr=log):
#    run(host='0.0.0.0', port=8080)

run(host='0.0.0.0', port=80, reolader=True)
