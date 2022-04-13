import hydra
from omegaconf import DictConfig
from data_loader.data_loader import DataLoader

@hydra.main(config_path='config', config_name='config')
def main(cfg: DictConfig):
    print('Main')
    data_loader = DataLoader()
    df = data_loader.get_data()
    print(df)
    return

if __name__ == "__main__":
    main()