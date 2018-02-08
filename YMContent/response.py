# -*- coding: utf-8 -*-
from .objects import *


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
        return self.headers.get('X-RateLimit-Daily-Limit')

    @property
    def daily_remaining(self):
        """

        :return: оставшееся количество запросов до превышения суточного ограничения
        :rtype: int
        """
        return self.headers.get('X-RateLimit-Daily-Remaining')

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
        return self.headers.get('X-RateLimit-Global-Limit')

    @property
    def global_remaining(self):
        """

        :return: оставшееся количество запросов в определенный промежуток времени до превышения глобального ограничения
        :rtype: int
        """
        return self.headers.get('X-RateLimit-Global-Remaining')

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
        return self.headers.get('X-RateLimit-Method-Limit')

    @property
    def method_remaining(self):
        """

        :return: оставшееся количество запросов к вызываемому ресурсу
        :rtype: int
        """
        return self.headers.get('X-RateLimit-Method-Remaining')

    @property
    def method_until(self):
        """

        :return: время обновления ресурсного посекундного ограничения
        :rtype: date
        """
        return self.headers.get('X-RateLimit-Method-Until')

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
        :rtype: str
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
        :rtype: object
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
        :rtype: str
        """
        return self.resp['context']['alternateCurrency']['id']

    @property
    def alt_currency_name(self):
        """

        :return: Название валюты
        :rtype: str
        """
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
        return self.resp['context']['page'].get('count')

    @property
    def page_total(self):
        """

        :return: Количество страниц в результате
        :rtype: int
        """
        return self.resp['context']['page'].get('total')

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
        :rtype: list[objects.YMCategory]
        """
        return [YMCategory(category) for category in self.resp['categories']]


class Category(Base):
    """Категория"""
    @property
    def category(self):
        """

        :return: Категория
        :rtype: objects.YMCategory
        """
        return YMCategory(self.resp['category'])


class Filters(Base):
    """Фильтры"""
    @property
    def sorts(self):
        """

        :return: Список сортировок
        :rtype: list[objects.YMSort]
        """
        return [YMSort(sort) for sort in self.resp['sorts']]

    @property
    def filters(self):
        """

        :return: Список фильтров
        :rtype: list[objects.YMFilter]
        """
        return [YMFilter(f) for f in self.resp['filters']]


class Model(Base):
    """Модель"""
    @property
    def model(self):
        """

        :return: Модель
        :rtype: objects.YMModel
        """
        return YMModel(self.resp['model'])


class ModelReview(Page):
    """

    :return: Список отзывов на модель
    :rtype: list[YMModelReview]
    """

    @property
    def reviews(self):
        return [YMModelReview(review) for review in self.resp['reviews']]


class Models(Base):

    @property
    def models(self):
        """

        :return: Список моделей
        :rtype: list[objects.YMModel]
        """
        return [YMModel(model) for model in self.resp['models']]


class CategoriesLookas(Page):

    @property
    def models(self):
        """

        :return: Список моделей товаров c самыми большими скидками на сегодняшний день для указанной категории
        :rtype: list[objects.YMModel]
        """
        return [YMModel(model) for model in self.resp['models']]


class ModelOffers(Page):

    @property
    def sorts(self):
        """

        :return: Список доступных сортировок товарных предложений модели
        :rtype: list[objects.YMSort]
        """
        return [YMSort(sort) for sort in self.resp['sorts']]

    @property
    def filters(self):
        """

        :return: Список фильтров, доступных для фильтрации товарных предложений модели
        :rtype: list[objects.YMFilter]
        """
        return [YMFilter(f) for f in self.resp['filters']]

    @property
    def offers(self):
        """

        :return: Список товарных предложений модели
        :rtype: list[objects.YMOffer]
        """
        return [YMOffer(offer) for offer in self.resp['offers']]


class ModelOffersDefault(Base):

    @property
    def offer(self):
        """

        :return: Товарное предложение
        :rtype: objects.YMOffer
        """
        return YMOffer(self.resp['offers'])


class ModelOffersStat(Base):

    @property
    def statistics(self):
        """

        :return: Информация о количестве и ценах товарных предложений модели по регионам
        :rtype: objects.YMStatistics
        """
        return YMStatistics(self.resp['statistics'])


class Offer(Base):

    @property
    def offer(self):
        """

        :return: Товарное предложение
        :rtype: objects.YMOffer
        """
        return YMOffer(self.resp['offer'])


class ModelOpinions(Page):

    @property
    def opinions(self):
        """

        :return: Отзывы
        :rtype: list[objects.YMModelOpinion]
        """
        return [YMModelOpinion(opinion) for opinion in self.resp['opinions']]


