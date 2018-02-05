# -*- coding: utf-8 -*-
from .objects import *


class Base(object):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    def json(self):
        return self.resp

    def curl(self):
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
        return self.resp.get('status') == 'OK'

    @property
    def http_status_code(self):
        """

        :return: HTTP статус обработки запроса
        :rtype: int
        """
        return self.req.status_code

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


class CategoriesChildren(Page):
    @property
    def categories(self):
        """

        :return: Список подкатегорий
        :rtype: list[objects.YMCategory]
        """
        return [YMCategory(category) for category in self.resp['categories']]


class Category(Base):
    @property
    def category(self):
        """

        :return: Категория
        :rtype: objects.YMCategory
        """
        return YMCategory(self.resp['category'])


class CategoriesFilters(Base):

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
        return [YMFilter(filter) for filter in self.resp['filters']]


class Model(Base):

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


class ModelsLookas(Base):

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


class CategoriesPopular(Page):

    @property
    def models(self):
        """

        :return: Список моделей
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
        return [YMFilter(filter) for filter in self.resp['filters']]

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


class ModelOffersFilters(Base):

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
        return [YMFilter(filter) for filter in self.resp['filters']]


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
        return [YMShopOpinion(opinion) for opinion in self.resp['opinions']]


class Shop(Page):

    @property
    def shop(self):
        return YMShop(self.resp['shop'])


class Shops(Page):

    @property
    def shops(self):
        return [YMShop(shop) for shop in self.resp['shops']]


class ShopsSummary(Page):

    @property
    def homeCount(self):
        return self.resp.get('homeCount')

    @property
    def deliveryCount(self):
        return self.resp.get('deliveryCount')

    @property
    def totalCount(self):
        return self.resp.get('totalCount')


class Outlets(Page):

    @property
    def outlets(self):
        return [YMOutlet(outlet) for outlet in self.resp.get('outlets', [])]


class Regions(Page):

    @property
    def regions(self):
        return [YMRegion(region) for region in self.resp.get('regions', [])]


class Region(Base):

    @property
    def region(self):
        return YMRegion(self.resp.get('region'))


class Suggests(Page):

    @property
    def suggests(self):
        return [YMRegion(region) for region in self.resp.get('suggests', [])]


class Vendors(Page):

    @property
    def vendors(self):
        return [YMVendor(vendor) for vendor in self.resp.get('vendors', [])]


class Vendor(Base):

    @property
    def vendor(self):
        return YMVendor(self.resp.get('vendor'))


class Search(Page):

    @property
    def items(self):
        return [YMModel(item) if 'model' in item.keys() else YMOffer(item) for item in self.resp['items']]

    @property
    def categories(self):
        return [YMSearchCategory(category) for category in self.resp['categories']]

    @property
    def sorts(self):
        return [YMSort(sort) for sort in self.resp['sorts']]


class Redirect(Page):

    @property
    def redirect(self):
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
        return YMSuggestion(self.resp['input'])

    @property
    def completions(self):
        return [YMSuggestionCompletion(c) for c in self.resp['completions']]

    @property
    def pages(self):
        return [YMSuggestion(c) for c in self.resp['pages']]
