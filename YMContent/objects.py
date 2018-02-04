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
    """Предупреждение"""

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('shortText'))

    @property
    def text(self):
        """

        :return: Текст предупреждения
        :rtype: str
        """
        return self.data.get('text')

    @property
    def shortText(self):
        """

        :return: Краткий текст предупреждения
        :rtype: str
        """
        return self.data.get('shortText')

    @property
    def age(self):
        """

        :return: Возрастное ограничение для категории
        :rtype: int
        """
        return self.data.get('age')


class YMCategory(YMBase):
    """Категория"""

    def __repr__(self):
        return '<{}: {} ({})>'.format(self.__class__.__name__, self.data.get('name'), self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор категории
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование категории
        :rtype: str
        """
        return self.data.get('name')

    @property
    def fullName(self):
        """

        :return: Полное наименование категории
        :rtype: str
        """
        return self.data.get('fullName')

    @property
    def parent(self):
        """

        :return: Идентификатор родительской категории
        :rtype: int
        """
        return self.data.get('parent')

    @property
    def adult(self):
        """

        :return: Признак категории, имеющей возрастное ограничение (18+)
        :rtype: bool
        """
        return self.data.get('adult')

    @property
    def link(self):
        """

        :return: Ссылка на карточку категории на Яндекс.Маркете
        :rtype: str
        """
        return self.data.get('link')

    @property
    def childCount(self):
        """

        :return: Количество дочерних категорий
        :rtype: int
        """
        return self.data.get('childCount')

    @property
    def modelCount(self):
        """

        :return: Количество моделей в категории
        :rtype: int
        """
        return self.data.get('modelCount')

    @property
    def offerCount(self):
        """

        :return: Количество товарных предложений в категории
        :rtype: int
        """
        return self.data.get('offerCount')

    @property
    def advertisingModel(self):
        """

        :return: Тип размещения товарных предложений в категории
        :rtype: str
        """
        return self.data.get('advertisingModel')

    @property
    def viewType(self):
        """

        :return: Тип отображения товаров в категории
        :rtype: str
        """
        return self.data.get('viewType')

    @property
    def warnings(self):
        """

        :return: Предупреждения, связанные с категорией
        :rtype: list[objects.YMWarning]
        """
        return [YMWarning(warning) for warning in self.data.get('warnings', [])]


class YMSearchCategory(YMCategory):
    @property
    def findCount(self):
        return self.data.get('findCount')


class YMSortOption(YMBase):

    def __repr__(self):
        return '<{}: {} ({})>'.format(self.__class__.__name__, self.data.get('id'), self.data.get('how'))

    @property
    def id(self):
        """

        :return: Идентификатор варианта сортировки
        :rtype: str
        """
        return self.data.get('id')

    @property
    def how(self):
        """

        :return: Направление сортировки
        :rtype: str
        """
        return self.data.get('how')

    @property
    def text(self):
        """

        :return: Наименование данного варианта сортировки
        :rtype: str
        """
        return self.data.get('text')


class YMSort(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('text'))

    @property
    def text(self):
        """

        :return: Наименование типа сортировки
        :rtype: str
        """
        return self.data.get('text')

    @property
    def field(self):
        """

        :return: Тип сортировки
        :rtype: str
        """
        return self.data.get('field')

    @property
    def options(self):
        """

        :return: Доступные варианты для данного типа сортировки
        :rtype: [objects.YMSortOption]
        """
        return [YMSortOption(option) for option in self.data.get('options', [])]


class YMFilterValue(YMBase):

    def __repr__(self):
        return '<{}: {} ({})>'.format(self.__class__.__name__, self.data.get('id'), self.data.get('name'))

    @property
    def id(self):
        """

        :return: Идентификатор значения фильтра, используется для установки значения фильтра
        :rtype: str
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Текстовое описание значение фильтра
        :rtype: str
        """
        return self.data.get('name')

    @property
    def initialFound(self):
        """

        :return: Количество моделей/офферов в выдаче, попадающих под значение фильтра, при отсутствии других фильтров
        :rtype: int
        """
        return self.data.get('initialFound')

    @property
    def found(self):
        """

        :return: Количество моделей/офферов в выдаче, попадающих под значение фильтра, при текущих условиях фильтрации
        :rtype: int
        """
        return self.data.get('found')

    @property
    def checked(self):
        """

        :return: Признак того, что значение выбрано в соответствии с текущими условиями фильтрации
        :rtype: bool
        """
        return self.data.get('checked')

    @property
    def color(self):
        """

        .. note:: Только для фильтра типа COLOR

        :return: Значение цвета
        :rtype: str
        """
        return self.data.get('color')

    @property
    def unitId(self):
        """

        .. note:: Только для фильтра типа SIZE

        :return: Код единицы измерения размера значения фильтра
        :rtype: str
        """
        return self.data.get('unitId')


class YMDatasourceOrder(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('sort'))

    @property
    def sort(self):
        """

        :return: Вариант/параметр, по которому осуществляется сортировка
        :rtype: str
        """
        return self.data.get('sort')

    @property
    def how(self):
        """

        :return: Направление сортировки
        :rtype: str
        """
        return self.data.get('how')


class YMDatasourceCriteria(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор фильтра
        :rtype: str
        """
        return self.data.get('id')

    @property
    def value(self):
        """

        :return: Значение фильтра
        :rtype: str
        """
        return self.data.get('value')

    @property
    def text(self):
        """

        :return: Текст поисковой фразы
        :rtype: str
        """
        return self.data.get('text')


class YMIcon(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('url'))

    @property
    def url(self):
        """

        :return: Ссылка на изображение
        :rtype: str
        """
        return self.data.get('url')


class YMDatasource(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def type(self):
        """

        :return: Тип источника данных
        :rtype: str
        """
        return self.data.get('id')

    @property
    def hid(self):
        """

        :return: Идентификатор категории
        :rtype: int
        """
        return self.data.get('hid')

    @property
    def nid(self):
        """

        :return: Идентификатор узла навигационного дерева
        :rtype: int
        """
        return self.data.get('nid')

    @property
    def order(self):
        """

        :return: Параметры сортировки моделей и товарных предложений источника
        :rtype: objects.YMDatasourceOrder
        """
        return YMDatasourceOrder(self.data.get('order'))

    @property
    def criteria(self):
        """

        :return: Список условий фильтрации моделей и товарных предложений источника
        :rtype: list[YMDatasourceCriteria]
        """
        return YMDatasourceCriteria(self.data.get('criteria'))


class YMNavigationNode(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор навигационного узла (nid)
        :rtype: int
        """
        return self.data.get('id')

    @property
    def hid(self):
        """

        :return: Идентификатор товарной категории (hid)
        :rtype: int
        """
        return self.data.get('hid')

    @property
    def shortName(self):
        """

        :return: Краткое наименование навигационного узла
        :rtype: str
        """
        return self.data.get('shortName')

    @property
    def type(self):
        """

        :return: Тип узла навигационного дерева
        :rtype: str
        """
        return self.data.get('type')

    @property
    def offerCount(self):
        """

        :return: Количество товарных предложений в категории узла
        :rtype: int
        """
        return self.data.get('offerCount')

    @property
    def modelCount(self):
        """

        :return: Количество моделей в категории узла
        :rtype: int
        """
        return self.data.get('modelCount')

    @property
    def visual(self):
        """

        :return: Признак визуальной категории
        :rtype: bool
        """
        return self.data.get('visual')

    @property
    def maxDiscount(self):
        """

        :return: Максимальная скидка в категории
        :rtype: str
        """
        return self.data.get('maxDiscount')

    @property
    def name(self):
        """

        :return: Полное наименование навигационного узла
        :rtype: str
        """
        return self.data.get('name')

    @property
    def datasource(self):
        """

        :return: Информация о источнике данных для узла навигационного дерева
        :rtype: objects.YMDatasource
        """
        return YMDatasource(self.data.get('datasource'))

    @property
    def icons(self):
        """

        :return: Список изображений, относящихся к данному узлу навигационного дерева
        :rtype: list[YMIcon]
        """
        return [YMIcon(icon) for icon in self.data.get('icons', [])]

    @property
    def parents(self):
        """

        :return: Иерархический список всех родителей узла, начиная с корня
        :rtype: list[objects.YMNavigationNode]
        """
        return [YMNavigationNode(node) for node in self.data.get('parents', [])]

    @property
    def categories(self):
        """

        :return: Список дочерних узлов
        :rtype: list[objects.YMNavigationNode]
        """
        return [YMNavigationNode(node) for node in self.data.get('categories', [])]


class YMFilter(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор фильтра
        :rtype: str
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование фильтра
        :rtype: str
        """
        return self.data.get('name')

    @property
    def type(self):
        """

        :return: Тип фильтра
        :rtype: str
        """
        return self.data.get('type')

    @property
    def description(self):
        """

        :return: Описание фильтра
        :rtype: str
        """
        return self.data.get('description')

    @property
    def unit(self):
        """

        :return: Единицы измерения значений фильтра
        :rtype: str
        """
        return self.data.get('unit')

    @property
    def defaultUnit(self):
        """

        :return: Код единиц измерения значений фильтра, используемых по умолчанию
        :rtype: str
        """
        return self.data.get('defaultUnit')

    @property
    def values(self):
        """

        :return: Список значений фильтра
        :rtype: list[objects.YMFilterValue]
        """
        return [YMFilterValue(value) for value in self.data.get('values', [])]

    @property
    def max(self):
        """

        :return: Максимальное значение числового фильтра
        :rtype: str
        """
        return self.data.get('max')

    @property
    def min(self):
        """

        :return: Минимальное значение числового фильтра
        :rtype: str
        """
        return self.data.get('min')

    @property
    def value(self):
        """

        :return: Выбранное значение числового фильтра
        :rtype: str
        """
        return self.data.get('value')

    @property
    def precision(self):
        """

        :return: Количество знаков поле запятой у значений фильтра
        :rtype: int
        """
        return self.data.get('precision')


class YMModelPhoto(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('url'))

    @property
    def width(self):
        """

        :return: Ширина изображения
        :rtype: int
        """
        return self.data.get('width')

    @property
    def height(self):
        """

        :return: Высота изображения
        :rtype: int
        """
        return self.data.get('height')

    @property
    def url(self):
        """

        :return: Ссылка на изображение
        :rtype: str
        """
        return self.data.get('url')

    @property
    def colorId(self):
        """

        :return: Код значения фильтра по цвету
        :rtype: str
        """
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
        return [YMVendorCategory(category) for category in self.data.get('children', [])]


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
        return [YMVendorCategory(category) for category in self.data.get('categories', [])]

    @property
    def topCategories(self):
        return [YMVendorCategory(category) for category in self.data.get('topCategories', [])]


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
        return [YMSpecificationFeature(feature) for feature in self.data.get('features', [])]


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
        return [YMParameterOption(parameter) for parameter in self.data.get('options', [])]


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
        """

        :return: Идентификатор модели
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование модели
        :rtype: str
        """
        return self.data.get('name')

    @property
    def kind(self):
        """

        :return: Тип товара
        :rtype: str
        """
        return self.data.get('kind')

    @property
    def type(self):
        """

        :return: Тип модели
        :rtype: str
        """
        return self.data.get('type')

    @property
    def isNew(self):
        """

        :return: Признак "новизны" товара
        :rtype: bool
        """
        return self.data.get('isNew')

    @property
    def link(self):
        """

        :return: Ссылка на карточку модели на большом маркете
        :rtype: str
        """
        return self.data.get('link')

    # todo пустое описание
    @property
    def vendorLink(self):
        """

        :return:
        :rtype:
        """
        return self.data.get('vendorLink')

    # todo пустое описание
    @property
    def barcode(self):
        """

        :return:
        :rtype:
        """
        return self.data.get('barcode')

    # todo пустое описание
    @property
    def vendorCode(self):
        """

        :return:
        :rtype:
        """
        return self.data.get('vendorCode')

    @property
    def offerCount(self):
        """

        :return: Количество товарных предложений модели в регионе запроса
        :rtype: int
        """
        return self.data.get('offerCount')

    @property
    def opinionCount(self):
        """

        :return: Количество отзывов на модель
        :rtype: int
        """
        return self.data.get('opinionCount')

    @property
    def reviewCount(self):
        """

        :return: Количество статей/обзоров на модель
        :rtype: int
        """
        return self.data.get('reviewCount')

    @property
    def modificationCount(self):
        """

        :return: Количество модификаций групповой модели. Поле отсутствует в выдаче, если модель не групповая
        :rtype: int
        """
        return self.data.get('modificationCount')

    @property
    def lastUpdate(self):
        """

        :return: Дата-время последнего обновления модели в спсике стравнения
        :rtype: int
        """
        return self.data.get('lastUpdate')

    # todo пустое описание
    @property
    def aliases(self):
        """

        :return:
        :rtype:
        """
        return self.data.get('aliases')

    @property
    def parent(self):
        """

        :return: Идентификатор модели
        :rtype: int
        """
        return self.data.get('parent')

    @property
    def description(self):
        """

        :return: Описание модели
        :rtype: str
        """
        return self.data.get('description')

    @property
    def photo(self):
        """

        :return: Основное изображение модели
        :rtype: objects.YMModelPhoto
        """
        return YMModelPhoto(self.data.get('photo'))

    @property
    def photos(self):
        """

        :return: Остальные изображения модели
        :rtype: list[objects.YMModelPhoto]
        """
        return [YMModelPhoto(photo) for photo in self.data.get('photos', [])]

    @property
    def category(self):
        """

        :return: Информация о категории, к которой относится модель
        :rtype: objects.YMCategory
        """
        return YMCategory(self.data.get('category'))

    @property
    def navigationNode(self):
        """

        :return: Информация об узле навигационного дерева, к которому относится модель
        :rtype: objects.YMNavigationNode
        """
        return YMNavigationNode(self.data.get('navigationNode'))

    @property
    def price(self):
        """

        :return: Информация о цене модели в основной валюте запроса
        :rtype: objects.YMPrice
        """
        return YMPrice(self.data.get('price'))

    @property
    def alternatePrice(self):
        """

        :return: Информация о цене модели в альтернативной валюте запроса
        :rtype: objects.YMPrice
        """
        return YMPrice(self.data.get('price'))

    @property
    def vendor(self):
        """

        :return: Информация о производителе модели
        :rtype: objects.YMVendor
        """
        return YMVendor(self.data.get('vendor'))

    @property
    def rating(self):
        """

        :return: Информация о рейтинге модели
        :rtype: objects.YMRating
        """
        return YMRating(self.data.get('rating'))

    @property
    def facts(self):
        """

        :return: Факты о модели
        :rtype: objects.YMFacts
        """
        return YMFacts(self.data.get('facts'))

    @property
    def warning(self):
        """

        :return: Дисклеймер, связанный с моделью
        :rtype: str
        """
        return self.data.get('warning')

    @property
    def warnings(self):
        """

        :return: Строковый код дисклеймера
        :rtype: list[objects.YMModelWarning]
        """
        return [YMModelWarning(warning) for warning in self.data.get('warnings', [])]

    @property
    def filters(self):
        """

        :return: Список фильтров, предназначенных для фильтрации моделей/модификаций
        :rtype: list[objects.YMFilter]
        """
        return [YMFilter(filter) for filter in self.data.get('filters', [])]

    @property
    def modifications(self):
        """

        :return: Список модификаций групповой модели
        :rtype: list[objects.YMModification]
        """
        return [YMModification(modification) for modification in self.data.get('modifications', [])]

    @property
    def specification(self):
        """

        :return: Основные характеристики модели
        :rtype: list[objects.YMSpecification]
        """
        return [YMSpecification(specification) for specification in self.data.get('specification', [])]

    # todo пустое описание
    @property
    def parameters(self):
        """

        :return:
        :rtype:
        """
        return [YMParameter(parameter) for parameter in self.data.get('parameters', [])]

    @property
    def userRelated(self):
        """

        :return: Информация, касающаяся текущего пользователя
        :rtype: list[objects.YMUserRelated]
        """
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
        return [YMOrganization(organization) for organization in self.data.get('organizations', [])]


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
        return [YMDeliveryOption(option) for option in self.data.get('options', [])]

    @property
    def pickupOptions(self):
        return [YMDeliveryPickupOption(option) for option in self.data.get('pickupOptions', [])]


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
        return [YMModelPhoto(photo) for photo in self.data.get('photos', [])]

    @property
    def photo(self):
        return YMModelPhoto(self.data.get('photo'))

    @property
    def previewPhotos(self):
        return [YMModelPhoto(photo) for photo in self.data.get('previewPhotos', [])]

    @property
    def activeFilters(self):
        return [YMFilter(f) for f in self.data.get('activeFilters', [])]

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
        return [YMStatisticsRegion(region) for region in self.data.get('regions', [])]


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
        return [YMOpinionAuthorSocial(social) for social in self.data.get('social', [])]


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
        return [YMOpinionComment(comment) for comment in self.data.get('children', [])]


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
        return [YMOpinionComment(comment) for comment in self.data.get('comments', [])]

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
        return [YMOpinionComment(comment) for comment in self.data.get('comments', [])]

    @property
    def region(self):
        return YMRegion(self.data.get('region'))

    @property
    def shop(self):
        return YMModelOpinionShop(self.data.get('model'))


class YMAddress(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def regionId(self):
        return self.data.get('regionId')

    @property
    def type(self):
        return self.data.get('type')

    @property
    def country(self):
        return self.data.get('country')

    @property
    def region(self):
        return self.data.get('region')

    @property
    def subRegion(self):
        return self.data.get('subRegion')

    @property
    def locality(self):
        return self.data.get('locality')

    @property
    def subLocality(self):
        return self.data.get('subLocality')

    @property
    def thoroughfare(self):
        return self.data.get('thoroughfare')

    @property
    def premiseNumber(self):
        return self.data.get('premiseNumber')

    @property
    def fullAddress(self):
        return self.data.get('fullAddress')

    @property
    def block(self):
        return self.data.get('block')

    @property
    def wing(self):
        return self.data.get('wing')

    @property
    def estate(self):
        return self.data.get('estate')

    @property
    def entrance(self):
        return self.data.get('entrance')

    @property
    def floor(self):
        return self.data.get('floor')

    @property
    def room(self):
        return self.data.get('room')

    @property
    def note(self):
        return self.data.get('note')

    @property
    def distance(self):
        return self.data.get('distance')

    @property
    def latitude(self):
        return self.data.get('latitude')

    @property
    def longitude(self):
        return self.data.get('longitude')

    @property
    def postcode(self):
        return self.data.get('postcode')


class YMSchedule(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def daysFrom(self):
        return self.data.get('daysFrom')

    @property
    def daysTill(self):
        return self.data.get('daysTill')

    @property
    def timeFrom(self):
        return self.data.get('from')

    @property
    def timeTill(self):
        return self.data.get('till')


class YMOutlet(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

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
    def shop(self):
        return YMShop(self.data.get('shop'))

    @property
    def phones(self):
        return [YMPhone(phone) for phone in self.data.get('phones', [])]

    @property
    def address(self):
        return YMAddress(self.data.get('address'))

    @property
    def schedule(self):
        return [YMSchedule(s) for s in self.data.get('schedule', [])]

    @property
    def distance(self):
        return self.data.get('distance')

    @property
    def latitude(self):
        return self.data.get('latitude')

    @property
    def longitude(self):
        return self.data.get('longitude')

    @property
    def offer(self):
        return YMOffer(self.data.get('offer'))


class YMRedirectModel(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def type(self):
        return self.data.get('type')

    @property
    def queryText(self):
        return self.data.get('queryText')

    @property
    def link(self):
        return self.data.get('link')

    @property
    def model(self):
        return YMModel(self.data.get('content').get('model'))

    @property
    def model_id(self):
        return self.data.get('model')['id']


class YMRedirectCatalog(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def type(self):
        return self.data.get('type')

    @property
    def queryText(self):
        return self.data.get('queryText')

    @property
    def link(self):
        return self.data.get('link')

    @property
    def items(self):
        return [YMModel(item) if 'model' in item.keys() else YMOffer(item) for item in self.get('items', [])]

    @property
    def categories(self):
        return [YMSearchCategory(category) for category in self.get('categories', [])]

    @property
    def sorts(self):
        return [YMSort(sort) for sort in self.get('sorts', [])]

    @property
    def navigationNode(self):
        return YMNavigationNode(self.data.get('navigationNode'))

    @property
    def criteria(self):
        return [YMDatasourceCriteria(c) for c in self.data.get('criteria', [])]


class YMRedirectVendor(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def type(self):
        return self.data.get('type')

    @property
    def queryText(self):
        return self.data.get('queryText')

    @property
    def link(self):
        return self.data.get('link')

    @property
    def vendor(self):
        return YMVendor(self.data.get('content').get('vendor'))

    @property
    def vendor_id(self):
        return self.data.get('vendor')['id']


class YMRedirectSearch(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def type(self):
        return self.data.get('type')

    @property
    def queryText(self):
        return self.data.get('queryText')

    @property
    def link(self):
        return self.data.get('link')

    @property
    def filters(self):
        return [YMFilter(f) for f in self.resp.get('filters', [])]

    @property
    def sorts(self):
        return [YMSort(sort) for sort in self.resp.get('sorts', [])]

    @property
    def criteria(self):
        return [YMDatasourceCriteria(c) for c in self.data.get('criteria', [])]


class YMSuggestion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def value(self):
        return self.data.get('value')

    @property
    def url(self):
        return self.data.get('url')


class YMSuggestionCompletion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def completion(self):
        return self.data.get('completion')

    @property
    def value(self):
        return self.data.get('value')
