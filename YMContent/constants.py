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
    'categories/{id}/populars'

    # Модели товаров
    'models/{id}',
    'models/{id}/reviews',
    'models/match',
    'models/{id}/looksas',
    'models/{id}/offers',
    'models/{id}/offers/default',
    'models/{id}/offers/stat',
    'models/{id}/offers/filters',
    'models/{id}/opinions'
    # 'model/{model_id}/info',
    # 'model/{model_id}/offers',
    # 'model/{model_id}/outlets',

    # Популярные модели
    # 'popular',
    # 'popular/{category_id}',

    # Товарные предложения
    'offers/{id}',

    # Отзывы
    # 'shop/{shop_id}/opinion'
    # 'model/{model_id}/opinion'

    # Магазины
    'shops/{id}/opinions',
    'shops/{id}',
    # 'shop/{shop_id}',
    # 'shop/{shop_id}/outlets',

    # Регионы
    # 'georegion',
    # 'georegion/{geo_id}',
    # 'georegion/{geo_id}/children',
    # 'georegion/suggest',

    # Производители
    # 'vendor',
    # 'vendor/{vendor_id}',

    # Сервисы
    # 'search',
    # 'model/match',
    # 'vendor/match',
    # 'filter/{category_id}',
]
