# -*- coding: utf-8 -*-

API_VERSION = 'v2'

USER_AGENT = 'YMContent'

VERSION = '0.2.6'

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
    'models/{}/outlets',

    # Товарные предложения
    'offers/{}',
    'offers/{}/outlets',

    # Магазины
    'shops/{}/opinions',
    'shops/{}/opinions/chronological',
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
    'vendors',
    'vendors/{}',
    'vendors/match',

    # Сервисы
    'search',
    'search/filters',
    'redirect',
    'suggestions'
]

CATEGORY_FIELDS = ('ALL', 'PARENT', 'STATISTICS', 'WARNINGS')
CATEGORY_SORT = ('BY_NAME', 'BY_OFFERS_NUM', 'NONE')
SEARCH_FILTERS = ('ALLVENDORS', 'DESCRIPTION', 'FOUND', 'SORTS', 'ALL', 'STANDARD')
FILTER_SET = ('ALL', 'BASIC', 'POPULAR')
MODEL_FIELDS = (
    'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS', 'FILTER_ALLVENDORS', 'FILTER_COLOR',
    'FILTER_DESCRIPTION',
    'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA', 'MODIFICATIONS', 'NAVIGATION_NODE', 'NAVIGATION_NODE_DATASOURCE',
    'NAVIGATION_NODE_ICONS', 'NAVIGATION_NODE_STATISTICS', 'OFFERS', 'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY',
    'OFFER_DELIVERY', 'OFFER_DISCOUNT', 'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP',
    'OFFER_VENDOR',
    'PHOTO', 'PHOTOS', 'PRICE', 'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION', 'VENDOR', 'ALL',
    'FILTER_ALL', 'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD', 'VENDOR_ALL')
MODEL_SORT = (
    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
    'QUALITY',
    'RATING', 'RELEVANCY')
OFFER_FIELDS = (
    'ACTIVE_FILTERS', 'CATEGORY', 'DELIVERY', 'DISCOUNT', 'OFFERS_LINK', 'OUTLET', 'OUTLET_COUNT', 'PHOTO', 'SHOP',
    'SHOP_ORGANIZATION', 'SHOP_RATING', 'VENDOR', 'ALL', 'SHOP_ALL', 'STANDARD')
SHOP_FIELDS = ('ORGANIZATION', 'RATING', 'ALL')
OUTLETS_FIELDS = (
    'OFFER', 'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT', 'OFFER_OFFERS_LINK',
    'OFFER_OUTLET', 'OFFER_OUTLET_COUNT', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR', 'SHOP', 'SHOP_ORGANIZATION',
    'SHOP_RATING', 'ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD')
GEO_FIELDS = ('DECLENSIONS', 'PARENT', 'ALL')
VENDOR_FIELDS = ('CATEGORIES', 'CATEGORY_PARENT', 'CATEGORY_STATISTICS', 'CATEGORY_WARNINGS', 'TOP_CATEGORIES', 'ALL')

OFFER = [
    'OFFER_ACTIVE_FILTERS',
    'OFFER_CATEGORY',
    'OFFER_DELIVERY',
    'OFFER_DISCOUNT',
    'OFFER_OFFERS_LINK',
    'OFFER_OUTLET',
    'OFFER_OUTLET_COUNT',
    'OFFER_PHOTO',
    'OFFER_SHOP',
    'OFFER_VENDOR',
    'OFFER_ALL']

MODEL = [
    'MODEL_CATEGORY',
    'MODEL_DEFAULT_OFFER',
    'MODEL_DISCOUNTS',
    'MODEL_FACTS',
    'MODEL_FILTER_COLOR',
    'MODEL_MEDIA',
    'MODEL_NAVIGATION_NODE',
    'MODEL_OFFERS',
    'MODEL_PHOTO',
    'MODEL_PHOTOS',
    'MODEL_PRICE',
    'MODEL_RATING',
    'MODEL_SPECIFICATION',
    'MODEL_VENDOR',
    'MODEL_ALL']

SHOP = [
    'SHOP_ORGANIZATION',
    'SHOP_RATING',
    'SHOP_ALL']
