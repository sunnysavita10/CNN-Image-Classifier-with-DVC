from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components.stage_03_train import Training
from CNNClassifier import logger
try:
    config = ConfigurationManager()
  
    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train()
    
except Exception as e:
    raise e