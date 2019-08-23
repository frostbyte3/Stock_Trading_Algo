def getEnv(key):
    with open('.env', 'r') as env:
        Env = dict()
        for line in env:
            var = line.rstrip().split('=')
            Env[var[0]] = var[1]
        return Env[key]