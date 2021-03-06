"""
NOTE: these tests are also meant to be run as PyPy "applevel" tests.

This means that global imports will NOT be visible inside the test
functions. In particular, you have to "import pytest" inside the test in order
to be able to use e.g. pytest.raises (which on PyPy will be implemented by a
"fake pytest module")
"""
from .support import HPyTest


class TestType(HPyTest):

    def test_simple_type(self):
        mod = self.make_module("""
            static HPyType_Slot Dummy_slots[] = {
                {0, NULL},
            };

            static HPyType_Spec Dummy_spec = {
                .name = "mytest.Dummy",
                .itemsize = 0,
                .flags = HPy_TPFLAGS_DEFAULT | HPy_TPFLAGS_BASETYPE,
                .slots = Dummy_slots,
            };

            @EXPORT_TYPE("Dummy", Dummy_spec)
            @INIT
        """)
        assert isinstance(mod.Dummy, type)
        assert mod.Dummy.__name__ == 'Dummy'
        assert mod.Dummy.__module__ == 'mytest'
        assert isinstance(mod.Dummy(), mod.Dummy)

        class Sub(mod.Dummy):
            pass
        assert isinstance(Sub(), mod.Dummy)

    def test_slots(self):
        mod = self.make_module("""
            HPy_DEF_METH_NOARGS(Dummy_repr)
            static HPy Dummy_repr_impl(HPyContext ctx, HPy self)
            {
                return HPyUnicode_FromString(ctx, "<Dummy>");
            }

            HPy_DEF_METH_NOARGS(Dummy_abs)
            static HPy Dummy_abs_impl(HPyContext ctx, HPy self)
            {
                return HPyLong_FromLong(ctx, 1234);
            }

            static HPyType_Slot Dummy_slots[] = {
                {Py_tp_repr, Dummy_repr},
                {Py_nb_absolute, Dummy_abs},
                {0, NULL},
            };

            static HPyType_Spec Dummy_spec = {
                .name = "mytest.Dummy",
                .slots = Dummy_slots
            };

            @EXPORT_TYPE("Dummy", Dummy_spec)
            @INIT
        """)
        d = mod.Dummy()
        assert repr(d) == '<Dummy>'
        assert abs(d) == 1234

    def test_tp_methods(self):
        mod = self.make_module("""
            HPy_DEF_METH_O(Dummy_foo)
            static HPy Dummy_foo_impl(HPyContext ctx, HPy self, HPy arg)
            {
                return HPy_Add(ctx, arg, arg);
            }

            HPy_DEF_METH_NOARGS(Dummy_bar)
            static HPy Dummy_bar_impl(HPyContext ctx, HPy self)
            {
                return HPyLong_FromLong(ctx, 1234);
            }

            static HPyMethodDef Dummy_methods[] = {
                {"foo", Dummy_foo, HPy_METH_O},
                {"bar", Dummy_bar, HPy_METH_NOARGS},
                {NULL}
            };

            static HPyType_Slot dummy_type_slots[] = {
                {Py_tp_methods, Dummy_methods},
                {0, NULL},
            };

            static HPyType_Spec dummy_type_spec = {
                .name = "mytest.Dummy",
                .slots = dummy_type_slots,
            };

            @EXPORT_TYPE("Dummy", dummy_type_spec)
            @INIT
        """)
        d = mod.Dummy()
        assert d.foo(21) == 42
        assert d.bar() == 1234

    def test_HPy_New(self):
        mod = self.make_module("""
            typedef struct {
                long x;
                long y;
            } PointObject;

            HPy_DEF_METH_KEYWORDS(Point_new)
            static HPy Point_new_impl(HPyContext ctx, HPy cls, HPy *args,
                                      HPy_ssize_t nargs, HPy kw)
            {
                PointObject *point;
                HPy h_point = HPy_New(ctx, cls, &point);
                if (HPy_IsNull(h_point))
                    return HPy_NULL;
                point->x = 7;
                point->y = 3;
                return h_point;
            }

            HPy_DEF_METH_NOARGS(Point_foo)
            static HPy Point_foo_impl(HPyContext ctx, HPy self)
            {
                PointObject *point = HPy_CAST(ctx, PointObject, self);
                return HPyLong_FromLong(ctx, point->x*10 + point->y);
            }

            static HPyMethodDef Point_methods[] = {
                {"foo", Point_foo, HPy_METH_NOARGS},
                {NULL},
            };

            static HPyType_Slot Point_slots[] = {
                {Py_tp_new, Point_new},
                {Py_tp_methods, Point_methods},
                {0, NULL},
            };

            static HPyType_Spec Point_spec = {
                .name = "mytest.Point",
                .basicsize = sizeof(PointObject),
                .slots = Point_slots,
            };

            @EXPORT_TYPE("Point", Point_spec)
            @INIT
        """)
        p = mod.Point()
        assert p.foo() == 73
