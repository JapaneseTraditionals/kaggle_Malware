# Arguments
from argparse import ArgumentParser


def get_option():
    """
    Define options of command lines
    ---
    References
    https://qiita.com/taashi/items/400871fb13df476f42d2
    https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0
    """
    argparser = ArgumentParser()
    argparser.add_argument('version',
                           type=str,
                           help='Version ID')
    argparser.add_argument('-p', '--Predict',
                           action='store_true',
                           help='Executing prediction')
    argparser.add_argument('-op', '--OnlyPredict',
                           action='store_true',
                           help='Executing ONLY prediction')
    argparser.add_argument('-gb', '--GetBackTraining',
                           action='store_true',
                           help='Getting back train() from the not trained fold')
    argparser.add_argument('-to', '--TrainOneRound',
                           action='store_true',
                           help='Training ONLY one round')
    argparser.add_argument('-ns', '--NotSendMessage',
                           action='store_true',
                           help='Not sending message')
    argparser.add_argument('-d', '--DaskMode',
                           action='store_true',
                           help='Using dask.dataframe.read_csv')
    argparser.add_argument('-rc', '--reCalculation',
                           type=str,
                           default=None,
                           help='Recalculation feature list file path')
    argparser.add_argument('-j', '--nJobs',
                           type=int,
                           default=-1,
                           help='n_jobs for preprocess.')
    return argparser.parse_args()
