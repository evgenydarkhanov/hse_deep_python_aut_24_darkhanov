class GreaterEqualError(Exception):
    pass


class SomeModel:
    def predict(self, message: str) -> float:
        return 0.5


def predict_message_mood(
    model: SomeModel,
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:

    if not isinstance(message, str):
        raise TypeError("message should be 'str'")

    if not isinstance(bad_thresholds, float):
        raise TypeError("bad_thresholds should be 'float'")

    if not isinstance(good_thresholds, float):
        raise TypeError("good_thresholds should be 'float'")

    if bad_thresholds > good_thresholds:
        raise GreaterEqualError("bad_thresholds > than good_thresholds")

    if bad_thresholds == good_thresholds:
        raise GreaterEqualError('bad_thresholds == good_thresholds')

    prediction = model.predict(message)

    if prediction < bad_thresholds:
        return 'неуд'
    if prediction > good_thresholds:
        return 'отл'
    return 'норм'
