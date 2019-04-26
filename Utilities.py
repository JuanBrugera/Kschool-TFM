from matplotlib import pyplot as plt
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


def get_splitted_fields(schema):
    fields = [field.name for field in schema.fields]
    id_field = fields[0]
    input_fields = fields[1:-1]
    target_field = fields[-1]

    return id_field, input_fields, target_field

def get_input_fields_dict(df, option, correlations=None, default_values=None):
    if option == 'in_model':
        result = {field.name: True for field in df.schema.fields[1:-1]}
    elif option == 'types':
        result = {field.name: field.dataType for field in df.schema.fields[1:-1]}
    elif option == 'correlation':
        result = {k.name: abs(v) for k,v in zip(df.schema.fields[:-1], correlations)}
    elif option == 'correlation_ordered':
        corr = {k.name: abs(v) for k,v in zip(df.schema.fields[:-1], correlations)}
        result = {k: v for v, k in enumerate(sorted(corr, key=corr.get, reverse=True))}
    elif option == 'default_values':
        result = {field.name: default_values[field.dataType] for field in df.schema.fields}
    else:
        result = {}

    return result

def get_select_fields(in_model_dict):
    return [k for k in in_model_dict.keys() if in_model_dict[k]]

def get_sample(df, fields, percentage):
    return df.select(*fields).sample(percentage)

def get_x_y_train(df, input_fields, target_field):
    panda_df = df.toPandas()
    x_train = panda_df[input_fields]
    y_train = panda_df[[target_field]]

    return x_train, y_train

def get_grid_search_cv(classifier, param_grid, score_dict, score_refit, cv):
    return GridSearchCV(classifier(),
                        param_grid=param_grid,
                        scoring=score_dict,
                        refit=score_refit,
                        cv=cv,
                        n_jobs=-1)

def get_randomized_search_cv(classifier, param_grid, score_dict, score_refit, cv, n_iter):
    return RandomizedSearchCV(classifier(),
                        param_distributions=param_grid,
                        scoring=score_dict,
                        refit=score_refit,
                        n_iter=n_iter,
                        cv=cv,
                        n_jobs=-1)

def print_scores(results, scores, score_refit):
    test_prefix = 'mean_test_%s'
    f = lambda x: float(x)
    score_refit_scores = str(results[test_prefix % score_refit])[1:-1].split()
    formatted = [f(score) for score in score_refit_scores]
    best_score_refit_score = max(formatted)
    index = formatted.index(best_score_refit_score)
    for score in scores.keys():
        test_scores = str(results[test_prefix % score])[1:-1].split()
        formatted_scores = [f(score) for score in test_scores]
        best_test_score = max(formatted_scores)
        score_for_score_refit = formatted_scores[index]
        print('best_%s: %s, %s_based_on_%s: %s' % (score, str(best_test_score), score, score_refit, str(score_for_score_refit)))
        plt.plot(formatted_scores, label=score)
    plt.legend()
    plt.show()

def get_na_fields(option):
    if option:
        with open('README.md', 'r') as f:
            text = f.read().split('\n')
            na_fields = [line.split()[1] for line in text if line.endswith("NA")]
        return na_fields
    else:
        return []

