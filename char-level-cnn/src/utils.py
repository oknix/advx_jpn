# -*- coding: utf-8 -*-
"""
@author: Viet Nguyen <nhviet1009@gmail.com>
"""
import numpy as np
from sklearn import metrics

def get_evaluation(y_true, y_prob, list_metrics):
    y_pred = np.argmax(y_prob, -1)
    output = {}
    if 'accuracy' in list_metrics:
        output['accuracy'] = metrics.accuracy_score(y_true, y_pred)
    if 'loss' in list_metrics:
        try:
            output['loss'] = metrics.log_loss(y_true, y_prob)
        except ValueError:
            output['loss'] = -1
    if 'confusion_matrix' in list_metrics:
        output['confusion_matrix'] = str(metrics.confusion_matrix(y_true, y_pred))
    return output

def get_default_folder(dataset, feature):
    if dataset == "agnews":
        input = "../data/ag_news_csv"
        output = "output/ag_news"
    elif dataset == "dbpedia":
        input = "../data/dbpedia_csv"
        output = "output/dbpedia"
    elif dataset == "chABSA":
        input = "../data/chABSA"
        output = "output/chABSA"
    return input, output + "_" + feature