class ShopOpinions(Page):

    @property
    def opinions(self):
        """

        :return: Отзывы
        :rtype: list[objects.YMShopOpinion]
        """
        return [YMShopOpinion(opinion) for opinion in self.resp['opinions']]


class Shop(Page):

    @property
    def shop(self):
        """

        :return: Информация о магазине
        :rtype: objects.YMShop
        """
        return YMShop(self.resp['shop'])


class Shops(Page):

    @property
    def shops(self):
        """

        :return: Информация о магазинах
        :rtype: list[objects.YMShop]
        """
        return [YMShop(shop) for shop in self.resp['shops']]


class ShopsSummary(Page):

    @property
    def homeCount(self):
        """

        :return: Количество магазинов, которые находятся в указанном регионе
        :rtype: int
        """
        return self.resp.get('homeCount')

    @property
    def deliveryCount(self):
        """

        :return: Количество магазинов, которые осуществляют доставку в указанный регион
        :rtype: int
        """
        return self.resp.get('deliveryCount')

    @property
    def totalCount(self):
        """

        :return: Общее количество магазинов, которые работают в указанном регионе: находятся в указанном регионе и осуществляют в него доставку
        :rtype: int
        """
        return self.resp.get('totalCount')


class Outlets(Page):

    @property
    def outlets(self):
        """

        :return: Список торговых точек / пунктов выдачи товара
        :rtype: list[objects.YMOutlet]
        """
        return [YMOutlet(outlet) for outlet in self.resp.get('outlets', [])]


class Regions(Page):

    @property
    def regions(self):
        """

        :return: Список регионов
        :rtype: list[objects.YMRegion]
        """
        return [YMRegion(region) for region in self.resp.get('regions', [])]


class Region(Base):

    @property
    def region(self):
        """

        :return: Регион
        :rtype: objects.YMRegion
        """
        return YMRegion(self.resp.get('region'))


class Suggests(Page):

    @property
    def suggests(self):
        """

        :return: Список регионов в результате поиска по частичному или полному наименованию
        :rtype: list[objects.YMRegion]
        """
        return [YMRegion(region) for region in self.resp.get('suggests', [])]


class Vendors(Page):

    @property
    def vendors(self):
        """

        :return: Список производителей
        :rtype: list[objects.YMVendor]
        """
        return [YMVendor(vendor) for vendor in self.resp.get('vendors', [])]


class Vendor(Base):

    @property
    def vendor(self):
        """

        :return: Производитель
        :rtype: objects.YMVendor
        """
        return YMVendor(self.resp.get('vendor'))


class Search(Page):

    @property
    def items(self):
        """

        :return: Список моделей и/или товарных предложений
        :rtype: list[objects.YMModel or objects.YMOffer]
        """
        return [YMModel(item) if 'model' in item.keys() else YMOffer(item) for item in self.resp['items']]

    @property
    def categories(self):
        """

        :return: Список категорий
        :rtype: list[objects.YMSearchCategory]
        """
        return [YMSearchCategory(category) for category in self.resp['categories']]

    @property
    def sorts(self):
        """

        :return: Список доступных сортировок
        :rtype: list[objects.YMSort]
        """
        return [YMSort(sort) for sort in self.resp['sorts']]


class Redirect(Page):

    @property
    def redirect(self):
        """

        :return: Информация по редиректу
        :rtype: objects.YMRedirectModel or objects.YMRedirectCatalog or objects.YMRedirectVendor or objects.YMRedirectSearch
        """
        if self.resp.get('redirect')['type'] == 'MODEL':
            return YMRedirectModel(self.resp.get('redirect'))
        elif self.resp.get('redirect')['type'] == 'CATALOG':
            return YMRedirectCatalog(self.resp.get('redirect'))
        elif self.resp.get('redirect')['type'] == 'VENDOR':
            return YMRedirectVendor(self.resp.get('redirect'))
        elif self.resp.get('redirect')['type'] == 'SEARCH':
            return YMRedirectSearch(self.resp.get('redirect'))


class Suggestions(Page):

    @property
    def input(self):
        """

        :return: Поисковая подсказка соответствующая введенному тексту
        :rtype: objects.YMSuggestion
        """
        return YMSuggestion(self.resp['suggestions']['input'])

    @property
    def completions(self):
        """

        :return: Поисковые подсказки для завершения фразы
        :rtype: list[objects.YMSuggestionCompletion]
        """
        return [YMSuggestionCompletion(c) for c in self.resp['suggestions']['completions']]

    @property
    def pages(self):
        """

        :return: Поисковые подсказки ведущие на конкретные страницы
        :rtype: list[objects.YMSuggestion]
        """
        return [YMSuggestion(c) for c in self.resp['suggestions']['pages']]
