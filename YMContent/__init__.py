# -*- coding: utf-8 -*-

__title__ = 'YandexMarketContent'
__version__ = '0.0.1'
__author__ = 'Pavel Yegorov'
__license__ = 'Apache 2.0'

from .constants import *
import requests
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError
import socket
import ssl
from .response import *

from pprint import pprint


class YMAPI(object):
    """Access Yandex REST API resources.
    :param authorization_key: Yandex authorization key
    """

    class BaseAPIError(BaseException):
        pass

    class FieldsParamError(BaseException):
        pass

    class GroupByParamError(BaseException):
        pass

    class HowParamError(BaseException):
        pass

    class MatchTypeParamError(BaseException):
        pass

    class TypeParamError(BaseException):
        pass

    class FilterSetParamError(BaseException):
        pass

    class SortParamError(BaseException):
        pass

    class GradeParamError(BaseException):
        pass

    class CountParamError(BaseException):
        pass

    class PageParamError(BaseException):
        pass

    class GeoParamError(BaseException):
        pass

    class NoGeoIdOrIP(BaseException):
        pass

    def __init__(self, authorization_key=None):
        if not authorization_key:
            raise YMAPI.NotAuthorized(
                "You must provide authorization key to access Yandex.Market API!")
        self.session = requests.Session()
        self.session.headers = {
            'Host': DOMAIN,
            'Authorization': authorization_key,
            'User-agent': USER_AGENT,
        }

    def _prepare_url(self, resource):
        return '%s://%s/%s/%s' % (PROTOCOL, DOMAIN, API_VERSION, resource)

    def _prepare_resource_path(self, resource_path, params=None):
        return resource_path.format(**params)

    def request(self, resource, req_id, params):
        if resource not in RESOURCES:
            raise Exception('Resource "%s" unsupported' % resource)

        resource_path = self._prepare_resource_path(resource, {'id': req_id})
        url = self._prepare_url(resource_path)

        try:
            response = self.session.get(
                url=url,
                params=params
            )

            data = response.json()

            if response.status_code in (401, 404, 422):
                raise YMAPI.BaseAPIError(
                    data['errors'][0]['message'])
            return response

        except (ConnectionError, ProtocolError, ReadTimeout, ReadTimeoutError, SSLError, ssl.SSLError,
                socket.error) as exception:
            pass

    def categories(self, fields=None, sort='NONE', geo_id=None, remote_ip=None, count=10, page=1):
        if geo_id is None and remote_ip is None:
            raise YMAPI.NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if fields:
            for field in fields.split(','):
                if field not in ('ALL', 'PARENT', 'STATISTICS', 'WARNINGS'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        if sort:
            if sort not in ('BY_NAME', 'BY_OFFERS_NUM', 'NONE'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        params = {'fields': fields,
                  'sort': sort,
                  'geo_id': geo_id,
                  'remote_ip': remote_ip,
                  'count': count,
                  'page': page}

        return Categories(self.request('categories', None, params))

    def categories_children(self, req_id=None, fields=None, sort='NONE', geo_id=None, remote_ip=None, count=10, page=1):
        if geo_id is None and remote_ip is None:
            raise YMAPI.NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if fields:
            for field in fields.split(','):
                if field not in ('ALL', 'PARENT', 'STATISTICS', 'WARNINGS'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        if sort:
            if sort not in ('BY_NAME', 'BY_OFFERS_NUM', 'NONE'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        params = {'fields': fields,
                  'sort': sort,
                  'geo_id': geo_id,
                  'remote_ip': remote_ip,
                  'count': count,
                  'page': page}
        return CategoriesChildren(self.request('categories/{id}/children', req_id, params))

    def category(self, req_id=None, fields=None, geo_id=None, remote_ip=None):
        if geo_id is None and remote_ip is None:
            raise YMAPI.NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if fields:
            for field in fields.split(','):
                if field not in ('ALL', 'PARENT', 'STATISTICS', 'WARNINGS'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        params = {'fields': fields,
                  'geo_id': geo_id,
                  'remote_ip': remote_ip}

        return Category(self.request('categories/{id}', req_id, params))

    def categories_filters(self, req_id=None, geo_id=None, remote_ip=None, fields=None, filter_set='POPULAR', rs=None,
                           sort='NONE', filters={}):
        if geo_id is None and remote_ip is None:
            raise YMAPI.NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if fields:
            for field in fields.split(','):
                if field not in ('ALLVENDORS', 'DESCRIPTION', 'FOUND', 'SORTS', 'ALL', 'STANDARD'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        if filter_set:
            for field in filter_set.split(','):
                if field not in ('ALL', 'BASIC', 'POPULAR'):
                    raise YMAPI.FilterSetParamError('"filter_set" param is wrong')

        if sort:
            if sort not in ('NAME', 'NONE'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        params = {'fields': fields,
                  'filter_set': filter_set,
                  'sort': sort,
                  'geo_id': geo_id,
                  'remote_ip': remote_ip
                  }

        if rs:
            params['rs'] = rs

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        return CategoriesFilters(self.request('categories/{id}/filters', req_id, params))

    # Todo Не готов
    def categories_match(self, name, category_name=None, description=None, locale='RU_ru', price=None,
                         shop_name=None):
        params = {'name': name, 'locale': locale}

        if category_name:
            params['category_name'] = category_name

        if description:
            params['description'] = description

        if price:
            params['price'] = price

        if shop_name:
            params['shop_name'] = shop_name

        return Category(self.request('categories/match', None, params))

    def models(self, req_id, fields='CATEGORY,PHOTO', filters={}, geo_id=None, remote_ip=None):
        if geo_id is None and remote_ip is None:
            raise YMAPI.NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if fields:
            for field in fields.split(','):
                if field not in (
                        'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS', 'FILTER_ALLVENDORS',
                        'FILTER_COLOR',
                        'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA', 'MODIFICATIONS',
                        'NAVIGATION_NODE',
                        'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS', 'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                        'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK',
                        'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR', 'PHOTO', 'PHOTOS', 'PRICE',
                        'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION', 'VENDOR', 'ALL', 'FILTER_ALL',
                        'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD', 'VENDOR_ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        params = {'fields': fields,
                  'geo_id': geo_id,
                  'remote_ip': remote_ip
                  }
        if filters:
            for (k, v) in filters.items():
                params[k] = v

        return Model(self.request('models/{id}', req_id, params))

    def models_reviews(self, req_id, count=10, page=1):
        params = {'count': count,
                  'page': page
                  }
        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        return ModelReview(self.request('models/{id}/reviews', req_id, params))

    def models_match(self, name, category_count=1, fields='CATEGORY,PHOTO', match_types='MULTI,REPORT',
                     category_name=None, description=None, locale='RU_ru', price=None, shop_name=None, category_id=None,
                     hid=None):
        params = {'category_count': category_count,
                  'fields': fields,
                  'match_types': match_types,
                  'name': name, 'locale': locale}

        if fields:
            for field in fields.split(','):
                if field not in (
                        'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS', 'FILTER_ALLVENDORS',
                        'FILTER_COLOR',
                        'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA', 'MODIFICATIONS',
                        'NAVIGATION_NODE',
                        'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS', 'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                        'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK',
                        'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR', 'PHOTO', 'PHOTOS', 'PRICE',
                        'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION', 'VENDOR', 'ALL', 'FILTER_ALL',
                        'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD', 'VENDOR_ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        if match_types:
            for match_type in match_types.split(','):
                if match_type not in (
                        'BATCH', 'MULTI', 'MULTI_STRING', 'REPORT', 'STRING', 'ALL'):
                    raise YMAPI.MatchTypeParamError('"match_types" param is wrong')

        if category_name:
            params['category_name'] = category_name

        if description:
            params['description'] = description

        if price:
            params['price'] = price

        if shop_name:
            params['shop_name'] = shop_name

        if category_id:
            params['category_id'] = category_id

        if hid:
            params['hid'] = hid

        return Models(self.request('models/match', None, params))

    def models_lookas(self, req_id, count=10, fields='CATEGORY,PHOTO'):
        params = {'count': count,
                  'fields': fields}

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if fields:
            for field in fields.split(','):
                if field not in (
                        'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS', 'FILTER_ALLVENDORS',
                        'FILTER_COLOR',
                        'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA', 'MODIFICATIONS',
                        'NAVIGATION_NODE',
                        'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS', 'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                        'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK',
                        'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR', 'PHOTO', 'PHOTOS', 'PRICE',
                        'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION', 'VENDOR', 'ALL', 'FILTER_ALL',
                        'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD', 'VENDOR_ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        return ModelsLookas(self.request('models/{id}/looksas', req_id, params))

    def categories_bestdeals(self, req_id, fields='CATEGORY,PHOTO', count=10, page=1):
        params = {'count': count,
                  'fields': fields}

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        if fields:
            for field in fields.split(','):
                if field not in (
                        'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS', 'FILTER_ALLVENDORS',
                        'FILTER_COLOR',
                        'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA', 'MODIFICATIONS',
                        'NAVIGATION_NODE',
                        'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS', 'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                        'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK',
                        'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR', 'PHOTO', 'PHOTOS', 'PRICE',
                        'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION', 'VENDOR', 'ALL', 'FILTER_ALL',
                        'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD', 'VENDOR_ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        return CategoriesLookas(self.request('categories/{id}/bestdeals', req_id, params))

    def categories_popular(self, req_id, fields='CATEGORY,PHOTO', count=10, page=1):
        params = {'count': count,
                  'fields': fields}

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        if fields:
            for field in fields.split(','):
                if field not in (
                        'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS', 'FILTER_ALLVENDORS',
                        'FILTER_COLOR',
                        'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA', 'MODIFICATIONS',
                        'NAVIGATION_NODE',
                        'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS', 'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                        'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK',
                        'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR', 'PHOTO', 'PHOTOS', 'PRICE',
                        'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION', 'VENDOR', 'ALL', 'FILTER_ALL',
                        'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD', 'VENDOR_ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')

        return CategoriesPopular(self.request('categories/{id}/populars', req_id, params))

    def models_offers(self, req_id, delivery_included=False, fields=None, groupBy=None, shop_regions=None, filters={},
                      count=10, page=1, how=None, sort=None, latitude=None, longitude=None):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if delivery_included:
            #     if delivery_included in [0,'0','F','FALSE','N','NO'
            params['delivery_included'] = delivery_included

        if fields:
            for field in fields.split(','):
                if field not in (
                        'FILTERS', 'FILTER_ALLVENDORS',
                        'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS',
                        'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT',
                        'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR',
                        'SHOP_ORGANIZATION', 'SHOP_RATING', 'SORTS', 'ALL', 'FILTER_ALL',
                        'OFFER_ALL', 'SHOP_ALL', 'STANDARD', 'VENDOR_ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if groupBy:
            if groupBy not in ('NONE', 'OFFER', 'SHOP'):
                raise YMAPI.GroupByParamError('"groupBy" param is wrong')
            params['groupBy'] = groupBy

        if shop_regions:
            params['shop_regions'] = shop_regions

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if how:
            if how not in ('ASC', 'DESC'):
                raise YMAPI.HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise YMAPI.GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise YMAPI.GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return ModelOffers(self.request('models/{id}/offers', req_id, params))

    def models_offers_default(self, req_id, fields='STANDARD', filters={}):
        params = {}

        if fields:
            for field in fields.split(','):
                if field not in (
                        'ACTIVE_FILTERS', 'CATEGORY',
                        'DELIVERY', 'DISCOUNT', 'OFFERS_LINK',
                        'OUTLET', 'OUTLET_COUNT', 'PHOTO', 'SHOP',
                        'SHOP_ORGANIZATION', 'SHOP_RATING', 'VENDOR',
                        'ALL', 'SHOP_ALL', 'STANDARD'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        return ModelOffersDefault(self.request('models/{id}/offers/default', req_id, params))

    def models_offers_stat(self, req_id):
        params = {}

        return ModelOffersStat(self.request('models/{id}/offers/default', req_id, params))

    def models_offers_filters(self, req_id, fields=None, filter_set=None, sort='NONE'):
        params = {}

        if fields:
            for field in fields.split(','):
                if field not in ('ALLVENDORS', 'DESCRIPTION', 'FOUND', 'SORTS', 'ALL', 'STANDARD'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if filter_set:
            if filter_set not in ('ALL', 'BASIC', 'POPULAR'):
                raise YMAPI.FilterSetParamError('"filter_set" param is wrong')
            params['filter_set'] = filter_set

        if sort:
            if sort not in ('NAME', 'NONE'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        return ModelOffersFilters(self.request('models/{id}/offers/filters', req_id, params))

    def offers(self, req_id, delivery_included=0, fields='STANDARD'):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if delivery_included:
            #     if delivery_included in [0,'0','F','FALSE','N','NO'
            params['delivery_included'] = delivery_included

        if fields:
            for field in fields.split(','):
                if field not in ('ACTIVE_FILTERS', 'CATEGORY',
                                 'DELIVERY', 'DISCOUNT', 'OFFERS_LINK',
                                 'OUTLET', 'OUTLET_COUNT', 'PHOTO', 'SHOP',
                                 'SHOP_ORGANIZATION', 'SHOP_RATING', 'VENDOR',
                                 'ALL', 'SHOP_ALL', 'STANDARD'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        return Offers(self.request('offers/{id}', req_id, params))

    def models_opinions(self, req_id, grade=None, max_comments=0, count=10, page=1, how=None, sort='DATE'):
        params = {}

        if grade < 1 or grade > 5:
            raise YMAPI.CountParamError('"grade" param must be between 1 and 5')

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        if how:
            if how not in ['ASC', 'DESC']:
                raise YMAPI.HowParamError('"how" param is wrong')
            params['how'] = how

        if sort:
            if sort not in ('DATE', 'GRADE', 'RANK'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        return ModelOpinions(self.request('offers/{id}', req_id, params))

    def shops_opinions(self, req_id, grade=None, max_comments=0, count=10, page=1, how=None, sort='DATE'):
        params = {}

        if grade < 1 or grade > 5:
            raise YMAPI.CountParamError('"grade" param must be between 1 and 5')

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        if how:
            if how not in ['ASC', 'DESC']:
                raise YMAPI.HowParamError('"how" param is wrong')
            params['how'] = how

        if sort:
            if sort not in ('DATE', 'GRADE', 'RANK'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        return ShopOpinions(self.request('shops/{id}', req_id, params))

    def shop(self, req_id, fields=None):
        params = {}

        if fields:
            for field in fields.split(','):
                if field not in ('ORGANIZATION', 'RATING',
                                 'ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        return Shop(self.request('shops/{id}', req_id, params))

    def shops(self, host, fields=None, geo_id=None):
        params = {'host': host}

        if geo_id is None:
            raise YMAPI.NoGeoIdOrIP(
                "You must provide geo_id")
        else:
            params['geo_id'] = geo_id

        if fields:
            for field in fields.split(','):
                if field not in ('ORGANIZATION', 'RATING',
                                 'ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        return Shops(self.request('shops', None, params))

    def geo_regions_shops_summary(self, req_id, fields='DELIVERY_COUNT,HOME_COUNT'):
        params = {}

        if fields:
            for field in fields.split(','):
                if field not in ('DELIVERY_COUNT', 'HOME_COUNT',
                                 'TOTAL_COUNT', 'ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        return ShopsSummary(self.request('geo/regions/{id}/shops/summary', req_id, params))

    def models_outlets(self, req_id, boundary=None, fields='STANDART', type='PICKUP,STORE', filters={}, count=10,
                       page=1, how=None, sort='RELEVANCY', latitude=None, longitude=None):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if boundary:
            params['boundary'] = boundary

        if fields:
            for field in fields.split(','):
                if field not in (
                        'OFFER', 'OFFER_ACTIVE_FILTERS',
                        'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT', 'OFFER_PHOTO',
                        'OFFER_SHOP', 'OFFER_VENDOR', 'SHOP',
                        'SHOP_ORGANIZATION', 'SHOP_RATING', 'ALL',
                        'OFFER_ALL', 'SHOP_ALL', 'STANDARD'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if type:
            for field in type.split(','):
                if field not in (
                        'PICKUP', 'STORE',
                        'ALL'):
                    raise YMAPI.TypeParamError('"fields" param is wrong')
            params['type'] = type

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        if how:
            if how not in ('ASC', 'DESC'):
                raise YMAPI.HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise YMAPI.GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise YMAPI.GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return Outlets(self.request('models/{id}/outlets', req_id, params))

    def shop_outlets(self, req_id, boundary=None, fields='STANDART', type='PICKUP,STORE', filters={}, count=10,
                     page=1, how=None, sort='RELEVANCY', latitude=None, longitude=None):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if boundary:
            params['boundary'] = boundary

        if fields:
            for field in fields.split(','):
                if field not in (
                        'OFFER', 'OFFER_ACTIVE_FILTERS',
                        'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT', 'OFFER_PHOTO',
                        'OFFER_SHOP', 'OFFER_VENDOR', 'SHOP',
                        'SHOP_ORGANIZATION', 'SHOP_RATING', 'ALL',
                        'OFFER_ALL', 'SHOP_ALL', 'STANDARD'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if type:
            for field in type.split(','):
                if field not in (
                        'PICKUP', 'STORE',
                        'ALL'):
                    raise YMAPI.TypeParamError('"fields" param is wrong')
            params['type'] = type

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        if how:
            if how not in ('ASC', 'DESC'):
                raise YMAPI.HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise YMAPI.GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise YMAPI.GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return Outlets(self.request('shops/{id}/outlets', req_id, params))

    def offer_outlets(self, req_id, boundary=None, fields='STANDART', type='PICKUP,STORE', filters={}, count=10,
                      page=1, how=None, sort='RELEVANCY', latitude=None, longitude=None):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if boundary:
            params['boundary'] = boundary

        if fields:
            for field in fields.split(','):
                if field not in (
                        'OFFER', 'OFFER_ACTIVE_FILTERS',
                        'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT', 'OFFER_PHOTO',
                        'OFFER_SHOP', 'OFFER_VENDOR', 'SHOP',
                        'SHOP_ORGANIZATION', 'SHOP_RATING', 'ALL',
                        'OFFER_ALL', 'SHOP_ALL', 'STANDARD'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if type:
            for field in type.split(','):
                if field not in (
                        'PICKUP', 'STORE',
                        'ALL'):
                    raise YMAPI.TypeParamError('"fields" param is wrong')
            params['type'] = type

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        if how:
            if how not in ('ASC', 'DESC'):
                raise YMAPI.HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise YMAPI.SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise YMAPI.GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise YMAPI.GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return Outlets(self.request('offers/{id}/outlets', req_id, params))

    def geo_regions(self, req_id, fields='STANDART', count=10, page=1):
        params = {'count': count,
                  'page': page}

        if fields:
            for field in fields.split(','):
                if field not in (
                        'DECLENSIONS', 'PARENT', 'ALL'):
                    raise YMAPI.FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if count < 1 or count > 30:
            raise YMAPI.CountParamError('"count" param must be between 1 and 30')

        if page < 1:
            raise YMAPI.PageParamError('"page" param must be larger than 1')

        return Regions(self.request('geo/regions', req_id, params))
