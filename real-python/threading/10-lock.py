import concurrent.futures
import threading
import time

"""
Example of a race condition
"""


class Account:
    def __init__(self, starting_balance):
        self.balance = starting_balance
        self.lock = threading.Lock()

    def update(self, transaction, amount):
        print(f'{transaction} thread updating...')
        with self.lock:
            local_copy = self.balance
            local_copy += amount
            time.sleep(1)
            self.balance = local_copy
        print(f'{transaction} thread finishing...')


if __name__ == '__main__':
    account = Account(100)
    print(f'starting with balance of {account.balance}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for transaction in [('deposit', 50), ('withdrawl', -150)]:
            executor.submit(account.update, transaction[0], transaction[1])

    print(f'ending balance of {account.balance}')
