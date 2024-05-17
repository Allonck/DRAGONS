from functools import wraps
from gempy.utils import logutils
import inspect

LOGINDENT = 0
log = logutils.get_logger(__name__)

def set_logging(pname):
    global LOGINDENT
    LOGINDENT += 1
    logutils.update_indent(LOGINDENT)
    stat_msg = "PRIMITIVE: {}".format(pname)
    log.status(stat_msg)
    log.status("-" * len(stat_msg))
    return

def unset_logging():
    global LOGINDENT
    log.status(".")
    LOGINDENT -= 1
    logutils.update_indent(LOGINDENT)
    return

def log_adjust(fn):
    @wraps(fn)
    def gn(*args, **kwargs):
        pobj = args[0]
        pname = fn.__name__
        set_logging(pname)
        ret_value = fn(*args, **kwargs)
        unset_logging()
        return ret_value
    return gn

# Move make_class_wrapper inside the log_adjust function to avoid circular import
def log_adjust(fn):
    @wraps(fn)
    def gn(*args, **kwargs):
        pobj = args[0]
        pname = fn.__name__
        set_logging(pname)
        ret_value = fn(*args, **kwargs)
        unset_logging()
        return ret_value
    return gn

def make_class_wrapper(cls):
    class class_wrapper(cls):
        def __getattribute__(self, attr_name):
            attr_fn = super().__getattribute__(attr_name)
            if callable(attr_fn):
                if attr_name not in attr_fn.__self__.__class__.__dict__:
                    return attr_fn
                else:
                    def logged_fn(*args, **kwargs):
                        print(f"Calling {attr_name} with args: {args}, kwargs: {kwargs}")
                        return attr_fn(*args, **kwargs)
                    return logged_fn
            else:
                return attr_fn
    return class_wrapper
