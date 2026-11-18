from train import train


def test_train_mean():
    assert train([1, 2, 3]) == 2
