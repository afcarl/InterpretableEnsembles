from sklearn import datasets

import pandas as pd
import numpy as np
import os
import collections


def load_wine():
    columns = ['Class', 'Alcohol', 'Acid', 'Ash', 'Alcalinity', 'Magnesium', 'Phenols', 'Flavanoids', 'Nonflavanoids',
              'Proanthocyanins', 'Color', 'Hue', 'Diluted', 'Proline']
    features = ['Alcohol', 'Acid', 'Ash', 'Alcalinity', 'Magnesium', 'Phenols', 'Flavanoids', 'Nonflavanoids',
              'Proanthocyanins', 'Color', 'Hue', 'Diluted', 'Proline']
    df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'wine.data'))
    df.columns = columns
    df['Class'] = np.subtract(df['Class'], 1)

    return df, features, 'Class', 'wine'


# def load_cars():
#     columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'Class']
#     features = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'car.data'))
#     df.columns = columns
#     df = df.reindex(np.random.permutation(df.index)).reset_index(drop=1)
#
#     mapping_buy_maint = {'low': 0, 'med': 1, 'high': 2, 'vhigh': 3}
#     mapping_doors = {'2': 0, '3': 1, '4': 2, '5more': 3}
#     mapping_persons = {'2': 0, '4': 1, 'more': 2}
#     mapping_lug = {'small': 0, 'med': 1, 'big': 2}
#     mapping_safety = {'low': 0, 'med': 1, 'high': 2}
#     mapping_class = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}
#
#     df['maint'] = df['maint'].map(mapping_buy_maint)
#     df['buying'] = df['buying'].map(mapping_buy_maint)
#     df['doors'] = df['doors'].map(mapping_doors)
#     df['persons'] = df['persons'].map(mapping_persons)
#     df['lug_boot'] = df['lug_boot'].map(mapping_lug)
#     df['safety'] = df['safety'].map(mapping_safety)
#     df['Class'] = df['Class'].map(mapping_class).astype(int)
#
#     return df, features, 'Class', 'cars'


# def load_wisconsin_breast_cancer():
#     columns = ['ID', 'ClumpThickness', 'CellSizeUniform', 'CellShapeUniform', 'MargAdhesion', 'EpithCellSize', 'BareNuclei',
#                'BlandChromatin', 'NormalNuclei', 'Mitoses', 'Class']
#     features = ['ClumpThickness', 'CellSizeUniform', 'CellShapeUniform', 'MargAdhesion', 'EpithCellSize', 'BareNuclei',
#                'BlandChromatin', 'NormalNuclei', 'Mitoses']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'breast-cancer-wisconsin.data'))
#     df.columns = columns
#     df['Class'] = np.subtract(np.divide(df['Class'], 2), 1)
#     df = df.drop('ID', axis=1).reset_index(drop=True)
#     df['BareNuclei'] = df['BareNuclei'].replace('?', int(np.mean(df['BareNuclei'][df['BareNuclei'] != '?'].map(int))))
#     df = df.applymap(int)
#
#     return df, features, 'Class', 'wisconsinBreast'
# #
#
def load_heart():
    columns = ['age', 'sex', 'chest pain type', 'resting blood pressure', 'serum cholestoral', 'fasting blood sugar', \
               'resting electrocardio', 'max heartrate', 'exercise induced', 'oldpeak', 'slope peak', \
               'vessels', 'thal', 'Class']
    features = ['age', 'sex', 'chest pain type', 'resting blood pressure', 'serum cholestoral', 'fasting blood sugar', \
               'resting electrocardio', 'max heartrate', 'exercise induced', 'oldpeak', 'slope peak', \
               'vessels', 'thal']

    columns_copy = []
    for column in columns:
        column=column[:10]
        columns_copy.append(column)
    columns = columns_copy

    features_copy = []
    for feature in features:
        feature=feature[:10]
        features_copy.append(feature)
    features=features_copy

    df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'heart.dat'), sep=' ')
    df.columns = columns
    df['Class'] = np.subtract(df['Class'], 1)
    return df, features, 'Class', 'heart'

## 3-fold CV:
# genetic = merger.genetic_algorithm(train_gen, 'cat', constructors, seed=1337, num_iterations=15,
#                                    num_crossovers=10, population_size=150, val_fraction=0.5, prune=True,
#                                    max_samples=1, tournament_size=10, nr_bootstraps=10)


