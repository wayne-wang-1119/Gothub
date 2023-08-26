from random import random

from webhook_process.tasks import process_order_web


def test():
    random_order_id = str(random())

    process_order_web(
        f"test_order_id_{random_order_id}",  # FIXME Needs to be random every time
        "test_user_id",
        "test_username",
        "https://github.com/Git-of-Thoughts/GoT-test.git",
        "",
        "",
        [],
        [],
    )


if __name__ == "__main__":
    test()
