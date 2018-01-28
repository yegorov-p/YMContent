# -*- coding: utf-8 -*-
import json


class YMBase(object):
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data


class YMRegion(YMBase):
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data

    def __repr__(self):
        return '<{}: {} ({})>'.format(self.__class__.__name__, self.data.get('name'), self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def type(self):
        return self.data.get('type')

    @property
    def childCount(self):
        return self.data.get('childCount')

    @property
    def nameAccusative(self):
        return self.data.get('nameAccusative')

    @property
    def nameGenitive(self):
        return self.data.get('nameGenitive')

    @property
    def country(self):
        return YMRegion(self.data.get('country'))

    @property
    def parent(self):
        return YMRegion(self.data.get('parent'))


class YMWarning(YMBase):
    """Категория"""

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('shortText'))

    @property
    def text(self):
        return self.data.get('text')

    @property
    def shortText(self):
        return self.data.get('shortText')

    @property
    def age(self):
        return self.data.get('age')


class YMCategory(YMBase):
    """Категория"""

    def __repr__(self):
        return '<{}: {} ({})>'.format(self.__class__.__name__, self.data.get('name'), self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def fullName(self):
        return self.data.get('fullName')

    @property
    def parent(self):
        return self.data.get('parent')

    @property
    def adult(self):
        return self.data.get('adult')

    @property
    def link(self):
        return self.data.get('link')

    @property
    def childCount(self):
        return self.data.get('childCount')

    @property
    def modelCount(self):
        return self.data.get('modelCount')

    @property
    def offerCount(self):
        return self.data.get('offerCount')

    @property
    def advertisingModel(self):
        return self.data.get('advertisingModel')

    @property
    def viewType(self):
        return self.data.get('viewType')

    @property
    def warnings(self):
        return [YMWarning(warning) for warning in self.data.get('warnings')]


class YMSortOption(YMBase):

    def __repr__(self):
        return '<{}: {} ({})>'.format(self.__class__.__name__, self.data.get('id'), self.data.get('how'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def how(self):
        return self.data.get('how')

    @property
    def text(self):
        return self.data.get('text')


class YMSort(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('text'))

    @property
    def text(self):
        return self.data.get('text')

    @property
    def field(self):
        return self.data.get('field')

    @property
    def options(self):
        return [YMSortOption(option) for option in self.data.get('options')]


class YMFilterValue(YMBase):

    def __repr__(self):
        return '<{}: {} ({})>'.format(self.__class__.__name__, self.data.get('id'), self.data.get('name'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def initialFound(self):
        return self.data.get('initialFound')

    @property
    def found(self):
        return self.data.get('found')

    @property
    def checked(self):
        return self.data.get('checked')

    @property
    def color(self):
        return self.data.get('color')

    @property
    def unitId(self):
        return self.data.get('unitId')

    @property
    def id(self):
        return self.data.get('id')


class YMDatasourceOrder(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('sort'))

    @property
    def sort(self):
        return self.data.get('sort')

    @property
    def how(self):
        return self.data.get('how')


class YMDatasourceCriteria(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def value(self):
        return self.data.get('value')

    @property
    def text(self):
        return self.data.get('text')


class YMIcon(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('url'))

    @property
    def url(self):
        return self.data.get('url')


class YMDatasource(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def hid(self):
        return self.data.get('hid')

    @property
    def nid(self):
        return self.data.get('nid')

    @property
    def order(self):
        return YMDatasourceOrder(self.data.get('order'))

    @property
    def criteria(self):
        return YMDatasourceCriteria(self.data.get('criteria'))


class YMNavigationNode(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def hid(self):
        return self.data.get('hid')

    @property
    def shortName(self):
        return self.data.get('shortName')

    @property
    def type(self):
        return self.data.get('type')

    @property
    def offerCount(self):
        return self.data.get('offerCount')

    @property
    def modelCount(self):
        return self.data.get('modelCount')

    @property
    def visual(self):
        return self.data.get('visual')

    @property
    def maxDiscount(self):
        return self.data.get('maxDiscount')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def datasource(self):
        return self.data.get('datasource')

    @property
    def icons(self):
        return [YMIcon(icon) for icon in self.data.get('icons')]

    @property
    def parents(self):
        return self.data.get('parents')

    @property
    def categories(self):
        return self.data.get('categories')


class YMFilter(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def type(self):
        return self.data.get('type')

    @property
    def description(self):
        return self.data.get('description')

    @property
    def unit(self):
        return self.data.get('unit')

    @property
    def defaultUnit(self):
        return self.data.get('defaultUnit')

    @property
    def values(self):
        return [YMFilterValue(value) for value in self.data.get('values', [])]

    @property
    def max(self):
        return self.data.get('max')

    @property
    def min(self):
        return self.data.get('min')

    @property
    def value(self):
        return self.data.get('value')

    @property
    def precision(self):
        return self.data.get('precision')


class YMModelPhoto(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('url'))

    @property
    def width(self):
        return self.data.get('width')

    @property
    def height(self):
        return self.data.get('height')

    @property
    def url(self):
        return self.data.get('url')

    @property
    def colorId(self):
        return self.data.get('colorId')


class YMPrice(YMBase):

    def __repr__(self):
        return '<{}'.format(self.__class__.__name__)

    @property
    def max(self):
        return self.data.get('max')

    @property
    def min(self):
        return self.data.get('min')

    @property
    def avg(self):
        return self.data.get('avg')

    @property
    def discount(self):
        return self.data.get('discount')

    @property
    def base(self):
        return self.data.get('base')


class YMShopPrice(YMBase):

    def __repr__(self):
        return '<{}'.format(self.__class__.__name__)

    @property
    def value(self):
        return self.data.get('value')

    @property
    def discount(self):
        return self.data.get('discount')

    @property
    def base(self):
        return self.data.get('base')

    @property
    def shopMin(self):
        return self.data.get('shopMin')

    @property
    def shopMax(self):
        return self.data.get('shopMax')


class YMVendor(object):
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')


class YMVendorCategory(YMCategory):

    @property
    def popularity(self):
        return self.data.get('popularity')

    @property
    def children(self):
        return [YMVendorCategory(category) for category in self.data.get('children')]


class YMVendor(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def site(self):
        return self.data.get('site')

    @property
    def picture(self):
        return self.data.get('picture')

    @property
    def recommendedShops(self):
        return self.data.get('recommendedShops')

    @property
    def link(self):
        return self.data.get('link')

    @property
    def categories(self):
        return [YMVendorCategory(category) for category in self.data.get('categories')]

    @property
    def topCategories(self):
        return [YMVendorCategory(category) for category in self.data.get('topCategories')]


class YMRatingDistribution(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def value(self):
        return self.data.get('value')

    @property
    def count(self):
        return self.data.get('count')

    @property
    def percent(self):
        return self.data.get('percent')


class YMRating(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def value(self):
        return self.data.get('value')

    @property
    def count(self):
        return self.data.get('count')

    @property
    def distribution(self):
        return YMRatingDistribution(self.data.get('distribution'))


class YMFacts(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def pro(self):
        return self.data.get('pro')

    @property
    def contra(self):
        return self.data.get('contra')


class YMModelWarning(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('code'))

    @property
    def code(self):
        return self.data.get('code')

    @property
    def message(self):
        return self.data.get('message')


class YMModification(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def description(self):
        return self.data.get('description')

    @property
    def popularity(self):
        return self.data.get('popularity')

    @property
    def offerCount(self):
        return self.data.get('offerCount')

    @property
    def shopCount(self):
        return self.data.get('shopCount')

    @property
    def price(self):
        return YMPrice(self.data.get('price'))

    @property
    def alternatePrices(self):
        return YMPrice(self.data.get('alternatePrices'))


class YMSpecificationFeature(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('name'))

    @property
    def name(self):
        return self.data.get('name')

    @property
    def value(self):
        return self.data.get('value')


class YMSpecification(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('name'))

    @property
    def name(self):
        return self.data.get('name')

    @property
    def features(self):
        return [YMSpecificationFeature(feature) for feature in self.data.get('features')]


class YMParameterOption(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')


class YMParameter(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('type'))

    @property
    def type(self):
        return self.data.get('type')

    @property
    def parameterId(self):
        return self.data.get('parameterId')

    @property
    def multivalue(self):
        return self.data.get('multivalue')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def unit(self):
        return self.data.get('unit')

    @property
    def mandatory(self):
        return self.data.get('mandatory')

    @property
    def values(self):
        return self.data.get('values')

    @property
    def options(self):
        return [YMParameterOption(parameter) for parameter in self.data.get('options')]


class YMUserRelated(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def inComparisonList(self):
        return self.data.get('inComparisonList')

    @property
    def inWishlist(self):
        return self.data.get('inWishlist')


class YMModel(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def kind(self):
        return self.data.get('kind')

    @property
    def type(self):
        return self.data.get('type')

    @property
    def isNew(self):
        return self.data.get('isNew')

    @property
    def link(self):
        return self.data.get('link')

    @property
    def vendorLink(self):
        return self.data.get('vendorLink')

    @property
    def barcode(self):
        return self.data.get('barcode')

    @property
    def vendorCode(self):
        return self.data.get('vendorCode')

    @property
    def offerCount(self):
        return self.data.get('offerCount')

    @property
    def opinionCount(self):
        return self.data.get('opinionCount')

    @property
    def reviewCount(self):
        return self.data.get('reviewCount')

    @property
    def modificationCount(self):
        return self.data.get('modificationCount')

    @property
    def lastUpdate(self):
        return self.data.get('lastUpdate')

    @property
    def aliases(self):
        return self.data.get('aliases')

    @property
    def parent(self):
        return self.data.get('parent')

    @property
    def description(self):
        return self.data.get('description')

    @property
    def photo(self):
        return YMModelPhoto(self.data.get('photo'))

    @property
    def photos(self):
        return [YMModelPhoto(photo) for photo in self.data.get('photos')]

    @property
    def category(self):
        return YMCategory(self.data.get('category'))

    @property
    def navigationNode(self):
        return YMNavigationNode(self.data.get('navigationNode'))

    @property
    def price(self):
        return YMPrice(self.data.get('price'))

    @property
    def vendor(self):
        return YMVendor(self.data.get('vendor'))

    @property
    def rating(self):
        return YMRating(self.data.get('rating'))

    @property
    def facts(self):
        return YMFacts(self.data.get('facts'))

    @property
    def warning(self):
        return self.data.get('warning')

    @property
    def warnings(self):
        return [YMModelWarning(warning) for warning in self.data.get('warnings')]

    @property
    def filters(self):
        return [YMFilter(filter) for filter in self.data.get('filters')]

    @property
    def modifications(self):
        return [YMModification(modification) for modification in self.data.get('modifications')]

    @property
    def specification(self):
        return [YMSpecification(specification) for specification in self.data.get('specification')]

    @property
    def parameters(self):
        return [YMParameter(parameter) for parameter in self.data.get('parameters')]

    @property
    def userRelated(self):
        return YMUserRelated(self.data.get('userRelated'))


class YMModelReview(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def url(self):
        return self.data.get('url')

    @property
    def title(self):
        return self.data.get('title')

    @property
    def favIcon(self):
        return self.data.get('favIcon')


class YMOrganization(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('name'))

    @property
    def name(self):
        return self.data.get('name')

    @property
    def ogrn(self):
        return self.data.get('ogrn')

    @property
    def address(self):
        return self.data.get('address')

    @property
    def postalAddress(self):
        return self.data.get('postalAddress')

    @property
    def type(self):
        return self.data.get('type')

    @property
    def contactUrl(self):
        return self.data.get('contactUrl')


class YMShop(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def domain(self):
        return self.data.get('domain')

    @property
    def registered(self):
        return self.data.get('registered')

    @property
    def opinionUrl(self):
        return self.data.get('opinionUrl')

    @property
    def region(self):
        return YMRegion(self.data.get('region'))

    @property
    def rating(self):
        return YMRating(self.data.get('rating'))

    @property
    def organizations(self):
        return [YMOrganization(organization) for organization in self.data.get('organizations')]


class YMPhone(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('number'))

    @property
    def number(self):
        return self.data.get('number')

    @property
    def sanitized(self):
        return self.data.get('sanitized')

    @property
    def call(self):
        return self.data.get('call')


class YMDeliveryOptionService(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')


class YMDeliveryOptionConditions(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def price(self):
        return YMShopPrice(self.data.get('price'))

    @property
    def alternatePrice(self):
        return YMShopPrice(self.data.get('alternatePrice'))

    @property
    def daysFrom(self):
        return self.data.get('daysFrom')

    @property
    def daysTo(self):
        return self.data.get('daysTo')

    @property
    def orderBefore(self):
        return self.data.get('orderBefore')

    @property
    def deliveryIncluded(self):
        return self.data.get('deliveryIncluded')


class YMDeliveryOption(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def brief(self):
        return self.data.get('brief')

    @property
    def service(self):
        return YMDeliveryOptionService(self.data.get('service'))

    @property
    def conditions(self):
        return YMDeliveryOptionConditions(self.data.get('conditions'))


class YMDeliveryPickupOption(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def brief(self):
        return self.data.get('brief')

    @property
    def outletCount(self):
        return self.data.get('outletCount')

    @property
    def service(self):
        return YMDeliveryOptionService(self.data.get('service'))

    @property
    def conditions(self):
        return YMDeliveryOptionConditions(self.data.get('conditions'))


class YMDelivery(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def free(self):
        return self.data.get('free')

    @property
    def deliveryIncluded(self):
        return self.data.get('deliveryIncluded')

    @property
    def carried(self):
        return self.data.get('carried')

    @property
    def pickup(self):
        return self.data.get('pickup')

    @property
    def downloadable(self):
        return self.data.get('downloadable')

    @property
    def localStore(self):
        return self.data.get('localStore')

    @property
    def localDelivery(self):
        return self.data.get('localDelivery')

    @property
    def brief(self):
        return self.data.get('brief')

    @property
    def inStock(self):
        return self.data.get('inStock')

    @property
    def is_global(self):
        return self.data.get('global')

    @property
    def price(self):
        return YMShopPrice(self.data.get('price'))

    @property
    def alternatePrice(self):
        return YMShopPrice(self.data.get('alternatePrice'))

    @property
    def shopRegion(self):
        return YMRegion(self.data.get('shopRegion'))

    @property
    def userRegion(self):
        return YMRegion(self.data.get('userRegion'))

    @property
    def description(self):
        return self.data.get('description')

    @property
    def options(self):
        return [YMDeliveryOption(option) for option in self.data.get('options')]

    @property
    def pickupOptions(self):
        return [YMDeliveryPickupOption(option) for option in self.data.get('pickupOptions')]


class YMPaymentOption(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def canPayByCard(self):
        return self.data.get('canPayByCard')


class YMOffer(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def wareMd5(self):
        return self.data.get('wareMd5')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def promocode(self):
        return self.data.get('promocode')

    @property
    def cpa(self):
        return self.data.get('cpa')

    @property
    def url(self):
        return self.data.get('url')

    @property
    def cpaUrl(self):
        return self.data.get('cpaUrl')

    @property
    def outletUrl(self):
        return self.data.get('outletUrl')

    @property
    def adult(self):
        return self.data.get('adult')

    @property
    def age(self):
        return self.data.get('age')

    @property
    def onStock(self):
        return self.data.get('onStock')

    @property
    def outletCount(self):
        return self.data.get('outletCount')

    @property
    def pickupCount(self):
        return self.data.get('pickupCount')

    @property
    def localStoreCount(self):
        return self.data.get('localStoreCount')

    @property
    def warranty(self):
        return self.data.get('warranty')

    @property
    def recommended(self):
        return self.data.get('recommended')

    @property
    def link(self):
        return self.data.get('link')

    @property
    def cartLink(self):
        return self.data.get('cartLink')

    @property
    def offersLink(self):
        return self.data.get('offersLink')

    @property
    def variationCount(self):
        return self.data.get('variationCount')

    @property
    def description(self):
        return self.data.get('description')

    @property
    def price(self):
        return YMShopPrice(self.data.get('price'))

    @property
    def alternatePrice(self):
        return YMShopPrice(self.data.get('alternatePrice'))

    @property
    def shop(self):
        return YMShop(self.data.get('shop'))

    @property
    def model(self):
        return YMModel(self.data.get('model'))

    @property
    def phone(self):
        return YMPhone(self.data.get('phone'))

    @property
    def photos(self):
        return [YMModelPhoto(photo) for photo in self.data.get('photos')]

    @property
    def photo(self):
        return YMModelPhoto(self.data.get('photo'))

    @property
    def previewPhotos(self):
        return [YMModelPhoto(photo) for photo in self.data.get('previewPhotos')]

    @property
    def activeFilters(self):
        return [YMFilter(filter) for filter in self.data.get('activeFilters')]

    @property
    def delivery(self):
        return YMDelivery(self.data.get('delivery'))

    @property
    def category(self):
        return YMCategory(self.data.get('category'))

    @property
    def vendor(self):
        return YMVendor(self.data.get('vendor'))

    @property
    def warning(self):
        return self.data.get('warning')

    @property
    def warnings(self):
        return YMModelWarning(self.data.get('warnings'))

    @property
    def paymentOptions(self):
        return YMPaymentOption(self.data.get('paymentOptions'))


class YMStatisticsRegion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        return self.data.get('id')

    @property
    def offerCount(self):
        return self.data.get('offerCount')

    @property
    def price_max(self):
        return self.data.get('price_max')

    @property
    def price_min(self):
        return self.data.get('price_min')

    @property
    def price_median(self):
        return self.data.get('price_median')


class YMStatistics(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def regions(self):
        return [YMStatisticsRegion(region) for region in self.data.get('regions')]


class YMOpinionAuthorSocial(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def type(self):
        return self.data.get('type')

    @property
    def url(self):
        return self.data.get('url')


class YMOpinionAuthor(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def name(self):
        return self.data.get('name')

    @property
    def avatarUrl(self):
        return self.data.get('avatarUrl')

    @property
    def grades(self):
        return self.data.get('grades')

    @property
    def visibility(self):
        return self.data.get('visibility')

    @property
    def social(self):
        return [YMOpinionAuthorSocial(social) for social in self.data.get('social')]


class YMModelOpinionUser(YMBase):
    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')


class YMOpinionComment(YMBase):
    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        return self.data.get('id')

    @property
    def rootId(self):
        return self.data.get('rootId')

    @property
    def parentId(self):
        return self.data.get('parentId')

    @property
    def title(self):
        return self.data.get('title')

    @property
    def updateTimestamp(self):
        return self.data.get('updateTimestamp')

    @property
    def valid(self):
        return self.data.get('valid')

    @property
    def deleted(self):
        return self.data.get('deleted')

    @property
    def blocked(self):
        return self.data.get('blocked')

    @property
    def sticky(self):
        return self.data.get('sticky')

    @property
    def body(self):
        return self.data.get('body')

    @property
    def user(self):
        return YMModelOpinionUser(self.data.get('user'))

    @property
    def children(self):
        return [YMOpinionComment(comment) for comment in self.data.get('children')]


class YMModelOpinionModel(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')


class YMModelOpinionShop(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        return self.data.get('id')

    @property
    def name(self):
        return self.data.get('name')


class YMModelOpinion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        return self.data.get('id')

    @property
    def date(self):
        return self.data.get('date')

    @property
    def vote(self):
        return self.data.get('vote')

    @property
    def grade(self):
        return self.data.get('grade')

    @property
    def rejectReason(self):
        return self.data.get('rejectReason')

    @property
    def state(self):
        return self.data.get('state')

    @property
    def agreeCount(self):
        return self.data.get('agreeCount')

    @property
    def disagreeCount(self):
        return self.data.get('disagreeCount')

    @property
    def usageTime(self):
        return self.data.get('usageTime')

    @property
    def verifiedBuyer(self):
        return self.data.get('verifiedBuyer')

    @property
    def text(self):
        return self.data.get('text')

    @property
    def pros(self):
        return self.data.get('pros')

    @property
    def cons(self):
        return self.data.get('cons')

    @property
    def author(self):
        return YMOpinionAuthor(self.data.get('author'))

    @property
    def comments(self):
        return [YMOpinionComment(comment) for comment in self.data.get('comments')]

    @property
    def region(self):
        return YMRegion(self.data.get('region'))

    @property
    def model(self):
        return YMModelOpinionModel(self.data.get('model'))


class YMShopOpinion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        return self.data.get('id')

    @property
    def date(self):
        return self.data.get('date')

    @property
    def vote(self):
        return self.data.get('vote')

    @property
    def grade(self):
        return self.data.get('grade')

    @property
    def rejectReason(self):
        return self.data.get('rejectReason')

    @property
    def state(self):
        return self.data.get('state')

    @property
    def agreeCount(self):
        return self.data.get('agreeCount')

    @property
    def disagreeCount(self):
        return self.data.get('disagreeCount')

    @property
    def shopOrderId(self):
        return self.data.get('shopOrderId')

    @property
    def delivery(self):
        return self.data.get('delivery')

    @property
    def problem(self):
        return self.data.get('problem')

    @property
    def text(self):
        return self.data.get('text')

    @property
    def pros(self):
        return self.data.get('pros')

    @property
    def cons(self):
        return self.data.get('cons')

    @property
    def author(self):
        return YMOpinionAuthor(self.data.get('author'))

    @property
    def comments(self):
        return [YMOpinionComment(comment) for comment in self.data.get('comments')]

    @property
    def region(self):
        return YMRegion(self.data.get('region'))

    @property
    def shop(self):
        return YMModelOpinionShop(self.data.get('model'))