# def load_glass():
#     columns = ['id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Class']
#     features = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'glass.data'))
#     df.columns = columns
#     df = df.drop('id', axis=1).reset_index(drop=True)
#     df['Class'] = np.subtract(df['Class'], 1)
#     df = df[df['Class'] != 3]
#     df['Class'] = df['Class'].map({0:0, 1:1, 2:2, 4: 3, 5: 4, 6: 5}).astype(int)
#     return df, features, 'Class', 'glass'


# GLASS:: genetic = merger.genetic_algorithm(train_gen, 'cat', constructors, seed=1337, num_iterations=5,
#                                            num_crossovers=15, population_size=150, val_fraction=0.25, prune=True,
#                                            max_samples=1, tournament_size=5, nr_bootstraps=10)  (3-fold CV)


# def load_austra():
#     columns = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','Class']
#     features = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'austra.data'))
#     df.columns = columns
#     df['Class'] = df['Class'].map({'y0': 0, 'y1': 1}).astype(int)
#     return df, features, 'Class', 'austra'

# AUSTRA:: genetic = merger.genetic_algorithm(train_gen, 'cat', constructors, seed=1337, num_iterations=5,
#                                            num_crossovers=15, population_size=150, val_fraction=0.33, prune=True,
#                                            max_samples=1, tournament_size=5, nr_bootstraps=10)  (3-fold CV)

#
# def load_led7():
#     columns = ['X1','X2','X3','X4','X5','X6','X7','Class']
#     features = ['X1','X2','X3','X4','X5','X6','X7']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'led7.data'))
#     df.columns = columns
#     df['Class'] = df['Class'].map({'y0': 0, 'y1': 1, 'y2': 2, 'y3': 3, 'y4': 4, 'y5': 5, 'y6': 6,
#                                    'y7': 7, 'y8': 8, 'y9': 9}).astype(int)
#     # print collections.Counter(df['Class'])
#     df = df[df['Class'] < 8]  # TODO: Orange is stupid, somehow you can't classify more than 8 classes
#     return df, features, 'Class', 'led7'


# def load_lymph():
#     columns = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18','Class']
#     features = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'lymph.data'))
#     df.columns = columns
#     df = df[df['Class'] != 'y1']
#     df = df[df['Class'] != 'y4']
#     # print collections.Counter(df['Class'])
#     df['Class'] = df['Class'].map({'y2': 0, 'y3': 1}).astype(int)
#     return df, features, 'Class', 'lymph'
#
#
# def load_pima():
#     columns = ['X1','X2','X3','X4','X5','X6','X7','X8','Class']
#     features = ['X1','X2','X3','X4','X5','X6','X7','X8']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'pima.data'))
#     df.columns = columns
#     df['Class'] = df['Class'].map({'y0': 0, 'y1': 1}).astype(int)
#     return df, features, 'Class', 'pima'


# def load_vehicle():
#     columns = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18','Class']
#     features = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'vehicle.data'))
#     df.columns = columns
#     df['Class'] = df['Class'].map({'y1': 0, 'y2': 1, 'y3': 2, 'y4': 3}).astype(int)
#     return df, features, 'Class', 'vehicle'


# def load_waveform():
#     columns = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18','X19','X20','X21','Class']
#     features = ['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16','X17','X18','X19','X20','X21']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'waveform.data'))
#     df.columns = columns
#     df['Class'] = df['Class'].map({'y0': 0, 'y1': 1, 'y2': 2}).astype(int)
#     return df, features, 'Class', 'waveform'

# def load_iris():
#     iris = datasets.load_iris()
#     df = pd.DataFrame(iris.data)
#     features = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]
#     df.columns = features
#     df['Class'] = iris.target
#
#     # df = df.drop('SepalWidth', axis=1)
#     # df = df.drop('PetalLength', axis=1)
#     # df = df[df['Class'] != 2]
#     # df = df.reset_index(drop=True)
#     # features = df.columns
#
#     return df, features, 'Class', 'iris'


def load_ecoli():
    columns = ['name', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2', 'Class']
    features = ['mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2']
    df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'ecoli.data'), delim_whitespace=True, header=0)
    df.columns = columns
    df = df.drop('name', axis=1).reset_index(drop=True)
    mapping_class = {'cp': 0, 'im': 1, 'pp': 2, 'imU': 3, 'om': 4, 'omL': 5, 'imL': 6, 'imS': 7}
    df['Class'] = df['Class'].map(mapping_class).astype(int)
    df = df[df['Class'] < 5]
    return df, features, 'Class', 'ecoli'


