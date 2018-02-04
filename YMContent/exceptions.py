# -*- coding: utf-8 -*-
class BaseAPIError(BaseException):
    pass


class FieldsParamError(BaseException):
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


class PageParamError(BaseException):
    pass


class GeoParamError(BaseException):
    pass


class NoGeoIdOrIP(BaseException):
    pass