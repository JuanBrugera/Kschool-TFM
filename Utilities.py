from matplotlib import pyplot as plt
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


def get_splitted_fields(schema):
    """
    This method returns id_field, input_fields and target_field givan an schema
    """
    fields = [field.name for field in schema.fields]
    id_field = fields[0]
    input_fields = fields[1:-1]
    target_field = fields[-1]

    return id_field, input_fields, target_field


def get_input_fields_dict(df, option, correlations=None, default_values=None):
    """
    Return distinct dicts (option).
    df = DataFrame from dict will be given
    option = determinates the dict will be returned
        in_model -> {field: True for field in input_fields}
        types -> {field: Type for field in input_fields}
        correlation -> {field: double for field in input_fields}
        correlation_ordered -> {field: integer for field in input_fields} sorted descending correlation[field]
        default_values -> {field: default_value for field in input_fields}
    correlations (None) = Mandatory when option is "correlation" or "correlation_ordered". List with the correlation between       input_fields and target.
    default_values (None) = Mandatory when option is "default_values". Dict with default values for each type of data.
    """
    if option == 'in_model':
        result = {field.name: True for field in df.schema.fields[1:-1]}
    elif option == 'types':
        result = {field.name: field.dataType for field in df.schema.fields[1:-1]}
    elif option == 'correlation':
        result = {k.name: abs(v) for k, v in zip(df.schema.fields[:-1], correlations)}
    elif option == 'correlation_ordered':
        corr = {k.name: abs(v) for k, v in zip(df.schema.fields[:-1], correlations)}
        result = {k: v for v, k in enumerate(sorted(corr, key=corr.get, reverse=True))}
    elif option == 'default_values':
        result = {field.name: default_values[field.dataType] for field in df.schema.fields}
    else:
        result = {}

    return result


def get_select_fields(in_model_dict):
    """
    Given an in_model dict, this method returns in_model[k] if it's True
    """
    return [k for k in in_model_dict.keys() if in_model_dict[k]]


def get_sample(df, fields, percentage):
    """
    Returns df.select(*fields).sample(percentage)
    """
    return df.select(*fields).sample(percentage)


def get_x_y_train(df, input_fields, target_field):
    """
    This method returns x_train and y_train given a DataFrame, input_fields and target_field
    """
    panda_df = df.toPandas()
    x_train = panda_df[input_fields]
    y_train = panda_df[[target_field]]

    return x_train, y_train


def get_grid_search_cv(classifier, param_grid, score_dict, score_refit, cv):
    """
    Returns an instace of GridSearchCV with the given params
    """
    return GridSearchCV(classifier(),
                        param_grid=param_grid,
                        scoring=score_dict,
                        refit=score_refit,
                        cv=cv,
                        n_jobs=-1)


def get_randomized_search_cv(classifier, param_grid, score_dict, score_refit, cv, n_iter):
    """
    Returns an instace of RandomizedSearchCV with the given params
    """
    return RandomizedSearchCV(classifier(),
                              param_distributions=param_grid,
                              scoring=score_dict,
                              refit=score_refit,
                              n_iter=n_iter,
                              cv=cv,
                              n_jobs=-1)


def print_scores(results, scores, score_refit):
    """
    Plots test score evolution from a CV search
    """
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
        print('best_%s: %s, %s_based_on_best_%s: %s' % (
            score, str(best_test_score), score, score_refit, str(score_for_score_refit)))
        plt.plot(formatted_scores, label=score)
    plt.legend()
    plt.show()
    

def get_na_fields(option):
    """
    Returns [fields] marked as NA in README.md if option is True. In other case, returns []
    """
    if option:
        with open('README.md', 'r') as f:
            text = f.read().split('\n')
            na_fields = [line.split()[1] for line in text if line.endswith("NA")]
        return na_fields
    else:
        return []
