# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _lsi_rt.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_lsi_rt', [dirname(__file__)])
        except ImportError:
            import _lsi_rt
            return _lsi_rt
        if fp is not None:
            try:
                _mod = imp.load_module('_lsi_rt', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _lsi_rt = swig_import_helper()
    del swig_import_helper
else:
    import _lsi_rt
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



_lsi_rt.SHARED_PTR_DISOWN_swigconstant(_lsi_rt)
SHARED_PTR_DISOWN = _lsi_rt.SHARED_PTR_DISOWN

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

import full_physics_swig.radiative_transfer_fixed_stokes_coefficient
import full_physics_swig.radiative_transfer
import full_physics_swig.generic_object
import full_physics_swig.observer
import full_physics_swig.named_spectrum
import full_physics_swig.state_vector
class LsiRt(full_physics_swig.radiative_transfer_fixed_stokes_coefficient.RadiativeTransferFixedStokesCoefficient):
    """

    This does a Low Stream Interpolator correction to another
    RadiativeTransfer object.

    There is a paper in the doc directory "LSI Paper.pdf" which
    describes this algorithm. Note that the paper describes an improved
    version, the code here is for an older implementation (we will update
    the papers version eventually).

    There is a configuration file that gives the optical depth boundaries
    to use in the LSI binning. This can either be read from an HDF file
    (the preferred way), or for backwards compatibility from an ASCII
    file.

    C++ includes: lsi_rt.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    @property
    def number_stokes(self):
        return self._v_number_stokes()


    def correction_only(self, Spec_domain, Spec_index):
        """

        ArrayAd< double, 2 > LsiRt::correction_only(const SpectralDomain &Spec_domain, int Spec_index) const
        Normally we calculate both the low streams stokes parameters, the LSI
        correction, and we apply them.

        However for testing it can be useful to calculate just the LSI
        correction. This is much faster to calculate, and allows us to test
        the LSI without doing the full RT calculation. 
        """
        return _lsi_rt.LsiRt_correction_only(self, Spec_domain, Spec_index)


    def _v_low_stream_radiative_transfer(self):
        """

        boost::shared_ptr<RadiativeTransfer> FullPhysics::LsiRt::low_stream_radiative_transfer() const

        """
        return _lsi_rt.LsiRt__v_low_stream_radiative_transfer(self)


    @property
    def low_stream_radiative_transfer(self):
        return self._v_low_stream_radiative_transfer()


    def _v_high_stream_radiative_transfer(self):
        """

        boost::shared_ptr<RadiativeTransfer> FullPhysics::LsiRt::high_stream_radiative_transfer() const

        """
        return _lsi_rt.LsiRt__v_high_stream_radiative_transfer(self)


    @property
    def high_stream_radiative_transfer(self):
        return self._v_high_stream_radiative_transfer()

    __swig_destroy__ = _lsi_rt.delete_LsiRt
LsiRt.correction_only = new_instancemethod(_lsi_rt.LsiRt_correction_only, None, LsiRt)
LsiRt._v_low_stream_radiative_transfer = new_instancemethod(_lsi_rt.LsiRt__v_low_stream_radiative_transfer, None, LsiRt)
LsiRt._v_high_stream_radiative_transfer = new_instancemethod(_lsi_rt.LsiRt__v_high_stream_radiative_transfer, None, LsiRt)
LsiRt_swigregister = _lsi_rt.LsiRt_swigregister
LsiRt_swigregister(LsiRt)



