# -*- coding: utf-8 -*-
class YMBase(object):
    def __init__(self, data):
        self.data = data

    def json(self):
        """

        :return: Объект в виде JSON
        :rtype: dict
        """
        return self.data


class YMRegion(YMBase):
    """Регион"""

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        """

        :return: Идентификатор региона
        :rtype: int

        225
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование региона
        :rtype: str

        Россия
        """
        return self.data.get('name')

    @property
    def type(self):
        """

        :return: Тип региона
        :rtype: str

        * **CONTINENT** — континент
        * **REGION** — регион
        * **COUNTRY** — страна
        * **COUNTRY_DISTRICT** — федеральный округ
        * **SUBJECT_FEDERATION** — субъект федерации
        * **CITY** — город
        * **VILLAGE** — село
        * **CITY_DISTRICT** — район города
        * **METRO_STATION** — станиция метро
        * **SUBJECT_FEDERATION_DISTRICT** — район субъекта федерации
        * **AIRPORT** — аэропорт
        * **OVERSEAS_TERRITORY** — отдельная территория какого-либо государства, расположенная в другой части света (например, Ангилья, Гренландия, Бермудские острова и т. д.)
        * **SECONDARY_DISTRICT** — район города второго уровня (например, для ВАО Москвы районами второго уровня являются Измайлово, Новокосино, Перово и т. д.)
        * **MONORAIL_STATION** — станция монорельса
        * **RURAL_SETTLEMENT** — сельское поселение
        * **OTHER** — другой тип населенного пункта
        * **HIDDEN** —
        """
        return self.data.get('type')

    @property
    def childCount(self):
        """

        :return: Количество дочерних регионов
        :rtype: int

        14
        """
        return self.data.get('childCount')

    @property
    def nameAccusative(self):
        """

        :return: Наименование региона в винительном падеже
        :rtype: str or None
        """
        return self.data.get('nameAccusative')

    @property
    def nameGenitive(self):
        """

        :return: Наименование региона в родительном падеже
        :rtype: str or None
        """
        return self.data.get('nameGenitive')

    @property
    def country(self):
        """

        :return: Страна, к которой относится регион
        :rtype: YMRegion or None
        """
        return YMRegion(self.data.get('country'))

    @property
    def parent(self):
        """

        :return: Родительский регион
        :rtype: YMRegion or None
        """
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

        90402
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование категории
        :rtype: str

        Авто
        """
        return self.data.get('name')

    @property
    def fullName(self):
        """

        :return: Полное наименование категории
        :rtype: str or None

        Товары для авто- и мототехники
        """
        return self.data.get('fullName')

    @property
    def parent(self):
        """

        :return: Идентификатор родительской категории
        :rtype: int or None

        90401
        """
        return self.data.get('parent')

    @property
    def adult(self):
        """

        :return: Признак категории, имеющей возрастное ограничение (18+)
        :rtype: bool

        False
        """
        return self.data.get('adult', False)

    @property
    def link(self):
        """

        :return: Ссылка на карточку категории на Яндекс.Маркете
        :rtype: str or None

        https://market.yandex.ru/catalog/90402/list?hid=90402&onstock=1&pp=1001
        """
        return self.data.get('link')

    @property
    def childCount(self):
        """

        :return: Количество дочерних категорий
        :rtype: int

        12
        """
        return self.data.get('childCount')

    @property
    def modelCount(self):
        """

        :return: Количество моделей в категории
        :rtype: int or None

        181170
        """
        return self.data.get('modelCount')

    @property
    def offerCount(self):
        """

        :return: Количество товарных предложений в категории
        :rtype: int or None

        3531718
        """
        return self.data.get('offerCount')

    @property
    def advertisingModel(self):
        """

        :return: Тип размещения товарных предложений в категории
        :rtype: str or None

        * **CPA** — плата за заказы, оформленные прямо на Яндекс.Маркете
        * **CPC** — плата только за клики по предложению магазина
        * **HYBRID** — возможны оба варианта размещения товарных предложений в категории
        """
        return self.data.get('advertisingModel')

    @property
    def viewType(self):
        """

        :return: Тип отображения товаров в категории
        :rtype: str or None

        * **LIST** — список
        * **GRID** — сетка
        """
        return self.data.get('viewType')

    @property
    def warnings(self):
        """

        :return: Предупреждения, связанные с категорией
        :rtype: list[YMWarning]
        """
        return [YMWarning(warning) for warning in self.data.get('warnings', [])]


class YMSearchCategory(YMCategory):
    @property
    def findCount(self):
        """

        :return: Количество категорий в результатах поиска
        :rtype: int

        12
        """
        return self.data.get('findCount')


class YMSortOption(YMBase):
    """Опции сортировки"""

    def __repr__(self):
        return '<{}: {} ({})>'.format(self.__class__.__name__, self.data.get('id'), self.data.get('how'))

    @property
    def id(self):
        """

        :return: Идентификатор варианта сортировки
        :rtype: str

        aprice
        """
        return self.data.get('id')

    @property
    def how(self):
        """

        :return: Направление сортировки
        :rtype: str

        * **ASC** — по возрастанию
        * **DESC** — по убыванию
        """
        return self.data.get('how')

    @property
    def text(self):
        """

        :return: Наименование данного варианта сортировки
        :rtype: str

        Сначала дешёвые
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

        по цене
        """
        return self.data.get('text')

    @property
    def field(self):
        """

        :return: Тип сортировки
        :rtype: str or None

        * **RELEVANCY** — сортировка по релевантности.
        * **PRICE** — сортировка по цене.
        * **RATING** — сортировка по рейтингу.
        * **DISTANCE** — сортировка по расстоянию до ближайшей точки продаж (значение доступно только при указании местоположения пользователя).
        * **POPULARITY** — сортировка по популярности.
        * **DISCOUNT** — сортировка по размеру скидки.

        .. note:: Для sort=DISCOUNT возможна только сортировка по убыванию (how=DESC).

        * **QUALITY** — сортировка по рейтингу.
        * **OPINIONS** — сортировка по количеству отзывов.
        * **DATE** — сортировка по дате.
        * **DELIVERY_TIME** — сортировка по времени доставки.
        * **NOFFERS** — сортировка по количеству предложений
        """
        return self.data.get('field')

    @property
    def options(self):
        """

        :return: Доступные варианты для данного типа сортировки
        :rtype: list[YMSortOption]
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

        12612583
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Текстовое описание значение фильтра
        :rtype: str

        AGV
        """
        return self.data.get('name')

    @property
    def initialFound(self):
        """

        :return: Количество моделей/офферов в выдаче, попадающих под значение фильтра, при отсутствии других фильтров
        :rtype: int or None

        56
        """
        return self.data.get('initialFound')

    @property
    def found(self):
        """

        :return: Количество моделей/офферов в выдаче, попадающих под значение фильтра, при текущих условиях фильтрации
        :rtype: int or None

        56
        """
        return self.data.get('found')

    @property
    def sku(self):
        """

        :return: id sku на который переключимся, если проставим это значение в фильтр (карта фильтров)
        :rtype: str or None
        """
        return self.data.get('sku')

    @property
    def checked(self):
        """

        :return: Признак того, что значение выбрано в соответствии с текущими условиями фильтрации
        :rtype: bool or None
        """
        return self.data.get('checked')

    @property
    def color(self):
        """

        .. note:: Только для фильтров типов COLOR и Filters.FilterType#PHOTO_PICKER

        :return: Значение цвета
        :rtype: str or None
        """
        return self.data.get('color')

    @property
    def unitId(self):
        """

        .. note:: Только для фильтра типа SIZE

        :return: Код единицы измерения размера значения фильтра
        :rtype: str or None
        """
        return self.data.get('unitId')

    @property
    def photo(self):
        """

        .. note:: Только для фильтра типа Filters.FilterType#PHOTO_PICKER

        :return: Ссылку на картинку для выбора цвета
        :rtype: str or None
        """
        return self.data.get('photo')


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
        return '<{}>'.format(self.__class__.__name__)

    @property
    def type(self):
        """

        :return: Тип источника данных
        :rtype: str
        """
        # todo Нет примера
        return self.data.get('type')

    @property
    def hid(self):
        """

        :return: Идентификатор категории
        :rtype: int

        91491
        """
        return self.data.get('hid')

    @property
    def nid(self):
        """

        :return: Идентификатор узла навигационного дерева
        :rtype: int

        54726
        """
        return self.data.get('nid')

    @property
    def sort(self):
        """

        :return: Вариант/параметр, по которому осуществляется сортировка
        :rtype: str or None

        * **POPULARITY** — По популярности
        * **PRICE** — По цене
        * **DATE** — Сначала новые
        * **RELEVANCE** — По релевантности
        * **RATING** — По рейтингу и цене
        * **DISTANCE** — По удаленности
        * **DISCOUNT** — По скидке (сортировка работает только по убыванию)
        * **QUALITY** — По рейтингу
        * **OPINIONS** — По отзывам
        * **DELIVERY_TIME** — По времени доставки
        """
        return self.data.get('order',{}).get('sort')

    @property
    def how(self):
        """

        :return: Направление сортировки
        :rtype: str or None

        * **ASC** — по возрастанию;
        * **DESC** — по убыванию.
        """
        return self.data.get('order', {}).get('how')

    @property
    def criteria(self):
        """

        :return: Список условий фильтрации моделей и товарных предложений источника
        :rtype: list[YMDatasourceCriteria]
        """
        return [YMDatasourceCriteria(criteria) for criteria in self.data.get('criteria', [])]


class YMNavigationNode(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор навигационного узла (nid)
        :rtype: int

        54726
        """
        return self.data.get('id')

    @property
    def hid(self):
        """

        :return: Идентификатор товарной категории (hid)
        :rtype: int

        91491
        """
        return self.data.get('hid')

    @property
    def shortName(self):
        """

        :return: Краткое наименование навигационного узла
        :rtype: str

        Мобильные телефоны
        """
        return self.data.get('shortName')

    @property
    def type(self):
        """

        :return: Тип узла навигационного дерева
        :rtype: str
        """
        # todo бывает нескольких видов, предположительно category, virtual, link
        return self.data.get('type')

    @property
    def offerCount(self):
        """

        :return: Количество товарных предложений в категории узла
        :rtype: int or None

        55595
        """
        return self.data.get('offerCount')

    @property
    def modelCount(self):
        """

        :return: Количество моделей в категории узла
        :rtype: int or None

        3002
        """
        return self.data.get('modelCount')

    @property
    def visual(self):
        """

        :return: Признак визуальной категории
        :rtype: bool or None
        """
        # todo нет примера
        return self.data.get('visual')

    @property
    def maxDiscount(self):
        """

        :return: Максимальная скидка в категории
        :rtype: str or None
        """
        # todo нет примера
        return self.data.get('maxDiscount')

    @property
    def name(self):
        """

        :return: Полное наименование навигационного узла
        :rtype: str

        Мобильные телефоны
        """
        return self.data.get('name')

    @property
    def datasource(self):
        """

        :return: Информация о источнике данных для узла навигационного дерева
        :rtype: YMDatasource
        """
        return YMDatasource(self.data.get('datasource'))

    @property
    def icons(self):
        """

        :return: Список изображений, относящихся к данному узлу навигационного дерева
        :rtype: list[YMIcon]
        """
        # todo нет примера
        return [YMIcon(icon) for icon in self.data.get('icons', [])]

    @property
    def parents(self):
        """

        :return: Иерархический список всех родителей узла, начиная с корня
        :rtype: list[YMNavigationNode]
        """
        # todo нет примера
        return [YMNavigationNode(node) for node in self.data.get('parents', [])]

    @property
    def categories(self):
        """

        :return: Список дочерних узлов
        :rtype: list[YMNavigationNode]
        """
        # todo нет примера
        return [YMNavigationNode(node) for node in self.data.get('categories', [])]


