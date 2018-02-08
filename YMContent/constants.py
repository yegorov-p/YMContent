# -*- coding: utf-8 -*-

API_VERSION = 'v2'

USER_AGENT = 'YMContent'

VERSION = '0.1.0'

PROTOCOL = 'https'

DOMAIN = 'api.content.market.yandex.ru'

RESOURCES = [
    # Категории
    'categories',
    'categories/{}/children',
    'categories/{}',
    'categories/{}/filters',
    'categories/match',
    'categories/{}/bestdeals',
    'categories/{}/populars',
    'categories/{}/search',

    # Модели товаров
    'models/{}',
    'models/{}/reviews',
    'models/match',
    'models/{}/looksas',
    'models/{}/offers',
    'models/{}/offers/default',
    'models/{}/offers/stat',
    'models/{}/offers/filters',
    'models/{}/opinions',
    'models/{}/outlets'

    # Товарные предложения
    'offers/{}',
    'offers/{}/outlets',

    # Магазины
    'shops/{}/opinions',
    'shops/{}',
    'shops',
    'shops/{}/outlets',

    # Регионы
    'geo/regions/{}/shops/summary',
    'geo/regions',
    'geo/regions/{}/children',
    'geo/regions/{}',
    'geo/suggest',

    # Производители
    'vendor',
    'vendors/{}',
    'vendors/match',

    # Сервисы
    'search',
    'search/filters',
    'redirect',
    'suggestions'
]
