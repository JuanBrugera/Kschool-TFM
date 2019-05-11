from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier, DecisionTreeClassifier, GBTClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from sklearn.metrics import accuracy_score, precision_score, make_scorer, recall_score, roc_auc_score
from xgboost import XGBClassifier

import Utilities as utils

class ClassifierModel:
    """
        Class to implement a cross validation classifier
    """
    Clasifier: object = None
    ParamGrid: dict = {}
    MetricsEvaluation: dict = {}
    BestMetricEvaluation: str = ""
    RandomizedSearch: bool = False
    Iterations: int = 0  
    CV: int = 0    
    Weights: dict = {}
    Model: object
    
    def __init__(self, clasifier, paramGrid: dict = {},
                 metricsEvaluation: dict = {}, bestMetricEvaluation: str = "",
                 randomizedSearch: bool = False, cv: int = 3,
                 iterations: int = 30):
        self.Clasifier = clasifier
        self.ParamGrid = paramGrid
        self.MetricsEvaluation = metricsEvaluation
        self.BestMetricEvaluation = bestMetricEvaluation
        self.RandomizedSearch = randomizedSearch
        self.Iterations = iterations
        self.CV = cv

    def run_classifier_model(self, x_train, y_train):
        print("Running for %s" % str(self.Clasifier))
        self.Model = self._select_model()
        self.Model.fit(x_train, y_train)
        utils.print_scores(self.Model.cv_results_, scores=self.BestMetricEvaluation, score_refit=self.BestMetricEvaluation)
        print("Best Params = %s\n" % str(self.Model.best_params_))
    
    def _select_model(self):
        print("Selecting model by %s for %s" % (str(self.RandomizedSearch), str(self.Clasifier)))
        model:object = None
        if not self.RandomizedSearch:
            model = utils.get_grid_search_cv(classifier=self.Clasifier,
                                               param_grid=self.ParamGrid,
                                               score_dict=self.MetricsEvaluation,
                                               score_refit=self.BestMetricEvaluation,
                                               cv=self.CV)
        else:
            model = utils.get_randomized_search_cv(classifier=self.Clasifier,
                                                    param_grid=self.ParamGrid,
                                                    score_dict=self.MetricsEvaluation,
                                                    score_refit=self.BestMetricEvaluation,
                                                    cv=self.CV,
                                                    n_iter=selfs.Iterations)

        return model
    
    
class CrossValidationClassifiersModels:
    CrossValidationsClassifiers: dict = {}
    MetricsEvaluation: dict = {}
    BestMetricEvaluation: str = ""
    CV: int = 0    
    XTrain: object = None
    YTrain: object = None
    ColumnsToUse: object = None
    
    # some values by default     
    
        
    _metricsEvaluationByDefault: dict = {
        'precision': make_scorer(precision_score),
        'accuracy': make_scorer(accuracy_score),
        'recall': make_scorer(recall_score),
        'auc' : make_scorer(roc_auc_score)
    }
    _bestMetricEvaluationByDefault: str = 'recall'
    
    def __init__(self, x_train, y_train, columnsToUse, crossValidationsClassifiers:dict = {}, 
                 metricsEvaluation: dict = {}, bestMetricEvaluation: str = "", 
                 cv: int = 3):
        
        self.CrossValidationsClassifiers = crossValidationsClassifiers

        if (metricsEvaluation == {}):
            self.MetricsEvaluation = self._metricsEvaluationByDefault            
            self.BestMetricEvaluation = self._bestMetricEvaluationByDefault
        else:
            self.MetricsEvaluation = metricsEvaluation       
            self.BestMetricEvaluation = bestMetricEvaluation
        
        self.CV = cv
        self.CrossValidationsClassifiers = crossValidationsClassifiers
        self.XTrain = x_train
        self.YTrain = y_train
        self.ColumnsToUse = columnsToUse
        
    def init_CrossValidationsClassifiers_by_default(self, crossValidationsClassifiers = {}):
        if (crossValidationsClassifiers = {}):
            self.CrossValidationsClassifiers = {
                    ClassifierModel(clasifier=DecisionTreeClassifier ,
                            paramGrid={
                                    'max_depth': range(1,10), 
                                },
                            metricsEvaluation =self.MetricsEvaluation, 
                            bestMetricEvaluation=self.BestMetricEvaluation),
                    ClassifierModel(clasifier=RandomForestClassifier ,
                            paramGrid={
                                    'max_depth': [2, 3, 5, 8, 10, 13, 18],
                                    'n_estimators': [10, 25, 50, 100]
                                },
                            metricsEvaluation =self.MetricsEvaluation, 
                            bestMetricEvaluation=self.BestMetricEvaluation),
                    ClassifierModel(clasifier=GBTClassifier ,
                            paramGrid={
                                    'max_depth': [2, 3, 5, 8, 10, 13, 18],
                                    'n_estimators': [10, 25, 50, 100]
                                },
                            metricsEvaluation =self.MetricsEvaluation, 
                            bestMetricEvaluation=self.BestMetricEvaluation),
                    ClassifierModel(clasifier=XGBClassifier ,
                            paramGrid={
                                    'max_depth': [2, 3, 5, 8, 10, 13, 18],
                                    'n_estimators': [10, 25, 50, 100]
                                },
                            metricsEvaluation =self.MetricsEvaluation, 
                            bestMetricEvaluation=self.BestMetricEvaluation),

                } 
            else:
                self.CrossValidationsClassifiers = crossValidationsClassifiers
        for crossValidationsClassifier in self.CrossValidationsClassifiers:
            print("Loaded for %s" % str(crossValidationsClassifier.Clasifier))

    def run_all_classifier_models(self):
        for crossValidationsClassifier in self.CrossValidationsClassifiers:
            crossValidationsClassifier.run_classifier_model(self.XTrain, self.YTrain)
            values = {k: v for k, v in zip(in_model.keys(), crossValidationsClassifier.Model.best_estimator_.feature_importances_)}
            result = {k: values[k] for v, k in enumerate(sorted(values, key=values.get, reverse=True))}
            crossValidationsClassifier.Weights = result