# def load_yeast():
#     columns = ['name', 'mcg', 'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc', 'Class']
#     features = ['mcg', 'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'yeast.data'), delim_whitespace=True, header=0)
#     df.columns = columns
#     df = df.drop('name', axis=1).reset_index(drop=True)
#     mapping_class = {'CYT': 0, 'NUC': 1, 'MIT': 2, 'ME3': 3, 'ME2': 4, 'ME1': 5, 'EXC': 6, 'VAC': 7, 'POX': 8, 'ERL': 9}
#     df['Class'] = df['Class'].map(mapping_class)
#     df = df[df['Class'] < 8]  # TODO: Orange is fucking stupid, somehow you can't classify more than 8 classes
#     print df.isnull().sum()
#     return df, features, 'Class', 'yeast'

## These datasets are very large and will take a very long time


# def load_magic():
#     columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym', 'fM3Long', 'fM3Trans', 'fAlpha', 'fDist', 'Class']
#     features = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym', 'fM3Long', 'fM3Trans', 'fAlpha', 'fDist']
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'magic04.data'))
#     df.columns = columns
#     mapping_class = {'g': 0, 'h': 1}
#     df['Class'] = df['Class'].map(mapping_class).astype(int)
#     return df, features, 'Class', 'magic'
#
#
# def load_shuttle():
#     columns = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6', 'feature7', 'feature8',
#                'feature9', 'Class']
#     features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6', 'feature7', 'feature8',
#                'feature9']
#
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'shuttle.tst'), sep=' ')
#     df.columns = columns
#     for feature in features:
#         if np.min(df[feature]) < 0:
#             df[feature] += np.min(df[feature]) * (-1)
#     df = df[df['Class'] < 6]
#     df['Class'] = np.subtract(df['Class'], 1)
#     df = df.reset_index(drop=True)
#
#     return df, features, 'Class', 'shuttle'

# def load_shuttle_full():
#     columns = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6', 'feature7', 'feature8',
#                'feature9', 'Class']
#     features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6', 'feature7', 'feature8',
#                'feature9']
#
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'shuttle_full.trn'), sep=' ')
#     df.columns = columns
#     for feature in features:
#         if np.min(df[feature]) < 0:
#             df[feature] += np.min(df[feature]) * (-1)
#     df = df[df['Class'] < 6]
#     df['Class'] = np.subtract(df['Class'], 1)
#     df = df.reset_index(drop=True)
#
#     return df, features, 'Class', 'shuttle'

#
#
# def load_nursery():
#     columns = ['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health', 'Class']
#     features = ['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health']
#
#     mapping_parents = {'usual': 0, 'pretentious': 1, 'great_pret': 2}
#     mapping_has_nurs = {'proper': 0, 'less_proper': 1, 'improper': 2, 'critical': 3, 'very_crit': 4}
#     mapping_form = {'complete': 0, 'completed': 1, 'incomplete': 2, 'foster': 3}
#     mapping_housing = {'convenient': 0, 'less_conv': 1, 'critical': 2}
#     mapping_finance = {'convenient': 0, 'inconv': 1}
#     mapping_social = {'nonprob': 0, 'slightly_prob': 1, 'problematic': 2}
#     mapping_health = {'recommended': 0, 'priority': 1, 'not_recom': 2}
#     mapping_class = {'not_recom': 1, 'recommend': 0, 'very_recom': 2, 'priority': 3, 'spec_prior': 4}
#
#     df = pd.read_csv(os.path.join(os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1]), 'nursery.data'), sep=',')
#     df = df.dropna()
#     df.columns = columns
#
#     df['parents'] = df['parents'].map(mapping_parents)
#     df['has_nurs'] = df['has_nurs'].map(mapping_has_nurs)
#     df['form'] = df['form'].map(mapping_form)
#     df['children'] = df['children'].map(lambda x: 4 if x == 'more' else int(x))
#     df['housing'] = df['housing'].map(mapping_housing)
#     df['finance'] = df['finance'].map(mapping_finance)
#     df['social'] = df['social'].map(mapping_social)
#     df['health'] = df['health'].map(mapping_health)
#     df['Class'] = df['Class'].map(mapping_class)
#
#     df = df[df['Class'] != 0]
#     df['Class'] = np.subtract(df['Class'], 1)
#     df = df.reset_index(drop=True)
#
#     return df, features, 'Class', 'nursery'
