# -*- coding: utf-8 -*-
from YMContent.objects import *


class Base(object):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()
        self.headers = r.headers

    def json(self):
        """

        :return: ответ в формате JSON
        :rtype: dict
        """
        return self.resp

    def curl(self):
        """

        :return: Эквивалент команды curl
        :rtype: str
        """
        headers = ["'{0}: {1}'".format(k, v) for k, v in self.req.request.headers.items()]
        headers = " -H ".join(sorted(headers))

        command = "curl -X {method} -H {headers} -d '{data}' '{uri}'".format(
            data=self.req.request.body or "",
            headers=headers,
            method=self.req.request.method,
            uri=self.req.request.url,
        )
        return command

    def is_ok(self):
        """

        :return: Статус корректности запроса
        :rtype: bool
        """
        return self.resp.get('status') == 'OK'

    @property
    def http_status_code(self):
        """

        :return: HTTP статус обработки запроса
        :rtype: int
        """
        return self.req.status_code

    @property
    def daily_limit(self):
        """

        :return: возможное количество запросов в сутки
        :rtype: int
        """
        return int(self.headers.get('X-RateLimit-Daily-Limit'))

    @property
    def daily_remaining(self):
        """

        :return: оставшееся количество запросов до превышения суточного ограничения
        :rtype: int
        """
        return int(self.headers.get('X-RateLimit-Daily-Remaining'))

    @property
    def daily_until(self):
        """

        :return: время обновления суточного ограничения
        :rtype: str
        """
        return self.headers.get('X-RateLimit-Daily-Until')

    @property
    def global_limit(self):
        """

        :return: возможное количество запросов в определенный промежуток времени
        :rtype: int
        """
        return int(self.headers.get('X-RateLimit-Global-Limit'))

    @property
    def global_remaining(self):
        """

        :return: оставшееся количество запросов в определенный промежуток времени до превышения глобального ограничения
        :rtype: int
        """
        return int(self.headers.get('X-RateLimit-Global-Remaining'))

    @property
    def global_until(self):
        """

        :return: время обновления глобального посекундного ограничения
        :rtype: str
        """
        return self.headers.get('X-RateLimit-Global-Until')

    @property
    def method_limit(self):
        """

        :return: возможное количество запросов к вызываемому ресурсу
        :rtype: int
        """
        return int(self.headers.get('X-RateLimit-Method-Limit'))

    @property
    def method_remaining(self):
        """

        :return: оставшееся количество запросов к вызываемому ресурсу
        :rtype: int
        """
        return int(self.headers.get('X-RateLimit-Method-Remaining'))

    @property
    def method_until(self):
        """

        :return: время обновления ресурсного посекундного ограничения
        :rtype: str
        """
        return self.headers.get('X-RateLimit-Method-Until')

    @property
    def fields_all_limit(self):
        """

        :return: возможное количество запросов с получением всех полей
        :rtype: int or None
        """
        return int(self.headers.get(
            'X-RateLimit-Fields-All-Limit')) if 'X-RateLimit-Fields-All-Limit' in self.headers else None

    @property
    def fields_all_remaining(self):
        """

        :return: оставшееся количество запросов с получением всех полей
        :rtype: int or None
        """
        return int(self.headers.get(
            'X-RateLimit-Fields-All-Remaining')) if 'X-RateLimit-Fields-All-Remaining' in self.headers else None

    @property
    def fields_all_until(self):
        """

        :return: время обновления ресурсного посекундного ограничения с получением всех полей
        :rtype: str or None
        """
        return self.headers.get('X-RateLimit-Fields-All-Until')

    @property
    def status(self):
        """

        :return: Статус обработки запроса
        :rtype: str
        """
        return self.resp.get('status')

    @property
    def id(self):
        """

        :return: Уникальный идентификатор запроса
        :rtype: str
        """
        return self.resp['context'].get('id')

    @property
    def time(self):
        """

        :return: Дата и время выполнения запроса в формате ISO 8601
        :rtype: str
        """
        return self.resp['context'].get('time')

    @property
    def link(self):
        """

        :return: Ссылка на текущий запрос
        :rtype: str or None
        """
        return self.resp['context'].get('link')

    @property
    def marketUrl(self):
        """

        :return: Ссылка на Яндекс.Маркет
        :rtype: str
        """
        return self.resp['context'].get('marketUrl')

    @property
    def region(self):
        """

        :return: Информация о регионе запроса
        :rtype: YMRegion
        """
        if self.resp['context'].get('region'):
            return YMRegion(self.resp['context'].get('region'))

    @property
    def currency_id(self):
        """

        :return: Код валюты
        :rtype: str
        """
        return self.resp['context']['currency']['id']

    @property
    def currency_name(self):
        """

        :return: Название валюты
        :rtype: str
        """
        return self.resp['context']['currency']['name']

    @property
    def alt_currency_id(self):
        """

        :return: Код валюты
        :rtype: str or None
        """
        if 'alternateCurrency' in self.resp['context']:
            return self.resp['context']['alternateCurrency']['id']

    @property
    def alt_currency_name(self):
        """

        :return: Название валюты
        :rtype: str or None
        """
        if 'alternateCurrency' in self.resp['context']:
            return self.resp['context']['alternateCurrency']['name']