class YMFilter(YMBase):
    """Фильтр"""

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор фильтра
        :rtype: str

        -2
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование фильтра
        :rtype: str

        Гарантия производителя
        """
        return self.data.get('name')

    @property
    def type(self):
        """

        :return: Тип фильтра
        :rtype: str

        * **BOOLEAN** — логический тип
        * **NUMBER** — числовой тип, задает диапазон допустимых значений
        * **ENUM** — тип перечисление, задает список допустимых значений, множественный выбор
        * **COLOR** — фильтр по цвету, аналогичен ENUM, значения фильтра дополнительно содержат HEX-код соответствующего цвета
        * **SIZE** — фильтр по размеру, аналогичен ENUM, значения фильтра дополнительно содержат код единиц измерения
        * **RADIO** — аналогичен ENUM, но допускает выбор только одного значения
        * **TEXT** — тип фильтра для фильтрации по поисковой фразе
        * **PHOTO_PICKER** —
        """
        return self.data.get('type')

    @property
    def description(self):
        """

        :return: Описание фильтра
        :rtype: str or None
        """
        # todo нет примера
        return self.data.get('description')

    @property
    def unit(self):
        """

        :return: Единицы измерения значений фильтра
        :rtype: str or None
        """
        # todo нет примера
        return self.data.get('unit')

    @property
    def defaultUnit(self):
        """

        :return: Код единиц измерения значений фильтра, используемых по умолчанию
        :rtype: str or None
        """
        # todo нет примера
        return self.data.get('defaultUnit')

    @property
    def values(self):
        """

        :return: Список значений фильтра
        :rtype: list[YMFilterValue]
        """
        # todo нет примера
        return [YMFilterValue(value) for value in self.data.get('values', [])]

    @property
    def max(self):
        """

        :return: Максимальное значение числового фильтра
        :rtype: str or None
        """
        # todo никогда не возвращается
        return self.data.get('max')

    @property
    def min(self):
        """

        :return: Минимальное значение числового фильтра
        :rtype: str or None
        """
        # todo никогда не возвращается
        return self.data.get('min')

    @property
    def value(self):
        """

        :return: Выбранное значение числового фильтра
        :rtype: str or None
        """
        # todo никогда не возвращается
        return self.data.get('value')

    @property
    def precision(self):
        """

        :return: Количество знаков поле запятой у значений фильтра
        :rtype: int or None
        """
        # todo никогда не возвращается
        return self.data.get('precision')


class YMThumbnail(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('url'))

    @property
    def width(self):
        """

        :return: Ширина изображения
        :rtype: int

        321
        """
        return self.data.get('width')

    @property
    def height(self):
        """

        :return: Высота изображения
        :rtype: int

        620
        """
        return self.data.get('height')

    @property
    def url(self):
        """

        :return: Ссылка на изображение
        :rtype: str

        https://avatars.mds.yandex.net/get-mpic/397397/img_id7051974271832358544.png/orig
        """
        return self.data.get('url')

    @property
    def container(self):
        """

        :return: container
        :rtype: str

        * **W50xH50** — 50x50
        * **W100xH100** — 100x100
        * **W150xH150** — 150x150
        * **W200xH200** — 200x200
        * **W300xH300** — 300x300
        """
        # todo нет примера
        return self.data.get('container')


class YMCriteria(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('url'))

    @property
    def id(self):
        """

        :return: Идентификатор фильтра
        :rtype: str
        """
        # todo нет примера
        return self.data.get('id')

    @property
    def value(self):
        """

        :return: Значение фильтра
        :rtype: str
        """
        # todo нет примера
        return self.data.get('value')

    @property
    def text(self):
        """

        :return: Текст поисковой фразы
        :rtype: str or None
        """
        # todo нет примера
        return self.data.get('text')


class YMModelPhoto(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('url'))

    @property
    def width(self):
        """

        :return: Ширина изображения
        :rtype: int

        321
        """
        return self.data.get('width')

    @property
    def height(self):
        """

        :return: Высота изображения
        :rtype: int

        620
        """
        return self.data.get('height')

    @property
    def url(self):
        """

        :return: Ссылка на изображение
        :rtype: str

        https://avatars.mds.yandex.net/get-mpic/397397/img_id7051974271832358544.png/orig
        """
        return self.data.get('url')

    @property
    def colorId(self):
        """

        :return: Код значения фильтра по цвету
        :rtype: str or None
        """
        # todo нет примера
        return self.data.get('colorId')

    @property
    def thumbnails(self):
        """

        :return: Уменьшенные копии изображения
        :rtype: list[YMThumbnail]
        """
        # todo нет примера
        return [YMThumbnail(thumbnail) for thumbnail in self.data.get('thumbnails', [])]

    @property
    def criteria(self):
        """

        :return: Критерий фильтрации копии изображения
        :rtype: list[YMCriteria]
        """
        # todo нет примера
        return [YMCriteria(criteria) for criteria in self.data.get('criteria', [])]


class YMPrice(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def max(self):
        """

        :return: Максимальная цена
        :rtype: str or None
        """
        return self.data.get('max')

    @property
    def min(self):
        """

        :return: Минимальная цена
        :rtype: str or None
        """
        return self.data.get('min')

    @property
    def avg(self):
        """

        :return: Среднее значение цены
        :rtype: str or None
        """
        return self.data.get('avg')

    @property
    def discount(self):
        """

        :return: Скидка
        :rtype: str or None
        """
        return self.data.get('discount')

    @property
    def base(self):
        """

        :return: Базовое значение цены
        :rtype: str or None
        """
        return self.data.get('base')


class YMShopPrice(YMBase):

    def __repr__(self):
        return '<{}'.format(self.__class__.__name__)

    @property
    def value(self):
        """

        :return: Значение цены
        :rtype: str
        """
        return self.data.get('value')

    @property
    def discount(self):
        """

        :return: Скидка
        :rtype: str or None
        """
        return self.data.get('discount')

    @property
    def base(self):
        """

        :return: Базовая цена
        :rtype: str or None
        """
        return self.data.get('base')

    @property
    def shopMin(self):
        """

        :return: Минимальная цена из всех склеенных офферов в данном магазине
        :rtype: str or None
        """
        return self.data.get('shopMin')

    @property
    def shopMax(self):
        """

        :return: Максимальная цена из всех склеенных офферов в данном магазине
        :rtype: str or None
        """
        return self.data.get('shopMax')


class YMVendorCategory(YMCategory):

    @property
    def popularity(self):
        """

        :return: Оценка популярности
        :rtype: float
        """
        return self.data.get('popularity')

    @property
    def children(self):
        """

        :return: Список дочерних категорий
        :rtype: list[YMVendorCategory]
        """
        return [YMVendorCategory(category) for category in self.data.get('children', [])]


class YMVendor(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор производителя
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование производителя
        :rtype: str or None
        """
        return self.data.get('name')

    @property
    def site(self):
        """

        :return: Ссылка на веб-сайт производителя
        :rtype: str or None
        """
        return self.data.get('site')

    @property
    def picture(self):
        """

        :return: Ссылка на изображение логотипа производителя
        :rtype: str or None
        """
        return self.data.get('picture')

    @property
    def recommendedShops(self):
        """

        :return: Ссылка на страницу производителя с рекомендованными магазинами
        :rtype: str or None
        """
        return self.data.get('recommendedShops')

    @property
    def link(self):
        """

        :return: Ссылка на карточку производителя на большом маркете
        :rtype: str or None
        """
        return self.data.get('link')

    @property
    def categories(self):
        """

        :return: Список категорий, в которых представлен данный производитель
        :rtype: list[YMVendorCategory]
        """
        return [YMVendorCategory(category) for category in self.data.get('categories', [])]

    @property
    def topCategories(self):
        """

        :return: Список наиболее популярных категорий товаров производителя
        :rtype: list[YMVendorCategory]
        """
        return [YMVendorCategory(category) for category in self.data.get('topCategories', [])]


