# -*- coding: utf-8 -*-

API_VERSION = 'v2'

USER_AGENT = 'pyYandexMarketContentAPI'

PROTOCOL = 'https'

DOMAIN = 'api.content.market.yandex.ru'

RESOURCES = [
    # Категории
    'categories',
    'categories/{id}/children',
    'categories/{id}',
    'categories/{id}/filters',
    'categories/match',
    'categories/{id}/bestdeals',
    'categories/{id}/populars',
    'categories/{id}/search',

    # Модели товаров
    'models/{id}',
    'models/{id}/reviews',
    'models/match',
    'models/{id}/looksas',
    'models/{id}/offers',
    'models/{id}/offers/default',
    'models/{id}/offers/stat',
    'models/{id}/offers/filters',
    'models/{id}/opinions',
    'models/{id}/outlets'

    # Товарные предложения
    'offers/{id}',
    'offers/{id}/outlets',

    # Магазины
    'shops/{id}/opinions',
    'shops/{id}',
    'shops',
    'shops/{id}/outlets',

    # Регионы
    'geo/regions/{id}/shops/summary',
    'geo/regions',
    'geo/regions/{id}/children',
    'geo/regions/{id}',
    'geo/suggest',

    # Производители
    'vendor',
    'vendors/{id}',
    'vendors/match',

    # Сервисы
    'search',
    'search/filters',
    'redirect',
    'suggestions'
]
