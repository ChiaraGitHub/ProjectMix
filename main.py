import hydra
from omegaconf import DictConfig

@hydra.main(config_path='config', config_name='config')
def main(cfg: DictConfig):
    print('Main')
    return

if __name__ == "__main__":
    main()