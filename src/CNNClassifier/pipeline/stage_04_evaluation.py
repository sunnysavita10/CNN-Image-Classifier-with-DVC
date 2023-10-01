from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components.stage_04_evaluation import Evaluation
from CNNClassifier import logger




try:
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()
except Exception as e:
   raise e
