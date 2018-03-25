# -*- coding: utf-8 -*-
from unittest import TestCase, skip
from YMContent import YMAPI, response, objects
import logging
import logging.config
import inspect
import re
import types
from pydoc import locate
import os

CATEGORIES = ['90402', '90509', '90666', '90722', '90764', '90801', '90813', '91009', '91307', '91512']
MODELS = ['1732210983', '1728227580', '13521091']

api = YMAPI(os.environ['TOKEN'])
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(filename)s:%(lineno)d %(levelname)-8s %(funcName)s %(message)s',
            # 'format': '%(message)s',
            'datefmt': "%H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },

    },
    'loggers': {
        'YMContent': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
}
logging.config.dictConfig(LOGGING)


def rvars_doc(s):
    return [r for r in re.findall('\* \*\*(.*)\*\*', s)]


def getmembers(test_object):
    '''Получение свойств объекта'''
    return [k[0] for k in inspect.getmembers(test_object, lambda x: isinstance(x, property))]


class TestYMAPI(TestCase):

    def insp(self, obj, data):
        logging.debug('INSPECTING object {}\n'.format(obj))
        logging.debug('{}'.format(data.curl()))
        logging.debug('JSON {}\n'.format(data.json()))
        for (k, v) in inspect.getmembers(getattr(response, obj), lambda x: isinstance(x, (property, types.MethodType))):
            doc = inspect.getdoc(v.fget) or ''
            rtype = re.search(':rtype: (.*)', doc).group(1)
            logging.debug('Checking property {}'.format(k))
            if rtype.startswith('list['):
                logging.debug('{} is a list, so checking each element'.format(k))
                self.assertIsInstance(data.__getattribute__(k), list)

                for element in data.__getattribute__(k):
                    self.check_object(element)

            else:
                result = []
                for t in rtype.split(' or '):
                    if t.startswith('list['):
                        result.append(list)
                    elif t == 'None':
                        result.append(type(None))
                    elif t.startswith('YM'):
                        result.append(getattr(objects, t))
                        self.check_object(data.__getattribute__(k))
                    else:
                        result.append(locate(t))

                logging.debug('Value: {}'.format(data.__getattribute__(k)))
                logging.debug('Types should be {} => {}'.format(result, type(data.__getattribute__(k))))
                logging.debug('\n')
                self.assertIsInstance(data.__getattribute__(k), tuple(result))
        # sleep(5)

    def check_object(self, obj):
        if obj.json() is None:
            logging.debug('It is None')
        else:
            logging.debug('It is {}'.format(obj))
            # logging.debug('Checking object {} {}'.format(obj, obj.__class__.__name__))
            logging.debug('JSON: {}'.format(obj.json()))
            test_object = getattr(objects, obj.__class__.__name__)
            self.assertIsInstance(obj, test_object)
            logging.debug('members: {}\n'.format(getmembers(test_object)))
            for p in getmembers(test_object):
                logging.debug('Testing {} => {}'.format(test_object, p))
                s = inspect.getdoc(getattr(test_object, p))
                str_types = re.search(':rtype: (.*)', s).group(1)
                # logging.debug('  Type should be {}'.format(str_types))
                result = []
                for t in str_types.split(' or '):
                    if t.startswith('list['):
                        # logging.debug('    Type is list')
                        result.append(list)
                    elif t == 'None':
                        # logging.debug('    Type is None')
                        result.append(type(None))
                    elif t.startswith('YM'):
                        # logging.debug('    Type is {}'.format(t))
                        # print('+++++', p, t, getattr(objects, t))
                        result.append(getattr(objects, t))
                        # self.check_object(obj.__getattribute__(p))
                    else:
                        result.append(locate(t))
                # logging.debug('    Value: {}'.format(obj.__getattribute__(p)))

                # print('!!!!', str_types, tuple(result))

                # return tuple(result)
                #################

                if obj.__getattribute__(p).__class__.__module__ == 'YMContent.objects':
                    self.check_object(obj.__getattribute__(p))
                else:
                    obj_param = obj.__getattribute__(p)
                    logging.debug('Value: {}'.format(obj_param))
                    if obj_param:
                        obj_doc = inspect.getdoc(getattr(test_object, p))

                        if rvars_doc(obj_doc):
                            logging.debug('Possible values: {}'.format(rvars_doc(obj_doc)))
                            self.assertIn(obj_param, rvars_doc(obj_doc))
                logging.debug(
                    'Possible types: {} => {}: {}\n'.format(str_types, tuple(result), type(obj.__getattribute__(p))))

                self.assertIsInstance(obj.__getattribute__(p), tuple(result))

    def test_categories(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories)).group(1),
                  api.categories(geo_id=213, fields='ALL')
                  )

    def test_categories_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories)).group(1),
                  api.categories(geo_id=213, fields='ALL', page=1)
                  )

    def test_categories_children(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_children)).group(1),
                      api.categories_children(category, geo_id=213, fields='ALL')
                      )

    def test_categories_children_single(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_children)).group(1),
                      api.categories_children(category, geo_id=213, fields='ALL', page=1)
                      )

    def test_category(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.category)).group(1),
                      api.category(category, geo_id=213, fields='ALL')
                      )

    def test_categories_filters(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_filters)).group(1),
                      api.categories_filters(category, geo_id=213, fields='ALL')
                      )

    def test_categories_match(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_match)).group(1),
                  api.categories_match('iphone')
                  )

    def test_model(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model)).group(1),
                      api.model(model, geo_id=213, fields='ALL')
                      )

    def test_models_reviews(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.models_reviews)).group(1),
                      api.models_reviews(model)
                      )

    def test_models_reviews_single(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.models_reviews)).group(1),
                      api.models_reviews(model, page=1)
                      )

    def test_models_match(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.models_match)).group(1),
                  api.models_match('Apple iPhone X', fields='ALL')
                  )

    @skip("testing skipping")
    def test_models_lookas(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.models_lookas)).group(1),
                      api.models_lookas(model, fields='ALL', geo_id=213)
                      )

    def test_models_lookas_single(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.models_lookas)).group(1),
                      api.models_lookas(model, fields='ALL', geo_id=213, page=1)
                      )

    @skip("testing skipping")
    def test_categories_bestdeals(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_bestdeals)).group(1),
                      api.categories_bestdeals(category, fields='ALL', geo_id=213)
                      )

    def test_categories_bestdeals_single(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_bestdeals)).group(1),
                      api.categories_bestdeals(category, fields='ALL', geo_id=213, page=1)
                      )

    @skip("testing skipping")
    def test_categories_popular(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_popular)).group(1),
                      api.categories_popular(category, fields='ALL', geo_id=213)
                      )

    def test_categories_popular_single(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_popular)).group(1),
                      api.categories_popular(category, fields='ALL', geo_id=213, page=1)
                      )

    def test_model_offers(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_offers)).group(1),
                      api.model_offers(model, fields='ALL')
                      )

    def test_model_offers_single(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_offers)).group(1),
                      api.model_offers(model, fields='ALL', page=1)
                      )

    def test_model_offers_default(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_offers_default)).group(1),
                      api.model_offers_default(model, fields='ALL', geo_id=213)
                      )

    def test_model_offers_stat(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_offers_stat)).group(1),
                      api.model_offers_stat(model, geo_id=213)
                      )

    def test_model_offers_filters(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_offers_filters)).group(1),
                      api.model_offers_filters(model, fields='ALL')
                      )

    def test_offer(self):
        for model in MODELS:
            offer_id = api.model_offers(model).offers[0].id
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.offer)).group(1),
                      api.offer(offer_id, geo_id=213)
                      )

    def test_model_opinions(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_opinions)).group(1),
                      api.model_opinions(model)
                      )

    def test_model_opinions_single(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_opinions)).group(1),
                      api.model_opinions(model, page=1)
                      )

    @skip('')
    def test_shop_opinions(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.shop_opinions)).group(1),
                  api.shop_opinions(155)
                  )

    def test_shop_opinions_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.shop_opinions)).group(1),
                  api.shop_opinions(155, page=1)
                  )

    def test_shop(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.shop)).group(1),
                  api.shop(155)
                  )

    def test_shops(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.shops)).group(1),
                  api.shops('ozon.ru', fields='ALL', geo_id=213)
                  )

    def test_geo_regions_shops_summary(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.geo_regions_shops_summary)).group(1),
                  api.geo_regions_shops_summary(213, fields='ALL')
                  )

    @skip("testing skipping")
    def test_model_outlets(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_outlets)).group(1),
                      api.model_outlets(model, fields='ALL', geo_id=213)
                      )

    def test_model_outlets_single(self):
        for model in MODELS:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.model_outlets)).group(1),
                      api.model_outlets(model, fields='ALL', geo_id=213, page=1)
                      )

    def test_shop_outlets(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.shop_outlets)).group(1),
                  api.shop_outlets(155, fields='ALL')
                  )

    def test_shop_outlets_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.shop_outlets)).group(1),
                  api.shop_outlets(155, fields='ALL', page=1)
                  )

    def test_offer_outlets(self):
        for model in MODELS:
            offer_id = api.model_offers(model).offers[0].id
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.offer_outlets)).group(1),
                      api.offer_outlets(offer_id, fields='ALL', geo_id=213)
                      )

    def test_geo_regions(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.geo_regions)).group(1),
                  api.geo_regions(fields='ALL')
                  )

    def test_geo_regions_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.geo_regions)).group(1),
                  api.geo_regions(fields='ALL', page=1)
                  )

    def test_geo_regions_children(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.geo_regions_children)).group(1),
                  api.geo_regions_children(213, fields='ALL')
                  )

    def test_geo_regions_children_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.geo_regions_children)).group(1),
                  api.geo_regions_children(213, fields='ALL', page=1)
                  )

    def test_geo_region(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.geo_region)).group(1),
                  api.geo_region(213, fields='ALL')
                  )

    def test_geo_suggest(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.geo_suggest)).group(1),
                  api.geo_suggest('Москв', fields='ALL')
                  )

    def test_geo_suggest_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.geo_suggest)).group(1),
                  api.geo_suggest('Москв', fields='ALL', page=1)
                  )

    def test_vendors(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.vendors)).group(1),
                  api.vendors(fields='ALL')
                  )

    def test_vendors_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.vendors)).group(1),
                  api.vendors(fields='ALL', page=1)
                  )

    def test_vendor(self):
        vendor_id = api.vendors().vendors[0].id
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.vendor)).group(1),
                  api.vendor(vendor_id, fields='ALL')
                  )

    def test_vendors_match(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.vendors_match)).group(1),
                  api.vendors_match('Apple', fields='ALL')
                  )

    def test_search(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.search)).group(1),
                  api.search('Apple', fields='ALL', geo_id=213)
                  )
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.search)).group(1),
                  api.search('Samsung', fields='ALL', geo_id=213)
                  )

    def test_search_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.search)).group(1),
                  api.search('Apple', fields='ALL', geo_id=213, page=1)
                  )
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.search)).group(1),
                  api.search('Samsung', fields='ALL', geo_id=213, page=1)
                  )

    @skip("testing skipping")
    def test_categories_search(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_search)).group(1),
                      api.categories_search(category, fields='ALL', geo_id=213)
                      )

    def test_categories_search_single(self):
        for category in CATEGORIES:
            self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.categories_search)).group(1),
                      api.categories_search(category, fields='ALL', geo_id=213, page=1)
                      )

    def test_search_filters(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.search_filters)).group(1),
                  api.search_filters('phone', fields='ALL', geo_id=213)
                  )

    def test_redirect(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.redirect)).group(1),
                  api.redirect('phone', fields='ALL', geo_id=213)
                  )

    def test_redirect_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.redirect)).group(1),
                  api.redirect('phone', fields='ALL', geo_id=213, page=1)
                  )

    def test_suggestions(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.suggestions)).group(1),
                  api.suggestions('iphone', geo_id=213)
                  )

    def test_suggestions_single(self):
        self.insp(re.search(':rtype: (.*)', inspect.getdoc(YMAPI.suggestions)).group(1),
                  api.suggestions('iphone', geo_id=213, page=1)
                  )

    # def test_everything(self):
    #     for (k, v) in inspect.getmembers(YMAPI):
    #         print(k,v)
    #         # for i in re.findall(':rtype: (.*)', inspect.getdoc(v) or ''):
    #         #     print('METHOD {}'.format(k))
    #         #     insp(i)
