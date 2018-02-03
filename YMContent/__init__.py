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
from .exceptions import *


class YMAPI(object):

    def __init__(self, authorization_key=None):
        """

        :param authorization_key: Авторизационный ключ
        :type authorization_key: str
        """
        if not authorization_key:
            raise NotAuthorized(
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

    def _request(self, resource, req_id, params):
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
                raise BaseAPIError(
                    data['errors'][0]['message'])
            return response

        except (ConnectionError, ProtocolError, ReadTimeout, ReadTimeoutError, SSLError, ssl.SSLError,
                socket.error) as exception:
            pass

    def _validate_fields(self, fields, values):
        if type(fields) == list:
            for field in fields:
                if field.upper() not in values:
                    raise FieldsParamError('"fields" param is wrong')
        elif type(fields) == str:
            for field in fields.split(','):
                if field.strip() not in values:
                    raise FieldsParamError('"fields" param is wrong')
        else:
            raise FieldsParamError('"fields" param is wrong')
        return fields

    def categories(self, fields=None, sort='NONE', geo_id=None, remote_ip=None, count=10, page=1):
        """
        Список категорий

        :param fields: Параметры категории, которые необходимо показать в выходных данных
        :type fields: str

        :param sort: Тип сортировки категорий
        :type sort: str

        :param geo_id: Идентификатор региона
        :type geo_id: int

        :param remote_ip: Идентификатор региона пользователя
        :type remote_ip: int

        :param count: IP-адрес пользователя
        :type count: str

        :param page: Номер страницы
        :type page: int

        :return: Список категорий первого уровня (корневых) товарного дерева :class:`response.Categories`
        :rtype: list[response.Categories]

        :raises FieldsParamError: неверное значение параметра fields
        :raises SortParamError: неверное значение параметра sort
        :raises NoGeoIdOrIP: не передан обязательный параметр geo_id или remote_ip
        :raises CountParamError: недопустимое значение параметра count
        :raises PageParamError: недопустимое значение параметра count

        .. seealso:: https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/category-controller-v2-get-root-categories-docpage/
        """
        params = {}

        if fields:
            params['fields'] = self._validate_fields(fields, ('ALL', 'PARENT', 'STATISTICS', 'WARNINGS'))

        if sort:
            if sort.upper() not in ('BY_NAME', 'BY_OFFERS_NUM', 'NONE'):
                raise SortParamError('"sort" param is wrong')
            params['sort'] = sort

        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        return Categories(self._request('categories', None, params))

    def categories_children(self, category_id=None, fields=None, sort='NONE', geo_id=None, remote_ip=None, count=10,
                            page=1):
        """
        Список подкатегорий

        :param category_id: Идентификатор категории
        :type category_id: int

        :param fields: Параметры категории, которые необходимо показать в выходных данных
        :type fields: str or list[str]

        :param sort: Тип сортировки категорий
        :type sort: str

        :param geo_id: Идентификатор региона
        :type geo_id: int

        :param remote_ip: Идентификатор региона пользователя
        :type remote_ip: int

        :param count: IP-адрес пользователя
        :type count: str

        :param page: Номер страницы
        :type page: int

        :return: Список категорий товарного дерева, вложенных в категорию с указанным в запросе идентификатором
        :rtype: list[response.CategoriesChildren]

        :raises FieldsParamError: неверное значение параметра fields
        :raises SortParamError: неверное значение параметра sort
        :raises NoGeoIdOrIP: не передан обязательный параметр geo_id или remote_ip
        :raises CountParamError: недопустимое значение параметра count
        :raises PageParamError: недопустимое значение параметра count

        .. seealso:: https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/category-controller-v2-get-children-categories-docpage/
        """
        params = {}
        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")
        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        if fields:
            params['fields'] = self._validate_fields(fields, ('ALL', 'PARENT', 'STATISTICS', 'WARNINGS'))

        if sort:
            if sort not in ('BY_NAME', 'BY_OFFERS_NUM', 'NONE'):
                raise SortParamError('"sort" param is wrong')
            params['sort'] = sort

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        return CategoriesChildren(self._request('categories/{}/children', category_id, params))

    def category(self, category_id=None, fields=None, geo_id=None, remote_ip=None):
        """
        Информация о категории

        :param category_id: Идентификатор категории
        :type category_id: int

        :param fields: Параметры категории, которые необходимо показать в выходных данных
        :type fields: str or list[str]

        :param geo_id: Идентификатор региона
        :type geo_id: int

        :param remote_ip: Идентификатор региона пользователя
        :type remote_ip: int

        :return: Информация о категории
        :rtype: response.Category

        :raises FieldsParamError: неверное значение параметра fields
        :raises NoGeoIdOrIP: не передан обязательный параметр geo_id или remote_ip

        .. seealso:: https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/category-controller-v2-get-category-docpage/
        """
        params = {}
        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")
        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        if fields:
            params['fields'] = self._validate_fields(fields, ('ALL', 'PARENT', 'STATISTICS', 'WARNINGS'))

        return Category(self._request('categories/{}', category_id, params))

    def categories_filters(self, category_id=None, geo_id=None, remote_ip=None, fields=None, filter_set='POPULAR',
                           rs=None,
                           sort='NONE', filters=None):
        """
        Список фильтров категории

        :param category_id: Идентификатор категории
        :type category_id: int

        :param fields: Параметры категории, которые необходимо показать в выходных данных
        :type fields: str or list[str]

        :param geo_id: Идентификатор региона
        :type geo_id: int

        :param remote_ip: Идентификатор региона пользователя
        :type remote_ip: int

        :param filter_set: Набор фильтров в выходных данных
        :type filter_set: str or list[str]

        :param rs: Поле содержащее закодированную информацию о текстовом запросе после редиректа, на которую будет ориентироваться поиск
        :type rs: str

        :param sort: Тип сортировки категорий
        :type sort: str

        :param filters: Условия фильтрации моделей и предложений на модель
        :type filters: dict

        :return: Cписок фильтров для фильтрации моделей и товарных предложений в указанной категории
        :rtype: response.CategoriesFilters

        :raises FieldsParamError: неверное значение параметра fields
        :raises NoGeoIdOrIP: не передан обязательный параметр geo_id или remote_ip

        .. seealso:: https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/category-controller-v2-get-category-filters-docpage/
        """
        params = {}
        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")
        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     ('ALLVENDORS', 'DESCRIPTION', 'FOUND', 'SORTS', 'ALL', 'STANDARD'))

        if filter_set:
            for field in filter_set.split(','):
                if field not in ('ALL', 'BASIC', 'POPULAR'):
                    raise FilterSetParamError('"filter_set" param is wrong')
            params['filter_set'] = filter_set

        if sort:
            if sort not in ('NAME', 'NONE'):
                raise SortParamError('"sort" param is wrong')
            params['sort'] = sort

        if rs:
            params['rs'] = rs

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        return CategoriesFilters(self._request('categories/{}/filters', category_id, params))

    def categories_match(self, name, category_name=None, description=None, locale='RU_ru', price=None,
                         shop_name=None):
        """
        Подбор категорий по параметрам

        :param name: Имя
        :type name: str

        :param category_name: Наименование категории
        :type category_name: str

        :param description: Описание модели
        :type description: str

        :param locale: Локаль поиска
        :type locale: str

        :param price: Цена модели
        :type price: str

        :param shop_name: Наименование магазина
        :type shop_name: str

        :return: Подобранные категории
        :rtype: response.Category

        .. seealso:: https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/category-controller-v2-match-docpage/
        """
        params = {'name': name, 'locale': locale}

        if category_name:
            params['category_name'] = category_name

        if description:
            params['description'] = description

        if price:
            params['price'] = price

        if shop_name:
            params['shop_name'] = shop_name

        return Category(self._request('categories/match', None, params))

    def model(self, model_id, fields='CATEGORY,PHOTO', filters=None, geo_id=None, remote_ip=None):
        """
        Информация о модели

        :param model_id: Идентификатор модели
        :type model_id: int

        :param fields: Свойства модели, которые необходимо показать в выходных данных
        :type fields: str or list[str]

        :param filters: Условия фильтрации моделей и предложений на модель
        :type filters: dict

        :param geo_id: Идентификатор региона
        :type geo_id: int

        :param remote_ip: Идентификатор региона пользователя
        :type remote_ip: int

        :return: Информация о модели
        :rtype: response.Model

        .. seealso:: https://tech.yandex.ru/market/content-data/doc/dg-v2/reference/models-controller-v2-get-model-docpage/
        """
        params = {}
        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")
        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     ('CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS',
                                                      'FILTER_ALLVENDORS',
                                                      'FILTER_COLOR',
                                                      'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA',
                                                      'MODIFICATIONS',
                                                      'NAVIGATION_NODE',
                                                      'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS',
                                                      'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                                                      'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY',
                                                      'OFFER_DISCOUNT',
                                                      'OFFER_OFFERS_LINK',
                                                      'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR',
                                                      'PHOTO', 'PHOTOS', 'PRICE',
                                                      'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION',
                                                      'VENDOR', 'ALL', 'FILTER_ALL',
                                                      'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD',
                                                      'VENDOR_ALL'))

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        return Model(self._request('models/{}', model_id, params))

    def models_reviews(self, req_id, count=10, page=1):
        params = {'count': count,
                  'page': page
                  }
        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        return ModelReview(self._request('models/{id}/reviews', req_id, params))

    def models_match(self, name, category_count=1, fields='CATEGORY,PHOTO', match_types='MULTI,REPORT',
                     category_name=None, description=None, locale='RU_ru', price=None, shop_name=None, category_id=None,
                     hid=None):
        params = {'category_count': category_count,
                  'fields': fields,
                  'match_types': match_types,
                  'name': name, 'locale': locale}

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS',
                                                         'FILTER_ALLVENDORS',
                                                         'FILTER_COLOR',
                                                         'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA',
                                                         'MODIFICATIONS',
                                                         'NAVIGATION_NODE',
                                                         'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS',
                                                         'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                                                         'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY',
                                                         'OFFER_DISCOUNT',
                                                         'OFFER_OFFERS_LINK',
                                                         'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR',
                                                         'PHOTO', 'PHOTOS', 'PRICE',
                                                         'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION',
                                                         'VENDOR', 'ALL', 'FILTER_ALL',
                                                         'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD',
                                                         'VENDOR_ALL'))

        if match_types:
            for match_type in match_types.split(','):
                if match_type not in (
                        'BATCH', 'MULTI', 'MULTI_STRING', 'REPORT', 'STRING', 'ALL'):
                    raise MatchTypeParamError('"match_types" param is wrong')

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

        return Models(self._request('models/match', None, params))

    def models_lookas(self, req_id, count=10, fields='CATEGORY,PHOTO'):
        params = {'count': count,
                  'fields': fields}

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS',
                                                         'FILTER_ALLVENDORS',
                                                         'FILTER_COLOR',
                                                         'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA',
                                                         'MODIFICATIONS',
                                                         'NAVIGATION_NODE',
                                                         'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS',
                                                         'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                                                         'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY',
                                                         'OFFER_DISCOUNT',
                                                         'OFFER_OFFERS_LINK',
                                                         'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR',
                                                         'PHOTO', 'PHOTOS', 'PRICE',
                                                         'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION',
                                                         'VENDOR', 'ALL', 'FILTER_ALL',
                                                         'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD',
                                                         'VENDOR_ALL'))

        return ModelsLookas(self._request('models/{id}/looksas', req_id, params))

    def categories_bestdeals(self, req_id, fields='CATEGORY,PHOTO', count=10, page=1):
        params = {'count': count,
                  'fields': fields}

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS',
                                                         'FILTER_ALLVENDORS',
                                                         'FILTER_COLOR',
                                                         'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA',
                                                         'MODIFICATIONS',
                                                         'NAVIGATION_NODE',
                                                         'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS',
                                                         'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                                                         'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY',
                                                         'OFFER_DISCOUNT',
                                                         'OFFER_OFFERS_LINK',
                                                         'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR',
                                                         'PHOTO', 'PHOTOS', 'PRICE',
                                                         'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION',
                                                         'VENDOR', 'ALL', 'FILTER_ALL',
                                                         'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD',
                                                         'VENDOR_ALL'))

        return CategoriesLookas(self._request('categories/{id}/bestdeals', req_id, params))

    def categories_popular(self, req_id, fields='CATEGORY,PHOTO', count=10, page=1, geo_id=None, remote_ip=None):
        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        params = {'count': count,
                  'fields': fields}

        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'CATEGORY', 'DEFAULT_OFFER', 'DISCOUNTS', 'FACTS', 'FILTERS',
                                                         'FILTER_ALLVENDORS',
                                                         'FILTER_COLOR',
                                                         'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS', 'MEDIA',
                                                         'MODIFICATIONS',
                                                         'NAVIGATION_NODE',
                                                         'NAVIGATION_NODE_DATASOURCE', 'NAVIGATION_NODE_ICONS',
                                                         'NAVIGATION_NODE_STATISTICS', 'OFFERS',
                                                         'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY',
                                                         'OFFER_DISCOUNT',
                                                         'OFFER_OFFERS_LINK',
                                                         'OFFER_OUTLET', 'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR',
                                                         'PHOTO', 'PHOTOS', 'PRICE',
                                                         'RATING', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SPECIFICATION',
                                                         'VENDOR', 'ALL', 'FILTER_ALL',
                                                         'NAVIGATION_NODE_ALL', 'OFFER_ALL', 'SHOP_ALL', 'STANDARD',
                                                         'VENDOR_ALL'))

        return CategoriesPopular(self._request('categories/{id}/populars', req_id, params))

    def models_offers(self, req_id, delivery_included=False, fields=None, groupBy=None, shop_regions=None, filters=None,
                      count=10, page=1, how=None, sort=None, latitude=None, longitude=None):
        params = {}

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        # ToDO нужно добавить преобразование типа в эталонный
        if delivery_included:
            #     if delivery_included in [0,'0','F','FALSE','N','NO'
            params['delivery_included'] = delivery_included

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'FILTERS', 'FILTER_ALLVENDORS',
                                                         'FILTER_DESCRIPTION', 'FILTER_FOUND', 'FILTER_SORTS',
                                                         'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY',
                                                         'OFFER_DISCOUNT',
                                                         'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT',
                                                         'OFFER_PHOTO', 'OFFER_SHOP', 'OFFER_VENDOR',
                                                         'SHOP_ORGANIZATION', 'SHOP_RATING', 'SORTS', 'ALL',
                                                         'FILTER_ALL',
                                                         'OFFER_ALL', 'SHOP_ALL', 'STANDARD', 'VENDOR_ALL'))

        if groupBy:
            if groupBy not in ('NONE', 'OFFER', 'SHOP'):
                raise GroupByParamError('"groupBy" param is wrong')
            params['groupBy'] = groupBy

        if shop_regions:
            params['shop_regions'] = shop_regions

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if how:
            if how not in ('ASC', 'DESC'):
                raise HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return ModelOffers(self._request('models/{id}/offers', req_id, params))

    def models_offers_default(self, req_id, fields='STANDARD', filters=None):
        params = {}

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'ACTIVE_FILTERS', 'CATEGORY',
                                                         'DELIVERY', 'DISCOUNT', 'OFFERS_LINK',
                                                         'OUTLET', 'OUTLET_COUNT', 'PHOTO', 'SHOP',
                                                         'SHOP_ORGANIZATION', 'SHOP_RATING', 'VENDOR',
                                                         'ALL', 'SHOP_ALL', 'STANDARD'))

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        return ModelOffersDefault(self._request('models/{id}/offers/default', req_id, params))

    def models_offers_stat(self, req_id):
        params = {}

        return ModelOffersStat(self._request('models/{id}/offers/default', req_id, params))

    def models_offers_filters(self, req_id, fields=None, filter_set=None, sort='NONE'):
        params = {}

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     ('ALLVENDORS', 'DESCRIPTION', 'FOUND', 'SORTS', 'ALL', 'STANDARD'))

        if filter_set:
            if filter_set not in ('ALL', 'BASIC', 'POPULAR'):
                raise FilterSetParamError('"filter_set" param is wrong')
            params['filter_set'] = filter_set

        if sort:
            if sort not in ('NAME', 'NONE'):
                raise SortParamError('"sort" param is wrong')

        return ModelOffersFilters(self._request('models/{id}/offers/filters', req_id, params))

    def offers(self, req_id, delivery_included=0, fields='STANDARD'):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if delivery_included:
            #     if delivery_included in [0,'0','F','FALSE','N','NO'
            params['delivery_included'] = delivery_included

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     ('ACTIVE_FILTERS', 'CATEGORY',
                                                      'DELIVERY', 'DISCOUNT', 'OFFERS_LINK',
                                                      'OUTLET', 'OUTLET_COUNT', 'PHOTO', 'SHOP',
                                                      'SHOP_ORGANIZATION', 'SHOP_RATING', 'VENDOR',
                                                      'ALL', 'SHOP_ALL', 'STANDARD'))

        return Offers(self._request('offers/{id}', req_id, params))

    def models_opinions(self, req_id, grade=None, max_comments=0, count=10, page=1, how=None, sort='DATE'):
        params = {}

        if grade < 1 or grade > 5:
            raise CountParamError('"grade" param must be between 1 and 5')

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if how:
            if how not in ['ASC', 'DESC']:
                raise HowParamError('"how" param is wrong')
            params['how'] = how

        if sort:
            if sort not in ('DATE', 'GRADE', 'RANK'):
                raise SortParamError('"sort" param is wrong')

        return ModelOpinions(self._request('offers/{id}', req_id, params))

    def shops_opinions(self, req_id, grade=None, max_comments=0, count=10, page=1, how=None, sort='DATE'):
        params = {}

        if grade:
            if grade < 1 or grade > 5:
                raise CountParamError('"grade" param must be between 1 and 5')
            params['grade'] = grade

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if how:
            if how not in ['ASC', 'DESC']:
                raise HowParamError('"how" param is wrong')
            params['how'] = how

        if sort:
            if sort not in ('DATE', 'GRADE', 'RANK'):
                raise SortParamError('"sort" param is wrong')

        return ShopOpinions(self._request('shops/{id}/opinions', req_id, params))

    def shop(self, req_id, fields=None):
        params = {}

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     ('ORGANIZATION', 'RATING',
                                                      'ALL'))

        return Shop(self._request('shops/{id}', req_id, params))

    def shops(self, host, fields=None, geo_id=None):
        params = {'host': host}

        if geo_id is None:
            raise NoGeoIdOrIP(
                "You must provide geo_id")
        else:
            params['geo_id'] = geo_id

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     ('ORGANIZATION', 'RATING',
                                                      'ALL'))

        return Shops(self._request('shops', None, params))

    def geo_regions_shops_summary(self, req_id, fields='DELIVERY_COUNT,HOME_COUNT'):
        params = {}

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     ('DELIVERY_COUNT', 'HOME_COUNT',
                                                      'TOTAL_COUNT', 'ALL'))

        return ShopsSummary(self._request('geo/regions/{id}/shops/summary', req_id, params))

    def models_outlets(self, req_id, boundary=None, fields='STANDART', type='PICKUP,STORE', filters=None, count=10,
                       page=1, how=None, sort='RELEVANCY', latitude=None, longitude=None):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if boundary:
            params['boundary'] = boundary

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'OFFER', 'OFFER_ACTIVE_FILTERS',
                                                         'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                                                         'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT',
                                                         'OFFER_PHOTO',
                                                         'OFFER_SHOP', 'OFFER_VENDOR', 'SHOP',
                                                         'SHOP_ORGANIZATION', 'SHOP_RATING', 'ALL',
                                                         'OFFER_ALL', 'SHOP_ALL', 'STANDARD'))

        if type:
            for field in type.split(','):
                if field not in (
                        'PICKUP', 'STORE',
                        'ALL'):
                    raise TypeParamError('"fields" param is wrong')
            params['type'] = type

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page
        if how:
            if how not in ('ASC', 'DESC'):
                raise HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return Outlets(self._request('models/{id}/outlets', req_id, params))

    def shop_outlets(self, req_id, boundary=None, fields='STANDART', type='PICKUP,STORE', filters=None, count=10,
                     page=1, how=None, sort='RELEVANCY', latitude=None, longitude=None):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if boundary:
            params['boundary'] = boundary

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'OFFER', 'OFFER_ACTIVE_FILTERS',
                                                         'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                                                         'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT',
                                                         'OFFER_PHOTO',
                                                         'OFFER_SHOP', 'OFFER_VENDOR', 'SHOP',
                                                         'SHOP_ORGANIZATION', 'SHOP_RATING', 'ALL',
                                                         'OFFER_ALL', 'SHOP_ALL', 'STANDARD'))

        if type:
            for field in type.split(','):
                if field not in (
                        'PICKUP', 'STORE',
                        'ALL'):
                    raise TypeParamError('"fields" param is wrong')
            params['type'] = type

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if how:
            if how not in ('ASC', 'DESC'):
                raise HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return Outlets(self._request('shops/{id}/outlets', req_id, params))

    def offer_outlets(self, req_id, boundary=None, fields='STANDART', type='PICKUP,STORE', filters=None, count=10,
                      page=1, how=None, sort='RELEVANCY', latitude=None, longitude=None):
        params = {}

        # ToDO нужно добавить преобразование типа в эталонный
        if boundary:
            params['boundary'] = boundary

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'OFFER', 'OFFER_ACTIVE_FILTERS',
                                                         'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                                                         'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT',
                                                         'OFFER_PHOTO',
                                                         'OFFER_SHOP', 'OFFER_VENDOR', 'SHOP',
                                                         'SHOP_ORGANIZATION', 'SHOP_RATING', 'ALL',
                                                         'OFFER_ALL', 'SHOP_ALL', 'STANDARD'))

        if type:
            for field in type.split(','):
                if field not in (
                        'PICKUP', 'STORE',
                        'ALL'):
                    raise TypeParamError('"fields" param is wrong')
            params['type'] = type

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if how:
            if how not in ('ASC', 'DESC'):
                raise HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return Outlets(self._request('offers/{id}/outlets', req_id, params))

    def geo_regions(self, req_id, fields='STANDART', count=10, page=1):
        params = {'count': count,
                  'page': page}

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'DECLENSIONS', 'PARENT', 'ALL'))

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        return Regions(self._request('geo/regions', req_id, params))

    def geo_regions_children(self, req_id, fields=None, count=10, page=1):
        params = {'count': count,
                  'page': page}

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'DECLENSIONS', 'PARENT', 'ALL'))

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        return Regions(self._request('geo/regions/{id}/children', req_id, params))

    def geo_regions_children(self, req_id, fields=None, count=10, page=1):
        params = {'count': count,
                  'page': page}

        if fields:
            params['fields'] = self._validate_fields(fields,
                                                     (
                                                         'DECLENSIONS', 'PARENT', 'ALL'))

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        return Regions(self._request('geo/regions/{id}/children', req_id, params))

    def geo_regions(self, req_id, fields=None, count=10, page=1):
        params = {}

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if fields:
            for field in fields.split(','):
                if field not in (
                        'DECLENSIONS', 'PARENT', 'ALL'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        return Region(self._request('geo/regions/{id}', req_id, params))

    def geo_regions_children(self, fields=None,
                             types='CITY, CITY_DISTRICT, REGION, RURAL_SETTLEMENT, SECONDARY_DISTRICT, VILLAGE',
                             count=10, page=1):
        params = {}

        if fields:
            for field in fields.split(','):
                if field not in (
                        'DECLENSIONS', 'PARENT', 'ALL'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if types:
            for field in types.split(','):
                if field not in (
                        'AIRPORT', 'CITY', 'CITY_DISTRICT', 'CONTINENT', 'COUNTRY', 'COUNTRY_DISTRICT', 'METRO_STATION',
                        'MONORAIL_STATION', 'OVERSEAS_TERRITORY', 'REGION', 'RURAL_SETTLEMENT', 'SECONDARY_DISTRICT',
                        'SUBJECT_FEDERATION', 'SUBJECT_FEDERATION_DISTRICT', 'VILLAGE', 'ALL'):
                    raise TypeParamError('"type" param is wrong')
            params['fields'] = fields

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        return Suggests(self._request('geo/suggest', None, params))

    def vendors(self, fields=None, count=10, page=1):
        params = {}

        if fields:
            for field in fields.split(','):
                if field not in (
                        'CATEGORIES', 'CATEGORY_PARENT', 'CATEGORY_STATISTICS', 'CATEGORY_WARNINGS', 'TOP_CATEGORIES',
                        'ALL'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        return Vendors(self._request('vendors', None, params))

    def vendor(self, req_id, fields=None):
        params = {}

        if fields:
            for field in fields.split(','):
                if field not in (
                        'CATEGORIES', 'CATEGORY_PARENT', 'CATEGORY_STATISTICS', 'CATEGORY_WARNINGS', 'TOP_CATEGORIES',
                        'ALL'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        return Vendor(self._request('vendors/{id}', req_id, params))

    def vendors_match(self, name, fields=None):
        params = {'name': name}

        if fields:
            for field in fields.split(','):
                # todo добавить всюду CATEGORY_ALL
                if field not in (
                        'CATEGORIES', 'CATEGORY_PARENT', 'CATEGORY_STATISTICS', 'CATEGORY_WARNINGS', 'TOP_CATEGORIES',
                        'ALL'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        return Vendor(self._request('vendors/match', None, params))

    def search(self, text, delivery_included=False, fields=None, onstock=0, outlet_types=None, price_max=None,
               price_min=None, result_type='ALL', shop_id=None, warranty=0, filters=None, barcode=False,
               search_type=None,
               category_id=None, hid=None, count=10, page=1, how=None, sort=None, latitude=None, longitude=None,
               geo_id=None, remote_ip=None):

        params = {'text': text}

        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        # ToDO нужно добавить преобразование типа в эталонный
        if delivery_included:
            #     if delivery_included in [0,'0','F','FALSE','N','NO'
            params['delivery_included'] = delivery_included

        if fields:
            for field in fields.split(','):
                if field not in (
                        'FILTERS', 'FOUND_CATEGORIES',
                        'MODEL_CATEGORY', 'MODEL_DEFAULT_OFFER', 'MODEL_DISCOUNTS',
                        'MODEL_FACTS', 'MODEL_FILTER_COLOR', 'MODEL_MEDIA', 'MODEL_NAVIGATION_NODE',
                        'MODEL_OFFERS', 'MODEL_PHOTO', 'MODEL_PHOTOS',
                        'MODEL_PRICE', 'MODEL_RATING', 'MODEL_SPECIFICATION',
                        'MODEL_VENDOR', 'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT', 'OFFER_PHOTO',
                        'OFFER_PHOTO', 'OFFER_VENDOR', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SORTS', 'ALL', 'MODEL_ALL',
                        'OFFER_ALL', 'SHOP_ALL', 'STANDARD'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        # ToDO нужно добавить преобразование типа в эталонный
        if onstock:
            #     if onstock in [0,'0','F','FALSE','N','NO'
            params['onstock'] = onstock

        if outlet_types:
            for field in outlet_types.split(','):
                if field not in (
                        'DELIVERY', 'PICKUP', 'STORE', 'ALL'):
                    raise FieldsParamError('"fields" param is wrong')
            params['outlet_types'] = outlet_types

        if price_max:
            params['price_max'] = price_max

        if price_min:
            params['price_min'] = price_min

        if result_type:
            if result_type not in (
                    'ALL', 'MODELS', 'OFFERS'):
                raise ResultTypeParamError('"result_type" param is wrong')
            params['fields'] = fields

        if shop_id:
            params['shop_id'] = shop_id

        # ToDO нужно добавить преобразование типа в эталонный
        if warranty:
            #     if onstock in [0,'0','F','FALSE','N','NO'
            params['warranty'] = warranty

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if barcode:
            params['barcode'] = barcode
            # todo Параметр действует только, если не указан search_type

        if search_type:
            if search_type not in (
                    'BARCODE', 'ISBN', 'TEXT'):
                raise SearchTypeParamError('"search_type" param is wrong')
            params['search_type'] = search_type

        if category_id:
            params['category_id'] = category_id

        if hid:
            params['hid'] = hid

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if how:
            if how not in ('ASC', 'DESC'):
                raise HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise SortParamError('"sort" param is wrong')

        # Todo Ограничение. Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        # todo Ограничение. Оба парметра должны быть определены совместно. Не допускается указывать один без другого.

        if latitude:
            if latitude < -90 or latitude > 90:
                raise GeoParamError('"latitude" param must be between -90 and 90')
            params['latitude'] = latitude

        if longitude:
            if longitude < -180 or longitude > 180:
                raise GeoParamError('"longitude" param must be between -180 and 180')
            params['longitude'] = longitude

        return Search(self._request('search', None, params))

    def categories_search(self, req_id, geo_id=None, remote_ip=None, fields=None, result_type='ALL', rs=None,
                          shop_regions=None, filters=None,
                          count=10, page=1, how=None, sort=None):

        params = {}

        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        if fields:
            for field in fields.split(','):
                if field not in (
                        'MODEL_CATEGORY', 'MODEL_DEFAULT_OFFER', 'MODEL_DISCOUNTS',
                        'MODEL_FACTS', 'MODEL_FILTER_COLOR', 'MODEL_MEDIA', 'MODEL_NAVIGATION_NODE',
                        'MODEL_OFFERS', 'MODEL_PHOTO', 'MODEL_PHOTOS',
                        'MODEL_PRICE', 'MODEL_RATING', 'MODEL_SPECIFICATION',
                        'MODEL_VENDOR', 'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT', 'OFFER_PHOTO',
                        'OFFER_PHOTO', 'OFFER_VENDOR', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'ALL', 'MODEL_ALL',
                        'OFFER_ALL', 'SHOP_ALL', 'STANDARD'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if result_type:
            if result_type not in (
                    'ALL', 'MODELS', 'OFFERS'):
                raise ResultTypeParamError('"result_type" param is wrong')
            params['result_type'] = result_type

        if rs:
            params['rs'] = rs

        if shop_regions:
            params['shop_regions'] = shop_regions

        if filters:
            for (k, v) in filters.items():
                params[k] = v

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if how:
            if how not in ('ASC', 'DESC'):
                raise HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise SortParamError('"sort" param is wrong')

        return Search(self._request('categories/{id}/search', req_id, params))

    def search_filters(self, text, fields=None):
        params = {'text': text}

        if fields:
            for field in fields.split(','):
                if field not in (
                        'ALLVENDORS', 'DESCRIPTION', 'FOUND',
                        'SORTS', 'ALL', 'STANDARD'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        return CategoriesFilters(self._request('search/filters', None, params))

    def redirect(self, text, redirect_types='SEARCH', barcode=False, search_type=None, category_id=None, hid=None,
                 fields=None, user_agent=None, count=10, page=1, how=None, sort=None, geo_id=None, remote_ip=None):
        params = {'text': text}

        if geo_id is None and remote_ip is None:
            raise NoGeoIdOrIP(
                "You must provide either geo_id or remote_ip")

        if geo_id:
            params['geo_id'] = geo_id

        if remote_ip:
            params['remote_ip'] = remote_ip

        if redirect_types:
            for field in redirect_types.split(','):
                if field not in (
                        'CATALOG', 'MODEL', 'SEARCH',
                        'VENDOR', 'ALL'):
                    raise RedirectTypesParamError('"redirect_types" param is wrong')
            params['redirect_types'] = redirect_types

        # todo Ограничение. Параметр действует только, если не указан search_type
        if barcode:
            params['barcode'] = barcode

        if search_type:
            if search_type not in (
                    'BARCODE', 'ISBN', 'TEXT'):
                raise RedirectTypesParamError('"redirect_types" param is wrong')
            params['search_type'] = search_type

        if category_id:
            params['category_id'] = category_id

        if hid:
            params['hid'] = hid

        if fields:
            for field in fields.split(','):
                if field not in (
                        'CATEGORY_PARENT', 'CATEGORY_STATISTICS', 'CATEGORY_WARNINGS',
                        'FILTERS', 'FOUND_CATEGORIES', 'MODEL_CATEGORY', 'MODEL_DEFAULT_OFFER', 'MODEL_DISCOUNTS',
                        'MODEL_FACTS', 'MODEL_FILTER_COLOR', 'MODEL_MEDIA', 'MODEL_NAVIGATION_NODE', 'MODEL_OFFERS',
                        'MODEL_PHOTO', 'MODEL_PHOTOS', 'MODEL_PRICE', 'MODEL_RATING', 'MODEL_SPECIFICATION',
                        'MODEL_VENDOR', 'OFFER_ACTIVE_FILTERS', 'OFFER_CATEGORY', 'OFFER_DELIVERY', 'OFFER_DISCOUNT',
                        'OFFER_OFFERS_LINK', 'OFFER_OUTLET', 'OFFER_OUTLET_COUNT', 'OFFER_PHOTO', 'OFFER_SHOP',
                        'OFFER_VENDOR', 'SHOP_ORGANIZATION', 'SHOP_RATING', 'SORTS', 'VENDOR_CATEGORIES',
                        'VENDOR_TOP_CATEGORIES', 'ALL', 'CATEGORY_ALL', 'MODEL_ALL', 'OFFER_ALL', 'SHOP_ALL',
                        'STANDARD', 'VENDOR_ALL'):
                    raise FieldsParamError('"fields" param is wrong')
            params['fields'] = fields

        if user_agent:
            params['user_agent'] = user_agent

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if how:
            if how not in ('ASC', 'DESC'):
                raise HowParamError('"how" param is wrong')

        if sort:
            if sort not in (
                    'DATE', 'DELIVERY_TIME', 'DISCOUNT', 'DISTANCE', 'NOFFERS', 'OPINIONS', 'POPULARITY', 'PRICE',
                    'QUALITY',
                    'RATING', 'RELEVANCY'):
                raise SortParamError('"sort" param is wrong')

        return Redirect(self._request('redirect', None, params))

    def suggestions(self, text, count=10, page=1, pos=None, suggest_types='DEFAULT'):
        params = {'text': text,
                  'count': count}

        if count < 1 or count > 30:
            raise CountParamError('"count" param must be between 1 and 30')
        else:
            params['count'] = count

        if page < 1:
            raise PageParamError('"page" param must be larger than 1')
        else:
            params['page'] = page

        if pos:
            params['pos'] = pos

        if suggest_types:
            for field in suggest_types.split(','):
                if field not in (
                        'CATALOG', 'MODEL', 'SEARCH',
                        'VENDOR', 'ALL', 'DEFAULT'):
                    raise RedirectTypesParamError('"redirect_types" param is wrong')
            params['suggest_types'] = suggest_types

        return Suggestions(self._request('redirect', None, params))
