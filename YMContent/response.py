# -*- coding: utf-8 -*-
from .objects import *


class Base(object):

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
        """HTTP статус обработки запроса"""
        return self.req.status_code

    @property
    def status(self):
        """Статус обработки запроса"""
        return self.resp.get('status')

    @property
    def id(self):
        """Уникальный идентификатор запроса"""
        return self.resp['context'].get('id')

    @property
    def time(self):
        """Дата и время выполнения запроса в формате ISO 8601"""
        return self.resp['context'].get('time')

    @property
    def link(self):
        """Ссылка на текущий запрос"""
        return self.resp['context'].get('link')

    @property
    def marketUrl(self):
        """Ссылка на Яндекс.Маркет"""
        return self.resp['context'].get('marketUrl')

    @property
    def region(self):
        """Информация о регионе запроса"""
        if self.resp['context'].get('region'):
            return YMRegion(self.resp['context'].get('region'))

    @property
    def currency_id(self):
        """Код валюты"""
        return self.resp['context']['currency']['id']

    @property
    def currency_name(self):
        """Название валюты"""
        return self.resp['context']['currency']['name']


class Page(Base):
    @property
    def page_number(self):
        return self.resp['context']['page'].get('number')

    @property
    def page_count(self):
        return self.resp['context']['page'].get('count')

    @property
    def page_total(self):
        return self.resp['context']['page'].get('total')

    @property
    def page_last(self):
        return self.resp['context']['page']['number'] == self.resp['context']['page']['total']
        # return self.resp['context']['page']['last']


class Categories(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def categories(self):
        return [YMCategory(category) for category in self.resp['categories']]


class CategoriesChildren(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def categories(self):
        return [YMCategory(category) for category in self.resp['categories']]


class Category(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def category(self):
        return YMCategory(self.resp['category'])


class CategoriesFilters(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def sorts(self):
        return [YMSort(sort) for sort in self.resp['sorts']]

    @property
    def filters(self):
        return [YMFilter(filter) for filter in self.resp['filters']]


class Model(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def model(self):
        return YMModel(self.resp['model'])


class ModelReview(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def reviews(self):
        return [YMModelReview(review) for review in self.resp['reviews']]


class Models(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def models(self):
        return [YMModel(model) for model in self.resp['models']]


class ModelsLookas(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def models(self):
        return [YMModel(model) for model in self.resp['models']]


class CategoriesLookas(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def models(self):
        return [YMModel(model) for model in self.resp['models']]


class CategoriesPopular(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def models(self):
        return [YMModel(model) for model in self.resp['models']]


class ModelOffers(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def sorts(self):
        return [YMSort(sort) for sort in self.resp['sorts']]

    @property
    def filters(self):
        return [YMFilter(filter) for filter in self.resp['filters']]

    @property
    def offers(self):
        return [YMOffer(offer) for offer in self.resp['offers']]


class ModelOffersDefault(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def offer(self):
        return YMOffer(self.resp['offers'])


class ModelOffersStat(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def statistics(self):
        return YMStatistics(self.resp['statistics'])


class ModelOffersFilters(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def sorts(self):
        return [YMSort(sort) for sort in self.resp['sorts']]

    @property
    def filters(self):
        return [YMFilter(filter) for filter in self.resp['filters']]


class Offers(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def offer(self):
        return YMOffer(self.resp['offer'])


class ModelOpinions(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def opinions(self):
        return [YMModelOpinion(opinion) for opinion in self.resp['opinions']]


class ShopOpinions(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def opinions(self):
        return [YMShopOpinion(opinion) for opinion in self.resp['opinions']]


class Shop(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def shop(self):
        return YMShop(self.resp['shop'])


class Shops(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def shops(self):
        return [YMShop(shop) for shop in self.resp['shops']]


class ShopsSummary(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

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
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def outlets(self):
        return [YMOutlet(outlet) for outlet in self.resp.get('outlets')]


class Regions(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def regions(self):
        return [YMRegion(region) for region in self.resp.get('regions')]


class Region(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def region(self):
        return YMRegion(self.resp.get('region'))


class Suggests(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def suggests(self):
        return [YMRegion(region) for region in self.resp.get('suggests')]


class Vendors(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def vendors(self):
        return [YMVendor(vendor) for vendor in self.resp.get('vendors')]


class Vendor(Base):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

    @property
    def vendor(self):
        return YMVendor(self.resp.get('vendor'))


class Search(Page):
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

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
    def __init__(self, r):
        self.req = r
        self.resp = r.json()

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
        # return YMRedirect(self.resp['redirect'])
