import yaml
from easydict import EasyDict as edict


constants_file = open("configs.yaml", 'r')
config_yaml = yaml.safe_load(constants_file)
CONFIG = edict(config_yaml)

# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
