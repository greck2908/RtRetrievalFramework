# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _lua_state.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_lua_state', [dirname(__file__)])
        except ImportError:
            import _lua_state
            return _lua_state
        if fp is not None:
            try:
                _mod = imp.load_module('_lua_state', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _lua_state = swig_import_helper()
    del swig_import_helper
else:
    import _lua_state
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x



_lua_state.SHARED_PTR_DISOWN_swigconstant(_lua_state)
SHARED_PTR_DISOWN = _lua_state.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

class LuaState(object):
    """

    This is a light wrapper around the lua_state object.

    This maintains the lifetime of this object, as well as other house
    keeping chores.

    C++ includes: lua_state.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """

        LuaState::LuaState(const std::string &Dir_name="./")
        Create a new instance of Lua.

        Because it is often convenient to do so, you can optionally give a
        directory that the we will change to before running Lua code. This
        allows things like configuration file to use relative paths from where
        the configuration file is located rather than where we are running
        from. 
        """
        _lua_state.LuaState_swiginit(self, _lua_state.new_LuaState(*args))

    def load_file(Fname):
        """

        boost::shared_ptr< LuaState > LuaState::load_file(const std::string &Fname)
        Create a new LuaState, and then open the given file.

        We run this in the same directory as the given file, so for example a
        configuration file can use relative paths for various files that will
        be relative to the location of the configuration file, not the
        directory we happen to be running in. 
        """
        return _lua_state.LuaState_load_file(Fname)

    load_file = staticmethod(load_file)

    def do_file(self, Fname):
        """

        void LuaState::do_file(const std::string &Fname)
        Load the given file and execute it. 
        """
        return _lua_state.LuaState_do_file(self, Fname)


    def run(self, S):
        """

        void LuaState::run(const std::string &S)
        Run the given Lua code. 
        """
        return _lua_state.LuaState_run(self, S)


    def _v_globals(self):
        """

        LuabindObject LuaState::globals()
        Globals table. 
        """
        return _lua_state.LuaState__v_globals(self)


    @property
    def globals(self):
        return self._v_globals()


    def _v_registry(self):
        """

        LuabindObject LuaState::registry()
        Registery table. 
        """
        return _lua_state.LuaState__v_registry(self)


    @property
    def registry(self):
        return self._v_registry()

    __swig_destroy__ = _lua_state.delete_LuaState
LuaState.__str__ = new_instancemethod(_lua_state.LuaState___str__, None, LuaState)
LuaState.do_file = new_instancemethod(_lua_state.LuaState_do_file, None, LuaState)
LuaState.run = new_instancemethod(_lua_state.LuaState_run, None, LuaState)
LuaState._v_globals = new_instancemethod(_lua_state.LuaState__v_globals, None, LuaState)
LuaState._v_registry = new_instancemethod(_lua_state.LuaState__v_registry, None, LuaState)
LuaState_swigregister = _lua_state.LuaState_swigregister
LuaState_swigregister(LuaState)

def LuaState_load_file(Fname):
    """

    boost::shared_ptr< LuaState > LuaState::load_file(const std::string &Fname)
    Create a new LuaState, and then open the given file.

    We run this in the same directory as the given file, so for example a
    configuration file can use relative paths for various files that will
    be relative to the location of the configuration file, not the
    directory we happen to be running in. 
    """
    return _lua_state.LuaState_load_file(Fname)



