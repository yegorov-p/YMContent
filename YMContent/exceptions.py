# -*- coding: utf-8 -*-
class NetworkAPIError(BaseException):
    pass

class BaseAPIError(BaseException):
    pass


class FieldsParamError(BaseException):
    pass


class OutletTypesParamError(BaseException):
    pass


class NotAuthorized(BaseException):
    pass


class GroupByParamError(BaseException):
    pass


class HowParamError(BaseException):
    pass


class MatchTypeParamError(BaseException):
    pass


class TypeParamError(BaseException):
    pass


class ResultTypeParamError(BaseException):
    pass


class RedirectTypesParamError(BaseException):
    pass


class SuggestTypesParamError(BaseException):
    pass


class SearchTypeParamError(BaseException):
    pass


class FilterSetParamError(BaseException):
    pass


class SortParamError(BaseException):
    pass


class GradeParamError(BaseException):
    pass


class CountParamError(BaseException):
    pass


class PosParamError(BaseException):
    pass


class PageParamError(BaseException):
    pass


class GeoParamError(BaseException):
    pass


class DeliveryIncludedParamError(BaseException):
    pass


class OnstockParamError(BaseException):
    pass


class WarrantyParamError(BaseException):
    pass


class NoGeoIdOrIP(BaseException):
    pass