class Page(Base):
    @property
    def page_number(self):
        """

        :return: Номер страницы
        :rtype: int
        """
        return self.resp['context']['page'].get('number')

    @property
    def page_count(self):
        """

        :return: Размер страницы
        :rtype: int
        """
        return int(self.resp['context']['page'].get('count'))

    @property
    def page_total(self):
        """

        :return: Количество страниц в результате
        :rtype: int
        """
        return int(self.resp['context']['page'].get('total'))

    @property
    def page_last(self):
        """

        :return: Признак последней страницы
        :rtype: bool
        """
        return self.resp['context']['page']['number'] == self.resp['context']['page']['total']


class Categories(Page):
    @property
    def categories(self):
        """

        :return: Список категорий
        :rtype: list[YMCategory]
        """
        return [YMCategory(category) for category in self.resp['categories']]


class Category(Base):
    """Категория"""

    @property
    def category(self):
        """

        :return: Категория
        :rtype: YMCategory
        """
        return YMCategory(self.resp['category'])


class Filters(Base):
    """Фильтры"""

    @property
    def sorts(self):
        """

        :return: Список сортировок
        :rtype: list[YMSort]
        """
        return [YMSort(sort) for sort in self.resp['sorts']]

    @property
    def filters(self):
        """

        :return: Список фильтров
        :rtype: list[YMFilter]
        """
        return [YMFilter(f) for f in self.resp['filters']]


class Model(Base):
    """Модель"""

    @property
    def model(self):
        """

        :return: Модель
        :rtype: YMModel
        """
        return YMModel(self.resp['model'])


class ModelReview(Page):
    @property
    def reviews(self):
        """

        :return: Список отзывов на модель
        :rtype: list[YMModelReview]
        """
        return [YMModelReview(review) for review in self.resp['reviews']]


class Models(Base):

    @property
    def models(self):
        """

        :return: Список моделей
        :rtype: list[YMModel]
        """
        return [YMModel(model) for model in self.resp['models']]


class ModelOffers(Page):

    @property
    def sorts(self):
        """

        :return: Список доступных сортировок товарных предложений модели
        :rtype: list[YMSort]
        """
        return [YMSort(sort) for sort in self.resp['sorts']]

    @property
    def filters(self):
        """

        :return: Список фильтров, доступных для фильтрации товарных предложений модели
        :rtype: list[YMFilter]
        """
        return [YMFilter(f) for f in self.resp['filters']]

    @property
    def offers(self):
        """

        :return: Список товарных предложений модели
        :rtype: list[YMOffer]
        """
        return [YMOffer(offer) for offer in self.resp['offers']]


class ModelOffersDefault(Base):

    @property
    def offer(self):
        """

        :return: Товарное предложение
        :rtype: YMOffer
        """
        return YMOffer(self.resp['offer'])


class ModelOffersStat(Base):

    @property
    def statistics(self):
        """

        :return: Информация о количестве и ценах товарных предложений модели по регионам
        :rtype: YMStatistics
        """
        return YMStatistics(self.resp['statistics'])


class Offer(Base):

    @property
    def offer(self):
        """

        :return: Товарное предложение
        :rtype: YMOffer
        """
        return YMOffer(self.resp['offer'])


class ModelOpinions(Page):

    @property
    def opinions(self):
        """

        :return: Отзывы
        :rtype: list[YMModelOpinion]
        """
        return [YMModelOpinion(opinion) for opinion in self.resp['opinions']]


class ShopOpinions(Page):

    @property
    def opinions(self):
        """

        :return: Отзывы
        :rtype: list[YMShopOpinion]
        """
        return [YMShopOpinion(opinion) for opinion in self.resp['opinions']]


