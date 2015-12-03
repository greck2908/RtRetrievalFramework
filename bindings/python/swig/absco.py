# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _absco.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_absco', [dirname(__file__)])
        except ImportError:
            import _absco
            return _absco
        if fp is not None:
            try:
                _mod = imp.load_module('_absco', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _absco = swig_import_helper()
    del swig_import_helper
else:
    import _absco
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


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _absco.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_absco.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_absco.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_absco.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_absco.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_absco.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_absco.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_absco.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_absco.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_absco.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_absco.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_absco.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_absco.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_absco.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_absco.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_absco.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_absco.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _absco.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_absco.SHARED_PTR_DISOWN_swigconstant(_absco)
SHARED_PTR_DISOWN = _absco.SHARED_PTR_DISOWN

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

import full_physics_swig.gas_absorption
import full_physics_swig.generic_object
class Absco(full_physics_swig.gas_absorption.GasAbsorption):
    """

    This class is used to read the absco tables.

    C++ includes: absco.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def _v_number_broadener_vmr(self):
        """

        virtual int FullPhysics::Absco::number_broadener_vmr() const
        Number of broadener VMR values in absco file.

        This may be 0, if we don't have any broadening. 
        """
        return _absco.Absco__v_number_broadener_vmr(self)


    @property
    def number_broadener_vmr(self):
        return self._v_number_broadener_vmr()


    def _v_number_layer(self):
        """

        virtual int FullPhysics::Absco::number_layer() const
        Number of pressure layers in absco file. 
        """
        return _absco.Absco__v_number_layer(self)


    @property
    def number_layer(self):
        return self._v_number_layer()


    def _v_number_temperature(self):
        """

        virtual int FullPhysics::Absco::number_temperature() const
        Number of temperature values in absco file. 
        """
        return _absco.Absco__v_number_temperature(self)


    @property
    def number_temperature(self):
        return self._v_number_temperature()


    def _v_broadener_vmr_grid(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::Absco::broadener_vmr_grid() const =0
        Return the broadener VMR grid used for this Absco file.

        This is number_broadener_vmr() in size, which may be size 0.

        This is dimensionless. 
        """
        return _absco.Absco__v_broadener_vmr_grid(self)


    @property
    def broadener_vmr_grid(self):
        return self._v_broadener_vmr_grid()


    def _v_pressure_grid(self):
        """

        virtual blitz::Array<double, 1> FullPhysics::Absco::pressure_grid() const =0
        Return the pressure grid used for this Absco file.

        This is number_layer() in size.

        This is in Pascals. 
        """
        return _absco.Absco__v_pressure_grid(self)


    @property
    def pressure_grid(self):
        return self._v_pressure_grid()


    def _v_temperature_grid(self):
        """

        virtual blitz::Array<double, 2> FullPhysics::Absco::temperature_grid() const =0
        Return the temperature grid for this Absco file.

        This is number_layer() x number_temperature() in size.

        This is in Kelvin. 
        """
        return _absco.Absco__v_temperature_grid(self)


    @property
    def temperature_grid(self):
        return self._v_temperature_grid()


    @property
    def broadener_name(self):
        return self._v_broadener_name()


    def table_scale(self, wn):
        """

        virtual double FullPhysics::Absco::table_scale(double wn) const =0
        Scale to apply to underlying ABSCO data to get the
        absorption_cross_section.

        This allows empirical corrections to be applied the ABSCO tables
        (e.g., O2 scaling). Note that as a user you don't need to apply this
        correction, it is already applied in absorption_cross_section() and
        AbscoInterpolator. 
        """
        return _absco.Absco_table_scale(self, wn)


    def absorption_cross_section(self, *args):
        """

        AutoDerivativeWithUnit< double > Absco::absorption_cross_section(double wn, const DoubleWithUnit &press, const AutoDerivativeWithUnit<
        double > &temp, const AutoDerivativeWithUnit< double > &broadener_vmr)
        const

        """
        return _absco.Absco_absorption_cross_section(self, *args)

    __swig_destroy__ = _absco.delete_Absco
Absco._v_number_broadener_vmr = new_instancemethod(_absco.Absco__v_number_broadener_vmr, None, Absco)
Absco._v_number_layer = new_instancemethod(_absco.Absco__v_number_layer, None, Absco)
Absco._v_number_temperature = new_instancemethod(_absco.Absco__v_number_temperature, None, Absco)
Absco._v_broadener_vmr_grid = new_instancemethod(_absco.Absco__v_broadener_vmr_grid, None, Absco)
Absco._v_pressure_grid = new_instancemethod(_absco.Absco__v_pressure_grid, None, Absco)
Absco._v_temperature_grid = new_instancemethod(_absco.Absco__v_temperature_grid, None, Absco)
Absco.table_scale = new_instancemethod(_absco.Absco_table_scale, None, Absco)
Absco.absorption_cross_section = new_instancemethod(_absco.Absco_absorption_cross_section, None, Absco)
Absco.read_double = new_instancemethod(_absco.Absco_read_double, None, Absco)
Absco.read_float = new_instancemethod(_absco.Absco_read_float, None, Absco)
Absco_swigregister = _absco.Absco_swigregister
Absco_swigregister(Absco)

class vector_absco(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _absco.vector_absco_swiginit(self, _absco.new_vector_absco(*args))
    __swig_destroy__ = _absco.delete_vector_absco
vector_absco.iterator = new_instancemethod(_absco.vector_absco_iterator, None, vector_absco)
vector_absco.__nonzero__ = new_instancemethod(_absco.vector_absco___nonzero__, None, vector_absco)
vector_absco.__bool__ = new_instancemethod(_absco.vector_absco___bool__, None, vector_absco)
vector_absco.__len__ = new_instancemethod(_absco.vector_absco___len__, None, vector_absco)
vector_absco.pop = new_instancemethod(_absco.vector_absco_pop, None, vector_absco)
vector_absco.__getslice__ = new_instancemethod(_absco.vector_absco___getslice__, None, vector_absco)
vector_absco.__setslice__ = new_instancemethod(_absco.vector_absco___setslice__, None, vector_absco)
vector_absco.__delslice__ = new_instancemethod(_absco.vector_absco___delslice__, None, vector_absco)
vector_absco.__delitem__ = new_instancemethod(_absco.vector_absco___delitem__, None, vector_absco)
vector_absco.__getitem__ = new_instancemethod(_absco.vector_absco___getitem__, None, vector_absco)
vector_absco.__setitem__ = new_instancemethod(_absco.vector_absco___setitem__, None, vector_absco)
vector_absco.append = new_instancemethod(_absco.vector_absco_append, None, vector_absco)
vector_absco.empty = new_instancemethod(_absco.vector_absco_empty, None, vector_absco)
vector_absco.size = new_instancemethod(_absco.vector_absco_size, None, vector_absco)
vector_absco.clear = new_instancemethod(_absco.vector_absco_clear, None, vector_absco)
vector_absco.swap = new_instancemethod(_absco.vector_absco_swap, None, vector_absco)
vector_absco.get_allocator = new_instancemethod(_absco.vector_absco_get_allocator, None, vector_absco)
vector_absco.begin = new_instancemethod(_absco.vector_absco_begin, None, vector_absco)
vector_absco.end = new_instancemethod(_absco.vector_absco_end, None, vector_absco)
vector_absco.rbegin = new_instancemethod(_absco.vector_absco_rbegin, None, vector_absco)
vector_absco.rend = new_instancemethod(_absco.vector_absco_rend, None, vector_absco)
vector_absco.pop_back = new_instancemethod(_absco.vector_absco_pop_back, None, vector_absco)
vector_absco.erase = new_instancemethod(_absco.vector_absco_erase, None, vector_absco)
vector_absco.push_back = new_instancemethod(_absco.vector_absco_push_back, None, vector_absco)
vector_absco.front = new_instancemethod(_absco.vector_absco_front, None, vector_absco)
vector_absco.back = new_instancemethod(_absco.vector_absco_back, None, vector_absco)
vector_absco.assign = new_instancemethod(_absco.vector_absco_assign, None, vector_absco)
vector_absco.resize = new_instancemethod(_absco.vector_absco_resize, None, vector_absco)
vector_absco.insert = new_instancemethod(_absco.vector_absco_insert, None, vector_absco)
vector_absco.reserve = new_instancemethod(_absco.vector_absco_reserve, None, vector_absco)
vector_absco.capacity = new_instancemethod(_absco.vector_absco_capacity, None, vector_absco)
vector_absco_swigregister = _absco.vector_absco_swigregister
vector_absco_swigregister(vector_absco)



