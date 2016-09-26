from abc import ABCMeta, abstractmethod, abstractproperty
from functools import wraps
import inspect
from collections import namedtuple
from copy import deepcopy

class TagSet(namedtuple('TagSet', 'add remove blocked_by blocks if_present')):
    def __new__(cls, add=None, remove=None, blocked_by=None, blocks=None, if_present=None):
        return super(TagSet, cls).__new__(cls, add or set(),
                                               remove or set(),
                                               blocked_by or set(),
                                               blocks or set(),
                                               if_present or set())

def astro_data_descriptor(fn):
    fn.descriptor_method = True
    return fn

def descriptor_list(ad):
    members = inspect.getmembers(ad, lambda x: hasattr(x, 'descriptor_method'))
    return tuple(mname for (mname, method) in members)

def astro_data_tag(fn):
    @wraps(fn)
    def wrapper(self):
        try:
            ret = fn(self)
            if ret is not None:
                if not isinstance(ret, TagSet):
                    raise TypeError("Tag function {} didn't return a TagSet".format(fn.__name__))

                return TagSet(*tuple(set(s) for s in ret))
        except KeyError:
            pass

        # Return empty TagSet for the "doesn't apply" case
        return TagSet()

    wrapper.tag_method = True
    return wrapper

class AstroDataError(Exception):
    pass

class DataProvider(object):
    __metaclass__ = ABCMeta
    @abstractproperty
    def header(self):
        pass

#    @abstractproperty
#    def data(self):
#        pass

    @abstractmethod
    def append(self, ext):
        pass

    @abstractmethod
    def __getitem__(self, slice):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __iadd__(self, oper):
        pass

    @abstractmethod
    def __isub__(self, oper):
        pass

    @abstractmethod
    def __imul__(self, oper):
        pass

    @abstractmethod
    def __idiv__(self, oper):
        pass

    @property
    def exposed(self):
        return ()

    @abstractproperty
    def data(self):
        pass

    @abstractproperty
    def uncertainty(self):
        pass

def simple_descriptor_mapping(**kw):
    def decorator(cls):
        for descriptor, descriptor_def in kw.items():
            setattr(cls, descriptor, property(descriptor_def))
        return cls
    return decorator

class AstroData(object):
    def __init__(self, provider):
        if not isinstance(provider, DataProvider):
            raise ValueError("AstroData is initialized with a DataProvider object. You may want to use ad.open('...') instead")
        self._dataprov = provider
        self._processing_tags = False

    def __process_tags(self):
        try:
            # This prevents infinite recursion
            if self._processing_tags:
                return set()
            self._processing_tags = True
            try:
                results = []
                for mname, method in inspect.getmembers(self, lambda x: hasattr(x, 'tag_method')):
                    ts = method()
                    plus, minus, blocked_by, blocks, if_present = ts
                    if plus or minus or blocks:
                        results.append(ts)

                # Sort by the length of substractions... those that substract from others go first
                results = sorted(results, key=lambda x: len(x.remove) + len(x.blocks), reverse=True)
                # Sort by length of blocked_by... those that are never disabled go first
                results = sorted(results, key=lambda x: len(x.blocked_by))
                # Sort by length of if_present... those that need other tags to be present go last
                results = sorted(results, key=lambda x: len(x.if_present))

                tags = set()
                removals = set()
                blocked = set()
                for plus, minus, blocked_by, blocks, is_present in results:
                    if is_present:
                        # If this TagSet requires other tags to be present, make sure that all of
                        # them are. Otherwise, skip...
                        if len(tags & is_present) != len(is_present):
                            continue
                    allowed = (len(tags & blocked_by) + len(plus & blocked)) == 0
                    if allowed:
                        # This set is not being blocked by others...
                        removals.update(minus)
                        tags.update(plus - removals)
                        blocked.update(blocks)
            finally:
                self._processing_tags = False

            return tags
        except AttributeError as e:
            return set()

    @property
    def tags(self):
        return self.__process_tags()

    @property
    def nddata(self):
        return self._dataprov.nddata

    @property
    def data(self):
        return self._dataprov.data

    @property
    def uncertainty(self):
        return self._dataprov.uncertainty

    @uncertainty.setter
    def uncertainty(self, value):
        self._dataprov.uncertainty = value

    @property
    def table(self):
        return self._dataprov.table

    def __getitem__(self, slicing):
        return self.__class__(self._dataprov[slicing])

    def __delitem__(self, idx):
        del self._dataprov[idx]

    def __getattr__(self, attribute):
        try:
            return getattr(self._dataprov, attribute)
        except AttributeError:
            clsname = self.__class__.__name__
            raise AttributeError("{!r} object has no attribute {!r}".format(clsname, attribute))

    def __contains__(self, attribute):
        return attribute in self._dataprov.exposed

    def __len__(self):
        return len(self._dataprov)

    @abstractmethod
    def info(self):
        pass

    def __add__(self, oper):
        copy = deepcopy(self)
        copy += oper
        return copy

    def __sub__(self, oper):
        copy = deepcopy(self)
        copy += oper
        return copy

    def __mul__(self, oper):
        copy = deepcopy(self)
        copy *= oper
        return copy

    def __div__(self, oper):
        copy = deepcopy(self)
        copy /= oper
        return copy

    def __iadd__(self, oper):
        self._dataprov += oper
        return self

    def __isub__(self, oper):
        self._dataprov -= oper
        return self

    def __imul__(self, oper):
        self._dataprov *= oper
        return self

    def __idiv__(self, oper):
        self._dataprov /= oper
        return self

    add = __iadd__
    subtract = __isub__
    multiply = __imul__
    divide = __idiv__

    def append(self, extension):
        self._dataprov.append(extension)