class YMRatingDistribution(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def value(self):
        """

        :return: Значение оценки
        :rtype: float
        """
        return self.data.get('value')

    @property
    def count(self):
        """

        :return: Количество оценок с указанным значением
        :rtype: int
        """
        return self.data.get('count')

    @property
    def percent(self):
        """

        :return: Доля оценок с указанным значением среди всех оценок
        :rtype: int
        """
        return self.data.get('percent')


class YMRatingStatus(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        """

        :return: Код статуса рейтинга
        :rtype: str
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование статуса рейтинга
        :rtype: str
        """
        return self.data.get('name')


class YMRating(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def value(self):
        """

        :return: Средняя оценка рейтинга
        :rtype: float or int
        """
        return self.data.get('value')

    @property
    def count(self):
        """

        :return: Количество оценок
        :rtype: int
        """
        return self.data.get('count')

    @property
    def distribution(self):
        """

        :return: Информация о распределении оценок
        :rtype: list[YMRatingDistribution]
        """
        return [YMRatingDistribution(d) for d in self.data.get('distribution')]

    @property
    def status(self):
        """

        :return: Статус рейтинга
        :rtype: list[YMRatingStatus]
        """
        return [YMRatingStatus(d) for d in self.data.get('distribution')]


class YMFacts(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def pro(self):
        """

        :return: Достоинства
        :rtype: list[str]
        """
        return self.data.get('pro')

    @property
    def contra(self):
        """

        :return: Недостатки
        :rtype: list[str]
        """
        return self.data.get('contra')


class YMModelWarning(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('code'))

    @property
    def code(self):
        """

        :return: Строковый код дисклеймера
        :rtype: str
        """
        return self.data.get('code')

    @property
    def message(self):
        """

        :return: Текст дисклеймера
        :rtype: str
        """
        return self.data.get('message')


class YMModification(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор модели-модификации
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование модели-модификации
        :rtype: str
        """
        return self.data.get('name')

    @property
    def description(self):
        """

        :return: Описание модели-модификации
        :rtype: str
        """
        return self.data.get('description')

    @property
    def popularity(self):
        """

        :return: Оценка популярности модели-модификации
        :rtype: str
        """
        return self.data.get('popularity')

    @property
    def offerCount(self):
        """

        :return: Кол-во товарных предложений для данной модификации
        :rtype: int
        """
        return self.data.get('offerCount')

    @property
    def shopCount(self):
        """

        :return: Кол-во магазинов, имеющих товарные предложения данной модификации
        :rtype: int
        """
        return self.data.get('shopCount')

    @property
    def price(self):
        """

        :return: Информация о цене модификации
        :rtype: YMPrice
        """
        return YMPrice(self.data.get('price'))

    @property
    def alternatePrices(self):
        """

        :return: Информация о ценах на модификацию в альтернативной валюте запроса
        :rtype: YMPrice
        """
        return YMPrice(self.data.get('alternatePrices'))


class YMSpecificationFeature(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('name'))

    @property
    def name(self):
        """

        :return: Наименование характеристики
        :rtype: str
        """
        return self.data.get('name')

    @property
    def value(self):
        """

        :return: Значение характеристики
        :rtype: str
        """
        return self.data.get('value')


class YMSpecification(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('name'))

    @property
    def name(self):
        """

        :return: Название группы характеристик
        :rtype: str
        """
        return self.data.get('name')

    @property
    def features(self):
        """

        :return: -
        :rtype: list[YMSpecificationFeature]
        """
        return [YMSpecificationFeature(feature) for feature in self.data.get('features', [])]


class YMParameterOption(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор значения параметра
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Название значения параметра
        :rtype: str
        """
        return self.data.get('name')


class YMParameter(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('type'))

    @property
    def type(self):
        """

        :return: Тип параметра категории
        :rtype: str
        """
        return self.data.get('type')

    @property
    def parameterId(self):
        """

        :return: Идентификатор параметра
        :rtype: int
        """
        return self.data.get('parameterId')

    @property
    def multivalue(self):
        """

        :return: Признак, что параметр имеет несколько значений
        :rtype: bool
        """
        return self.data.get('multivalue')

    @property
    def name(self):
        """

        :return: Название параметра
        :rtype: str
        """
        return self.data.get('name')

    @property
    def unit(self):
        """

        :return: Единица измерения параметра
        :rtype: str
        """
        return self.data.get('unit')

    @property
    def mandatory(self):
        """

        :return: Является ли атрибут обязательным
        :rtype: bool
        """
        return self.data.get('mandatory')

    @property
    def values(self):
        """

        :return: Список значений параметра
        :rtype: list[bool]
        """
        return self.data.get('values')

    @property
    def options(self):
        """

        :return: Список возможных значений параметра
        :rtype: list[YMParameterOption]
        """
        return [YMParameterOption(parameter) for parameter in self.data.get('options', [])]


class YMUserRelated(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def inComparisonList(self):
        """

        :return: Модель находится в списках сравнений
        :rtype: bool
        """
        return self.data.get('inComparisonList')

    @property
    def inWishlist(self):
        """

        :return: Модель находится в отложеннных
        :rtype: bool
        """
        return self.data.get('inWishlist')


class YMModel(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор модели
        :rtype: int

        1732210983
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование модели
        :rtype: str

        Смартфон Apple iPhone X 256GB
        """
        return self.data.get('name')

    @property
    def kind(self):
        """

        :return: Тип товара
        :rtype: str or None

        автомагнитола
        """
        return self.data.get('kind')

    @property
    def type(self):
        """

        :return: Тип модели
        :rtype: str

        * **MODEL** — Обычная модель
        * **GROUP** — Групповая модель
        * **MODIFICATION** — Модификация
        * **BOOK** — Книга
        * **CLUSTER** — Визуальная модель
        """
        return self.data.get('type')

    @property
    def isNew(self):
        """

        :return: Признак "новизны" товара
        :rtype: bool

        False
        """
        return self.data.get('isNew')

    @property
    def link(self):
        """

        :return: Ссылка на карточку модели
        :rtype: str

        https://market.yandex.ru/product/1732210983?hid=91491&pp=1001
        """
        return self.data.get('link')

    @property
    def vendorLink(self):
        """

        :return: Ссылка на страницу производителя
        :rtype: str or None

        https://market.yandex.ru/brands/267101?pp=1001
        """
        return self.data.get('vendorLink')

    # todo пустое описание
    @property
    def barcode(self):
        """

        :return: Штрих-код модели
        :rtype: str or None
        """
        # todo нет примера
        return self.data.get('barcode')

    # todo пустое описание
    @property
    def vendorCode(self):
        """

        :return: Общий идентификатор модели
        :rtype: str or None
        """
        # todo нет примера
        return self.data.get('vendorCode')

    @property
    def offerCount(self):
        """

        :return: Количество товарных предложений модели в регионе запроса
        :rtype: int

        248
        """
        return self.data.get('offerCount')

    @property
    def opinionCount(self):
        """

        :return: Количество отзывов на модель
        :rtype: int

        33
        """
        return self.data.get('opinionCount')

    @property
    def reviewCount(self):
        """

        :return: Количество статей/обзоров на модель
        :rtype: int

        6
        """
        return self.data.get('reviewCount')

    @property
    def modificationCount(self):
        """

        :return: Количество модификаций групповой модели. Поле отсутствует в выдаче, если модель не групповая
        :rtype: int or None
        """
        # todo нет примера
        return self.data.get('modificationCount')

    @property
    def lastUpdate(self):
        """

        :return: Дата-время последнего обновления модели в спсике стравнения
        :rtype: int or None
        """
        # todo нет примера
        return self.data.get('lastUpdate')

    # todo пустое описание
    # todo нет примера
    @property
    def aliases(self):
        """

        :return: ---
        :rtype: str or None
        """
        return self.data.get('aliases')

    # todo нет примера
    @property
    def parent(self):
        """

        :return: Идентификатор модели
        :rtype: int or None
        """
        return self.data.get('parent', {}).get('id')

    @property
    def description(self):
        """

        :return: Описание модели
        :rtype: str

        GSM, LTE-A, смартфон, iOS 11, вес 174 г, ШхВхТ 70.9x143.6x7.7 мм, экран 5.8", 2436x1125, Bluetooth, NFC, Wi-Fi, GPS, ГЛОНАСС, фотокамера 12 МП, память 256 Гб
        """
        return self.data.get('description')

    @property
    def photo(self):
        """

        :return: Основное изображение модели
        :rtype: YMModelPhoto
        """
        return YMModelPhoto(self.data.get('photo'))

    @property
    def photos(self):
        """

        :return: Остальные изображения модели
        :rtype: list[YMModelPhoto]
        """
        return [YMModelPhoto(photo) for photo in self.data.get('photos', [])]

    @property
    def category(self):
        """

        :return: Информация о категории, к которой относится модель
        :rtype: YMCategory
        """
        return YMCategory(self.data.get('category'))

    @property
    def navigationNode(self):
        """

        :return: Информация об узле навигационного дерева, к которому относится модель
        :rtype: YMNavigationNode
        """
        return YMNavigationNode(self.data.get('navigationNode'))

    @property
    def price(self):
        """

        :return: Информация о цене модели в основной валюте запроса
        :rtype: YMPrice
        """
        return YMPrice(self.data.get('price'))

    @property
    def alternatePrice(self):
        """

        :return: Информация о цене модели в альтернативной валюте запроса
        :rtype: YMPrice
        """
        return YMPrice(self.data.get('price'))

    @property
    def vendor(self):
        """

        :return: Информация о производителе модели
        :rtype: YMVendor
        """
        return YMVendor(self.data.get('vendor'))

    @property
    def rating(self):
        """

        :return: Информация о рейтинге модели
        :rtype: YMRating
        """
        return YMRating(self.data.get('rating'))

    @property
    def facts(self):
        """

        :return: Факты о модели
        :rtype: YMFacts
        """
        return YMFacts(self.data.get('facts'))

    @property
    def warning(self):
        """

        :return: Дисклеймер, связанный с моделью
        :rtype: str or None
        """
        return self.data.get('warning')

    @property
    def warnings(self):
        """

        :return: Строковый код дисклеймера
        :rtype: list[YMModelWarning]
        """
        return [YMModelWarning(warning) for warning in self.data.get('warnings', [])]

    @property
    def filters(self):
        """

        :return: Список фильтров, предназначенных для фильтрации моделей/модификаций
        :rtype: list[YMFilter]
        """
        return [YMFilter(f) for f in self.data.get('filters', [])]

    @property
    def modifications(self):
        """

        :return: Список модификаций групповой модели
        :rtype: list[YMModification]
        """
        return [YMModification(modification) for modification in self.data.get('modifications', [])]

    @property
    def specification(self):
        """

        :return: Основные характеристики модели
        :rtype: list[YMSpecification]
        """
        return [YMSpecification(specification) for specification in self.data.get('specification', [])]

    @property
    def parameters(self):
        """

        :return: Параметры модели
        :rtype: list[YMParameter]
        """
        return [YMParameter(parameter) for parameter in self.data.get('parameters', [])]

    @property
    def userRelated(self):
        """

        :return: Информация, касающаяся текущего пользователя
        :rtype: list[YMUserRelated]
        """
        return [YMUserRelated(userrelated) for userrelated in self.data.get('userRelated', [])]


class YMModelReview(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def url(self):
        """

        :return: URL обзорной статьи на модель
        :rtype: str
        """
        return self.data.get('url')

    @property
    def title(self):
        """

        :return: Заголовок обзора на модель
        :rtype: str
        """
        return self.data.get('title')

    @property
    def favIcon(self):
        """

        :return: URL значка веб-сайта с обзором на модель
        :rtype: str
        """
        return self.data.get('favIcon')


class YMOrganization(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('name'))

    @property
    def name(self):
        """

        :return: Юридическое название
        :rtype: str
        """
        return self.data.get('name')

    @property
    def ogrn(self):
        """

        :return: Основной государственный номер регистрации
        :rtype: str
        """
        return self.data.get('ogrn')

    @property
    def address(self):
        """

        :return: Юридический адрес
        :rtype: str
        """
        return self.data.get('address')

    @property
    def postalAddress(self):
        """

        :return: Фактический адрес
        :rtype: str
        """
        return self.data.get('postalAddress')

    @property
    def type(self):
        """

        :return: Тип организации
        :rtype: str
        """
        return self.data.get('type')

    @property
    def contactUrl(self):
        """

        :return: Ссылка на страницу с контактной информацией
        :rtype: str
        """
        return self.data.get('contactUrl')


class YMShop(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор магазина
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование магазина
        :rtype: str
        """
        return self.data.get('name')

    @property
    def domain(self):
        """

        :return: URL, содержащий контактную информацию магазина
        :rtype: str
        """
        return self.data.get('domain')

    @property
    def registered(self):
        """

        :return: Дата регистрации на Маркете
        :rtype: str
        """
        return self.data.get('registered')

    @property
    def opinionUrl(self):
        """

        :return: Ссылка на отзывы о магазине
        :rtype: str
        """
        return self.data.get('opinionUrl')

    @property
    def region(self):
        """

        :return: Домашний регион
        :rtype: YMRegion
        """
        return YMRegion(self.data.get('region'))

    @property
    def rating(self):
        """

        :return: Информация о рейтинге магазина
        :rtype: YMRating
        """
        return YMRating(self.data.get('rating'))

    @property
    def organizations(self):
        """

        :return: Информация об организации
        :rtype: list[YMOrganization]
        """
        return [YMOrganization(organization) for organization in self.data.get('organizations', [])]


class YMPhone(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('number'))

    @property
    def number(self):
        """

        :return: Значение номера телефона в произвольном формате
        :rtype: str
        """
        return self.data.get('number')

    @property
    def sanitized(self):
        """

        :return: Значение номера телефона в числовом формате
        :rtype: str
        """
        return self.data.get('sanitized')

    @property
    def call(self):
        """

        :return: Ссылка для получения номера телефона
        :rtype: str or None
        """
        return self.data.get('call')


class YMDeliveryOptionService(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        """

        :return: Идентификатор службы доставки
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование службы доставки
        :rtype: str
        """
        return self.data.get('name')


class YMDeliveryOptionConditions(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def price(self):
        """

        :return: Стоимость доставки в основной валюте
        :rtype: YMShopPrice
        """
        return YMShopPrice(self.data.get('price'))

    @property
    def alternatePrice(self):
        """

        :return: Стоимость доставки в альтернативной валюте
        :rtype: YMShopPrice
        """
        return YMShopPrice(self.data.get('alternatePrice'))

    @property
    def daysFrom(self):
        """

        :return: Определяет начало периода (день недели), в котором возможна доставка
        :rtype: int
        """
        return self.data.get('daysFrom')

    @property
    def daysTo(self):
        """

        :return: Определяет окончание периода (день недели), в котором возможна доставка
        :rtype: int
        """
        return self.data.get('daysTo')

    @property
    def orderBefore(self):
        """

        :return: Время, до которого нужно сделать заказ в часовом поясе пользователя. Возможные значения - от 0 до 23. Отсутствие параметра - заказ можно делать в любое время
        :rtype: int
        """
        return self.data.get('orderBefore')

    @property
    def deliveryIncluded(self):
        """

        :return: Признак, что стоимость доставки включена в стоимость товарного предложения. Отсутствие свойства в ввыдаче равнозначно значению false.
        :rtype: bool
        """
        return self.data.get('deliveryIncluded')


class YMDeliveryOption(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def brief(self):
        """

        :return: Краткое описание условий доставки
        :rtype: str
        """
        return self.data.get('brief')

    @property
    def service(self):
        """

        :return: Информация о службе доставки
        :rtype: YMDeliveryOptionService
        """
        return YMDeliveryOptionService(self.data.get('service'))

    @property
    def conditions(self):
        """

        :return: Информация об условиях доставки
        :rtype: YMDeliveryOptionConditions
        """
        return YMDeliveryOptionConditions(self.data.get('conditions'))


class YMDeliveryPickupOption(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def brief(self):
        """

        :return: Краткое описание условий доставки
        :rtype: str
        """
        return self.data.get('brief')

    @property
    def outletCount(self):
        """

        :return: Количество пунктов выдачи и торговых залов, в которых можно забрать заказ
        :rtype: int
        """
        return self.data.get('outletCount')

    @property
    def service(self):
        """

        :return: Информация о службе доставки
        :rtype: YMDeliveryOptionService
        """
        return YMDeliveryOptionService(self.data.get('service'))

    @property
    def conditions(self):
        """

        :return: Информация об условиях доставки
        :rtype: YMDeliveryOptionConditions
        """
        return YMDeliveryOptionConditions(self.data.get('conditions'))


class YMDelivery(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def free(self):
        """

        :return: Признак бесплатной доставки
        :rtype: bool
        """
        return self.data.get('free')

    @property
    def deliveryIncluded(self):
        """

        :return: Признак, что цена доставки включена в стоимость товара
        :rtype: bool
        """
        return self.data.get('deliveryIncluded')

    @property
    def carried(self):
        """

        :return: Признак наличия доставки
        :rtype: bool
        """
        return self.data.get('carried')

    @property
    def pickup(self):
        """

        :return: Признак возможности самовывоза заказа
        :rtype: bool
        """
        return self.data.get('pickup')

    @property
    def downloadable(self):
        """

        :return: Признак, что товар можно скачать
        :rtype: bool
        """
        return self.data.get('downloadable')

    @property
    def localStore(self):
        """

        :return: Признак наличия торгового зала в регионе пользователя
        :rtype: bool
        """
        return self.data.get('localStore')

    @property
    def localDelivery(self):
        """

        :return: Признак локальной доставки
        :rtype: bool
        """
        return self.data.get('localDelivery')

    @property
    def brief(self):
        """

        :return: Краткое описание условий доставки
        :rtype: str
        """
        return self.data.get('brief')

    @property
    def inStock(self):
        """

        :return: Признак наличия товара
        :rtype: bool
        """
        return self.data.get('inStock')

    @property
    def is_global(self):
        """

        :return: Признак трансграничной доставки
        :rtype: bool
        """
        return self.data.get('global')

    @property
    def price(self):
        """

        :return: Стоимость доставки в валюте заказа
        :rtype: YMShopPrice
        """
        return YMShopPrice(self.data.get('price'))

    @property
    def alternatePrice(self):
        """

        :return: Стоимость доставки в альтернативной или неденоминированной валюте
        :rtype: YMShopPrice
        """
        return YMShopPrice(self.data.get('alternatePrice'))

    @property
    def shopRegion(self):
        """

        :return: Свой регион магазина
        :rtype: YMRegion
        """
        return YMRegion(self.data.get('shopRegion'))

    @property
    def userRegion(self):
        """

        :return: Регион пользователя
        :rtype: YMRegion
        """
        return YMRegion(self.data.get('userRegion'))

    @property
    def description(self):
        """

        :return: Описание условий доставки
        :rtype: str or None
        """
        return self.data.get('description')

    @property
    def options(self):
        """

        :return: Информация о службах доставки, с которыми сотрудничает магазин
        :rtype: list[YMDeliveryOption]
        """
        return [YMDeliveryOption(option) for option in self.data.get('options', [])]

    @property
    def pickupOptions(self):
        """

        :return: Информация об условиях самовывоза
        :rtype: list[YMDeliveryPickupOption]
        """
        return [YMDeliveryPickupOption(option) for option in self.data.get('pickupOptions', [])]


class YMPaymentOption(YMBase):

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def canPayByCard(self):
        """

        :return: Оплата картой на Маркете
        :rtype: bool
        """
        return self.data.get('canPayByCard')


class YMOffer(YMBase):

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор предложения
        :rtype: str
        """
        return self.data.get('id')

    @property
    def wareMd5(self):
        """

        :return: MD5 хеш-код предложения
        :rtype: str
        """
        return self.data.get('wareMd5')

    @property
    def name(self):
        """

        :return: Название предложения
        :rtype: str
        """
        return self.data.get('name')

    @property
    def promocode(self):
        """

        :return: Признак, что товар можно купить с промокодом
        :rtype: bool or None
        """
        return self.data.get('promocode')

    @property
    def cpa(self):
        """

        :return: Признак, что товар можно заказать на Яндекс.Маркете (в рамках программы «Заказ на Маркете»)
        :rtype: bool or None
        """
        return self.data.get('cpa')

    @property
    def url(self):
        """

        :return: URL товара на сайте магазина
        :rtype: str
        """
        return self.data.get('url')

    @property
    def cpaUrl(self):
        """

        :return: URL карточки модели на Яндекс.Маркете
        :rtype: str or None
        """
        return self.data.get('cpaUrl')

    @property
    def outletUrl(self):
        """

        :return: URL карты со списком точек выдачи товара
        :rtype: str or None
        """
        return self.data.get('outletUrl')

    @property
    def adult(self):
        """

        :return: Признак, что предложение относится к интим-категории (18+)
        :rtype: bool or None
        """
        return self.data.get('adult')

    @property
    def age(self):
        """

        :return: Возрастные ограничения для предложения
        :rtype: str or None
        """
        return self.data.get('age')

    @property
    def onStock(self):
        """

        :return: Признак наличия товара
        :rtype: bool or None
        """
        return self.data.get('onStock')

    @property
    def outletCount(self):
        """

        :return: Количество точек выдачи
        :rtype: int
        """
        return self.data.get('outletCount')

    @property
    def pickupCount(self):
        """

        :return: Количество точек самовывоза
        :rtype: int
        """
        return self.data.get('pickupCount')

    @property
    def localStoreCount(self):
        """

        :return: Количество торговых залов в регионе пользователя
        :rtype: int
        """
        return self.data.get('localStoreCount')

    @property
    def warranty(self):
        """

        :return: Признак наличия гарантии производителя
        :rtype: bool
        """
        return self.data.get('warranty')

    @property
    def recommended(self):
        """

        :return: Признак наличия рекомендации производителя
        :rtype: bool
        """
        return self.data.get('recommended')

    @property
    def link(self):
        """

        :return: URL предложения на Яндекс.Маркете
        :rtype: str or None
        """
        return self.data.get('link')

    @property
    def cartLink(self):
        """

        :return: URL для добавления предложения в корзину на Яндекс.Маркете
        :rtype: str or None
        """
        return self.data.get('cartLink')

    @property
    def offersLink(self):
        """

        :return: URL предложений на модификации модели в указанном магазине
        :rtype: str or None
        """
        return self.data.get('offersLink')

    @property
    def variationCount(self):
        """

        :return: Количество других предложений на указанный товар в магазине
        :rtype: int or None
        """
        return self.data.get('variationCount')

    @property
    def description(self):
        """

        :return: Описание предложения
        :rtype: str
        """
        return self.data.get('description')

    @property
    def price(self):
        """

        :return: Информация о цене
        :rtype: YMShopPrice
        """
        return YMShopPrice(self.data.get('price'))

    @property
    def alternatePrice(self):
        """

        :return: Информация о цене в альтернативной валюте
        :rtype: YMShopPrice
        """
        return YMShopPrice(self.data.get('alternatePrice'))

    @property
    def shop(self):
        """

        :return: Информация о магазине, который разместил предложение
        :rtype: YMShop
        """
        return YMShop(self.data.get('shop'))

    @property
    def model(self):
        """

        :return: Идентификатор модели
        :rtype: int or None
        """
        return self.data.get('model', {}).get('id')

    @property
    def phone(self):
        """

        :return: Номер телефона магазина
        :rtype: YMPhone
        """
        return YMPhone(self.data.get('phone'))

    @property
    def photos(self):
        """

        :return: Изображения товара
        :rtype: list[YMModelPhoto]
        """
        return [YMModelPhoto(photo) for photo in self.data.get('photos', [])]

    @property
    def photo(self):
        """

        :return: Основное изображение товара
        :rtype: YMModelPhoto
        """
        return YMModelPhoto(self.data.get('photo'))

    @property
    def previewPhotos(self):
        """

        :return: Уменьшенные изображения товара
        :rtype: list[YMModelPhoto]
        """
        return [YMModelPhoto(photo) for photo in self.data.get('previewPhotos', [])]

    @property
    def activeFilters(self):
        """

        :return: Параметры модели, по которым можно отфильтровать предложения на нее в поиске Яндекс.Маркета
        :rtype: list[YMFilter]
        """
        return [YMFilter(f) for f in self.data.get('activeFilters', [])]

    @property
    def delivery(self):
        """

        :return: Информация о доставке
        :rtype: YMDelivery
        """
        return YMDelivery(self.data.get('delivery'))

    @property
    def category(self):
        """

        :return: Информация о категории предложения
        :rtype: YMCategory
        """
        return YMCategory(self.data.get('category'))

    @property
    def vendor(self):
        """

        :return: Информация о производителе
        :rtype: YMVendor
        """
        return YMVendor(self.data.get('vendor'))

    @property
    def warning(self):
        """

        :return: Предупреждение, связанное с предложением
        :rtype: str or None
        """
        return self.data.get('warning')

    @property
    def warnings(self):
        """

        :return: Код предупреждения, связанного с предложением
        :rtype: list[YMModelWarning]
        """
        return [YMModelWarning(warn) for warn in self.data.get('warnings', [])]

    @property
    def paymentOptions(self):
        """

        :return: Способы оплаты товара
        :rtype: YMPaymentOption
        """
        return YMPaymentOption(self.data.get('paymentOptions'))


class YMStatisticsRegion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        """

        :return: Идентификатор региона
        :rtype: int
        """
        return self.data.get('id')

    @property
    def offerCount(self):
        """

        :return: Количество товарных предложений модели в регионе
        :rtype: int
        """
        return self.data.get('offerCount')

    @property
    def price_max(self):
        """

        :return: Максимальная цена
        :rtype: str
        """
        return self.data.get('price', {}).get('price_max')

    @property
    def price_min(self):
        """

        :return: Минимальная цена
        :rtype: str
        """
        return self.data.get('price', {}).get('price_min')

    @property
    def price_median(self):
        """

        :return: Медиана по ценам
        :rtype: str
        """
        return self.data.get('price', {}).get('price_median')


class YMStatistics(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def regions(self):
        """

        :return: Список статистик по регионам
        :rtype: list[YMStatisticsRegion]
        """
        return [YMStatisticsRegion(region) for region in self.data.get('regions', [])]


class YMOpinionAuthorSocial(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def type(self):
        """

        :return: Тип профиля
        :rtype: str
        """
        return self.data.get('type')

    @property
    def url(self):
        """

        :return: Ссылка на профиль
        :rtype: str
        """
        return self.data.get('url')


class YMOpinionAuthor(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def name(self):
        """

        :return: Имя автора
        :rtype: str or None
        """
        return self.data.get('name')

    @property
    def avatarUrl(self):
        """

        :return: Ссылка на аватар
        :rtype: str or None
        """
        return self.data.get('avatarUrl')

    @property
    def grades(self):
        """

        :return: Количество оценок
        :rtype: int or None
        """
        return self.data.get('grades')

    @property
    def visibility(self):
        """

        :return: Вариант отображения отзыва
        :rtype: str
        """
        return self.data.get('visibility')

    @property
    def social(self):
        """

        :return: Оиформация о профилях автора в социальных сетях
        :rtype: list[YMOpinionAuthorSocial]
        """
        return [YMOpinionAuthorSocial(social) for social in self.data.get('social', [])]


class YMModelOpinionUser(YMBase):
    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор автора комментария
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Имя автора комментария
        :rtype: str
        """
        return self.data.get('name')


class YMOpinionComment(YMBase):
    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.data.get('id'))

    @property
    def id(self):
        """

        :return: Идентификатор комментария
        :rtype: str
        """
        return self.data.get('id')

    @property
    def rootId(self):
        """

        :return: Идентификатор корневого объекта, к которому относится комментарий
        :rtype: str
        """
        return self.data.get('rootId')

    @property
    def parentId(self):
        """

        :return: Идентификатор родительского комментария или корневого объекта в дереве комментариев
        :rtype: str
        """
        return self.data.get('parentId')

    @property
    def title(self):
        """

        :return: Заголовок комментария
        :rtype: str
        """
        return self.data.get('title')

    @property
    def updateTimestamp(self):
        """

        :return: Timestamp времени последнего обновления комментария
        :rtype: int
        """
        return self.data.get('updateTimestamp')

    @property
    def valid(self):
        """

        :return: Комментарий действителен
        :rtype: bool
        """
        return self.data.get('valid')

    @property
    def deleted(self):
        """

        :return: Признак удаленного комментария
        :rtype: bool
        """
        return self.data.get('deleted')

    @property
    def blocked(self):
        """

        :return: Комментарий заблокирован
        :rtype: bool
        """
        return self.data.get('blocked')

    @property
    def sticky(self):
        """

        :return: Признак прикрепленного комментария
        :rtype: bool
        """
        return self.data.get('sticky')

    @property
    def body(self):
        """

        :return: Текст комментария
        :rtype: str
        """
        return self.data.get('body')

    @property
    def user(self):
        """

        :return: Информация об авторе комментария
        :rtype: YMModelOpinionUser
        """
        return YMModelOpinionUser(self.data.get('user'))

    @property
    def children(self):
        """

        :return: Список дочерних комментариев к данному в дереве комментариев
        :rtype: list[YMOpinionComment]
        """
        return [YMOpinionComment(comment) for comment in self.data.get('children', [])]


class YMModelOpinionModel(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

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
        :rtype: str or None
        """
        return self.data.get('name')


class YMModelOpinionShop(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        """

        :return: Идентификатор магазина
        :rtype: int
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование магазина
        :rtype: str
        """
        return self.data.get('name')


class YMOpinion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        """

        :return: Идентификатор отзыва
        :rtype: int
        """
        return self.data.get('id')

    @property
    def date(self):
        """

        :return: Дата написания
        :rtype: str
        """
        return self.data.get('date')

    @property
    def vote(self):
        """

        :return: Мнение текущего пользователя об отзыве
        :rtype: bool or None
        """
        return self.data.get('vote')

    @property
    def grade(self):
        """

        :return: Оценка
        :rtype: int
        """
        return self.data.get('grade')

    @property
    def rejectReason(self):
        """

        :return: Причина отклонения отзыва
        :rtype: str or None
        """
        return self.data.get('rejectReason')

    @property
    def state(self):
        """

        :return: Статус отзыва
        :rtype: str or None
        """
        return self.data.get('state')

    @property
    def agreeCount(self):
        """

        :return: Количество согласных с оценкой
        :rtype: int
        """
        return self.data.get('agreeCount')

    @property
    def disagreeCount(self):
        """

        :return: Количество несоглазных с оценкой
        :rtype: int
        """
        return self.data.get('disagreeCount')

    @property
    def text(self):
        """

        :return: Текст отзыва
        :rtype: str or None
        """
        return self.data.get('text')

    @property
    def pros(self):
        """

        :return: Описание достоинств
        :rtype: str or None
        """
        return self.data.get('pros')

    @property
    def cons(self):
        """

        :return: Описание недостатков
        :rtype: str or None
        """
        return self.data.get('cons')

    @property
    def author(self):
        """

        :return: Информация об авторе
        :rtype: YMOpinionAuthor
        """
        return YMOpinionAuthor(self.data.get('author'))

    @property
    def comments(self):
        """

        :return: Комментарии
        :rtype: list[YMOpinionComment]
        """
        return [YMOpinionComment(comment) for comment in self.data.get('comments', [])]

    @property
    def region(self):
        """

        :return: Регион
        :rtype: YMRegion
        """
        return YMRegion(self.data.get('region'))


class YMModelOpinion(YMOpinion):

    @property
    def usageTime(self):
        """

        :return: Время использования модели
        :rtype: str
        """
        return self.data.get('usageTime')

    @property
    def verifiedBuyer(self):
        """

        :return: Признак проверенного покупателя
        :rtype: bool
        """
        return self.data.get('verifiedBuyer')

    @property
    def model(self):
        """

        :return: Модель
        :rtype: YMModelOpinionModel
        """
        return YMModelOpinionModel(self.data.get('model'))


class YMShopOpinion(YMOpinion):

    @property
    def shopOrderId(self):
        """

        :return: Идентификатор заказа, относящегося к отзыву
        :rtype: str or None
        """
        return self.data.get('shopOrderId')

    @property
    def delivery(self):
        """

        :return: Способ покупки
        :rtype: str
        """
        return self.data.get('delivery')

    @property
    def problem(self):
        """

        :return: Статус решения проблемы пользователя
        :rtype: str or None
        """
        return self.data.get('problem')

    @property
    def shop(self):
        """

        :return: Магазин
        :rtype: YMModelOpinionShop
        """
        return YMModelOpinionShop(self.data.get('model'))


class YMAddress(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def regionId(self):
        """

        :return: Идентификатор региона, к которому относится данный адрес
        :rtype: int
        """
        return self.data.get('regionId')

    @property
    def type(self):
        """

        :return: Тип региона, к которому относится данный адрес
        :rtype: str or None
        """
        return self.data.get('type')

    @property
    def country(self):
        """

        :return: Наименование страны
        :rtype: str or None
        """
        return self.data.get('country')

    @property
    def region(self):
        """

        :return: Наименование региона
        :rtype: str or None
        """
        return self.data.get('region')

    @property
    def subRegion(self):
        """

        :return: Район внутри области
        :rtype: str or None
        """
        return self.data.get('subRegion')

    @property
    def locality(self):
        """

        :return: Наименование города, поселка, деревни и тд
        :rtype: str
        """
        return self.data.get('locality')

    @property
    def subLocality(self):
        """

        :return: Наименование района
        :rtype: str or None
        """
        return self.data.get('subLocality')

    @property
    def thoroughfare(self):
        """

        :return: Улица, проспект, км шоссе и тд
        :rtype: str
        """
        return self.data.get('thoroughfare')

    @property
    def premiseNumber(self):
        """

        :return: Номер дома, строение, участка и тд
        :rtype: str or None
        """
        return self.data.get('premiseNumber')

    @property
    def fullAddress(self):
        """

        :return: Полный адрес
        :rtype: str
        """
        return self.data.get('fullAddress')

    @property
    def block(self):
        """

        :return: Корпус
        :rtype: str or None
        """
        return self.data.get('block')

    @property
    def wing(self):
        """

        :return: Строение
        :rtype: str or None
        """
        return self.data.get('wing')

    @property
    def estate(self):
        """

        :return: Владение
        :rtype: str or None
        """
        return self.data.get('estate')

    @property
    def entrance(self):
        """

        :return: Подъезд
        :rtype: str or None
        """
        return self.data.get('entrance')

    @property
    def floor(self):
        """

        :return: Этаж
        :rtype: str or None
        """
        return self.data.get('floor')

    @property
    def room(self):
        """

        :return: Комната, офис
        :rtype: str or None
        """
        return self.data.get('room')

    @property
    def note(self):
        """

        :return: Примечание
        :rtype: str or None
        """
        return self.data.get('note')

    @property
    def distance(self):
        """

        :return: Расстояние
        :rtype: float or None
        """
        return self.data.get('geoPoint').get('distance')

    @property
    def latitude(self):
        """

        :return: Широта
        :rtype: float
        """
        return self.data.get('geoPoint', {}).get('coordinates', {}).get('latitude')

    @property
    def longitude(self):
        """

        :return: Долгота
        :rtype: float
        """
        return self.data.get('geoPoint', {}).get('coordinates', {}).get('longitude')

    @property
    def postcode(self):
        """

        :return: Почтовый индекс
        :rtype: str or None
        """
        return self.data.get('postcode')


class YMSchedule(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def daysFrom(self):
        """

        :return: День недели, определяет начало периода работы в рамках недели
        :rtype: str
        """
        return self.data.get('daysFrom')

    @property
    def daysTill(self):
        """

        :return: День недели, определяет окончание периода работы в рамках недели
        :rtype: str
        """
        return self.data.get('daysTill')

    @property
    def timeFrom(self):
        """

        :return: Время суток, определяет начало периода работы в рамках дня
        :rtype: str
        """
        return self.data.get('from')

    @property
    def timeTill(self):
        """

        :return: Время суток, определяет окончание периода работы в рамках дня
        :rtype: str
        """
        return self.data.get('till')


class YMOutlet(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def id(self):
        """

        :return: Идентификатор торговой точки / пункта выдачи товара
        :rtype: str
        """
        return self.data.get('id')

    @property
    def name(self):
        """

        :return: Наименование торговой точки / пункта выдачи товара
        :rtype: str
        """
        return self.data.get('name')

    @property
    def type(self):
        """

        :return: Тип торговой точки / пункта выдачи товара
        :rtype: str
        """
        return self.data.get('type')

    @property
    def shop(self):
        """

        :return: Информация о магазине, осуществляющем выдачу товара в данной торговой точке
        :rtype: YMShop
        """
        return YMShop(self.data.get('shop'))

    @property
    def phones(self):
        """

        :return: Список телефонов торговой точки / пункта выдачи товара
        :rtype: list[YMPhone]
        """
        return [YMPhone(phone) for phone in self.data.get('phones', [])]

    @property
    def address(self):
        """

        :return: Адрес торговой точки / пункта выдачи товара
        :rtype: YMAddress
        """
        return YMAddress(self.data.get('address'))

    @property
    def schedule(self):
        """

        :return: Расписание работы торговой точки / пункта выдачи товара
        :rtype: list[YMSchedule]
        """
        return [YMSchedule(s) for s in self.data.get('schedule', [])]

    @property
    def distance(self):
        """

        :return: Расстояние
        :rtype: float or None
        """
        return self.data.get('geoPoint', {}).get('distance')

    @property
    def latitude(self):
        """

        :return: Широта
        :rtype: float or None
        """
        return self.data.get('geoPoint', {}).get('coordinates', {}).get('latitude')

    @property
    def longitude(self):
        """

        :return: Долгота
        :rtype: float or None
        """
        return self.data.get('geoPoint', {}).get('coordinates', {}).get('longitude')

    @property
    def offer(self):
        """

        :return: Товарное предложение в контексте запроса
        :rtype: YMOffer
        """
        return YMOffer(self.data.get('offer'))


class YMRedirect(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def type(self):
        """

        :return: Тип редиректа
        :rtype: str
        """
        return self.data.get('type')

    @property
    def queryText(self):
        """

        :return: Текст оригинального запроса на редирект
        :rtype: str
        """
        return self.data.get('queryText')

    @property
    def link(self):
        """

        :return: Ссылка на данный редирект, направляющая на Яндекс.Маркет
        :rtype: str
        """
        return self.data.get('link')


class YMRedirectModel(YMRedirect):

    @property
    def model(self):
        """

        :return: Информация о модели
        :rtype: YMModel
        """
        return YMModel(self.data.get('content').get('model'))

    @property
    def model_id(self):
        """

        :return: Идентификатор модели
        :rtype: int
        """
        return self.data.get('model',{}).get('id')


class YMRedirectCatalog(YMRedirect):

    @property
    def items(self):
        """

        :return: Список моделей и/или товарных предложений
        :rtype: list[YMModel or YMOffer]
        """
        return [YMModel(item) if 'model' in item.keys() else YMOffer(item) for item in
                self.data['content'].get('items', [])]

    @property
    def categories(self):
        """

        :return: Список категорий
        :rtype: list[YMSearchCategory]
        """
        return [YMSearchCategory(category) for category in self.data.get('categories', [])]

    @property
    def filters(self):
        """

        :return: Фильтры
        :rtype: list[YMFilter]
        """
        return [YMFilter(f) for f in self.data.get('filters', [])]

    @property
    def sorts(self):
        """

        :return: Сортировки
        :rtype: list[YMSort]
        """
        return [YMSort(sort) for sort in self.data.get('sorts', [])]

    @property
    def navigationNode(self):
        """

        :return: Краткая информация об узле навигационного дерева
        :rtype: YMNavigationNode
        """
        return YMNavigationNode(self.data.get('navigationNode'))

    @property
    def criteria(self):
        """

        :return: Список условий фильтрации, уточняющих поиск
        :rtype: list[YMDatasourceCriteria]
        """
        return [YMDatasourceCriteria(c) for c in self.data.get('criteria', [])]


class YMRedirectVendor(YMRedirect):

    @property
    def vendor(self):
        """

        :return: Производитель
        :rtype: YMVendor
        """
        return YMVendor(self.data.get('content').get('vendor'))

    @property
    def vendor_id(self):
        """

        :return: Идентификатор производителя
        :rtype: int
        """
        return self.data.get('vendor',{}).get('id')


class YMRedirectSearch(YMRedirect):

    # @property
    # def items(self):
    #     """
    #
    #     :return: Список моделей и/или товарных предложений
    #     :rtype: list[YMModel or YMOffer]
    #     """
    #     return [YMModel(item) if 'model' in item.keys() else YMOffer(item) for item in
    #             self.data['content'].get('items', [])]

    @property
    def filters(self):
        """

        :return: Фильтры
        :rtype: list[YMFilter]
        """
        return [YMFilter(f) for f in self.data.get('filters', [])]

    @property
    def sorts(self):
        """

        :return: Сортировки
        :rtype: list[YMSort]
        """
        return [YMSort(sort) for sort in self.data.get('sorts', [])]

    @property
    def criteria(self):
        """

        :return: Список условий фильтрации, уточняющих поиск
        :rtype: list[YMDatasourceCriteria]
        """
        return [YMDatasourceCriteria(c) for c in self.data.get('criteria', [])]


class YMSuggestion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def value(self):
        """

        :return: Значение поисковой подсказки
        :rtype: str
        """
        return self.data.get('value')

    @property
    def url(self):
        """

        :return: Ссылка на страницу соответствующую поисковой посдказке
        :rtype: str or None
        """
        return self.data.get('url')


class YMSuggestionCompletion(YMBase):
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @property
    def completion(self):
        """

        :return: Завершение фразы
        :rtype: str
        """
        return self.data.get('completion')

    @property
    def value(self):
        """

        :return: Фраза целиком после завершения
        :rtype: str
        """
        return self.data.get('value')
