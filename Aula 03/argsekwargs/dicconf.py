def config_settings(defaults={}, **kwargs):
    defaults.update(kwargs)
    return defaults

config = config_settings({"host": "localhost", "port": 8080}, host="192.168.0.1", user="admin")
print(config)
