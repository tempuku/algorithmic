from typing import List


def wallets_coins(wallets_list: List[int], coins: int):
    if not wallets_list:
        return False
    wallets_list.sort(reverse=True)
    wallet_max = wallets_list.pop(0)
    if wallet_max > coins:
        return False
    coins -= wallet_max
    for wallet in wallets_list:
        if wallet > coins:
            continue
        coins -= wallet
    if coins == 0:
        return True
    return False


if __name__ == '__main__':
    wallets_list = [2,3]
    coins = 3
    print(wallets_coins(wallets_list, coins))
