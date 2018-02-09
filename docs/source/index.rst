YMContent
=========

Просто установить:

   pip3 install YMContent


Просто использовать:

   >>> from YMContent import YMAPI
   >>> api = YMAPI('SuperSecretToken')
   >>> a = api.model('1732210983', geo_id=213, fields='ALL')
   >>> a.model.name
   Смартфон Apple iPhone X 256GB
   >>> a.model.description
   GSM, LTE-A, смартфон, iOS 11, вес 174 г, ШхВхТ 70.9x143.6x7.7 мм, экран 5.8", 2436x1125, Bluetooth, NFC, Wi-Fi, GPS, ГЛОНАСС, фотокамера 12 МП, память 256 Гб
   >>> a.model.price.json()
   {'max': '92930', 'min': '72290', 'avg': '77499'}

Список доступных методов:
-------------------------

.. currentmodule:: YMContent

.. autosummary::
        ~YMContent.YMAPI.categories
        ~YMContent.YMAPI.categories_children
        ~YMContent.YMAPI.category
        ~YMContent.YMAPI.categories_filters
        ~YMContent.YMAPI.categories_match
        ~YMContent.YMAPI.model
        ~YMContent.YMAPI.models_reviews
        ~YMContent.YMAPI.models_match
        ~YMContent.YMAPI.models_lookas
        ~YMContent.YMAPI.categories_bestdeals
        ~YMContent.YMAPI.categories_popular
        ~YMContent.YMAPI.model_offers
        ~YMContent.YMAPI.model_offers_default
        ~YMContent.YMAPI.model_offers_stat
        ~YMContent.YMAPI.model_offers_filters
        ~YMContent.YMAPI.offer
        ~YMContent.YMAPI.model_opinions
        ~YMContent.YMAPI.shop_opinions
        ~YMContent.YMAPI.shop
        ~YMContent.YMAPI.shops
        ~YMContent.YMAPI.geo_regions_shops_summary
        ~YMContent.YMAPI.model_outlets
        ~YMContent.YMAPI.shop_outlets
        ~YMContent.YMAPI.offer_outlets
        ~YMContent.YMAPI.geo_regions
        ~YMContent.YMAPI.geo_regions_children
        ~YMContent.YMAPI.geo_region
        ~YMContent.YMAPI.geo_suggest
        ~YMContent.YMAPI.vendors
        ~YMContent.YMAPI.vendor
        ~YMContent.YMAPI.vendors_match
        ~YMContent.YMAPI.search
        ~YMContent.YMAPI.categories_search
        ~YMContent.YMAPI.search_filters
        ~YMContent.YMAPI.redirect
        ~YMContent.YMAPI.suggestions


:ref:`genindex`

.. toctree::

   YMContent
