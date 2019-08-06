import yaml

#Load config
with open("config.yml", 'r') as configYmlfile:
    cfg = yaml.load(configYmlfile, Loader=yaml.FullLoader)
print(cfg['discord_secret_token'])