from config import redis
import json


def update_redis_with_all_cryptos(crypto_list):
    redis.redis_client.set('crypto_list', json.dumps(crypto_list))


def get_redis_crypto_list():
    crypto_list_json = redis.redis_client.get('crypto_list')
    if crypto_list_json:
        return json.loads(crypto_list_json)
    else:
        return []