class Shop(Base):

    @property
    def shop(self):
        """

        :return: Информация о магазине
        :rtype: YMShop
        """
        return YMShop(self.resp['shop'])


class Shops(Base):

    @property
    def shops(self):
        """

        :return: Информация о магазинах
        :rtype: list[YMShop]
        """
        return [YMShop(shop) for shop in self.resp['shops']]


class ShopsSummary(Base):

    @property
    def homeCount(self):
        """

        :return: Количество магазинов, которые находятся в указанном регионе
        :rtype: int
        """
        return self.resp['summary'].get('homeCount')

    @property
    def deliveryCount(self):
        """

        :return: Количество магазинов, которые осуществляют доставку в указанный регион
        :rtype: int
        """
        return self.resp['summary'].get('deliveryCount')

    @property
    def totalCount(self):
        """

        :return: Общее количество магазинов, которые работают в указанном регионе: находятся в указанном регионе и осуществляют в него доставку
        :rtype: int
        """
        return self.resp['summary'].get('totalCount')


class Outlets(Page):

    @property
    def outlets(self):
        """

        :return: Список торговых точек / пунктов выдачи товара
        :rtype: list[YMOutlet]
        """
        return [YMOutlet(outlet) for outlet in self.resp.get('outlets', [])]


class Regions(Page):

    @property
    def regions(self):
        """

        :return: Список регионов
        :rtype: list[YMRegion]
        """
        return [YMRegion(region) for region in self.resp.get('regions', [])]


class Region(Base):

    @property
    def region(self):
        """

        :return: Регион
        :rtype: YMRegion
        """
        return YMRegion(self.resp.get('region'))


class Suggests(Page):

    @property
    def suggests(self):
        """

        :return: Список регионов в результате поиска по частичному или полному наименованию
        :rtype: list[YMRegion]
        """
        return [YMRegion(region) for region in self.resp.get('suggests', [])]


class Vendors(Page):

    @property
    def vendors(self):
        """

        :return: Список производителей
        :rtype: list[YMVendor]
        """
        return [YMVendor(vendor) for vendor in self.resp.get('vendors', [])]


class Vendor(Base):

    @property
    def vendor(self):
        """

        :return: Производитель
        :rtype: YMVendor
        """
        return YMVendor(self.resp.get('vendor'))


class Search(Page):

    @property
    def items(self):
        """

        :return: Список моделей и/или товарных предложений
        :rtype: list[YMModel or YMOffer]
        """
        return [YMModel(item) if item['__type'] == 'model' else YMOffer(item) for item in self.resp['items']]

    @property
    def categories(self):
        """

        :return: Список категорий
        :rtype: list[YMSearchCategory]
        """
        return [YMSearchCategory(category) for category in self.resp.get('categories', [])]

    @property
    def sorts(self):
        """

        :return: Список доступных сортировок
        :rtype: list[YMSort]
        """
        return [YMSort(sort) for sort in self.resp.get('sorts', [])]


class Redirect(Page):

    @property
    def redirect(self):
        """

        :return: Информация по редиректу
        :rtype: YMRedirectModel or YMRedirectCatalog or YMRedirectVendor or YMRedirectSearch
        """
        if self.resp.get('redirect')['type'] == 'MODEL':
            return YMRedirectModel(self.resp.get('redirect'))
        elif self.resp.get('redirect')['type'] == 'CATALOG':
            return YMRedirectCatalog(self.resp.get('redirect'))
        elif self.resp.get('redirect')['type'] == 'VENDOR':
            return YMRedirectVendor(self.resp.get('redirect'))
        elif self.resp.get('redirect')['type'] == 'SEARCH':
            return YMRedirectSearch(self.resp.get('redirect'))


class Suggestions(Base):

    @property
    def input(self):
        """

        :return: Поисковая подсказка соответствующая введенному тексту
        :rtype: YMSuggestion
        """
        return YMSuggestion(self.resp['suggestions']['input'])

    @property
    def completions(self):
        """

        :return: Поисковые подсказки для завершения фразы
        :rtype: list[YMSuggestionCompletion]
        """
        return [YMSuggestionCompletion(c) for c in self.resp['suggestions']['completions']]

    @property
    def pages(self):
        """

        :return: Поисковые подсказки ведущие на конкретные страницы
        :rtype: list[YMSuggestion]
        """
        return [YMSuggestion(c) for c in self.resp['suggestions']['pages']]
