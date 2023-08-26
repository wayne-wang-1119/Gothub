from webhook_process.tasks import process_order_web


def test():
    process_order_web(
        "",
        "",
        "",
        "",
        "",
        "",
        [],
        [],
    )


if __name__ == "__main__":
    test()
