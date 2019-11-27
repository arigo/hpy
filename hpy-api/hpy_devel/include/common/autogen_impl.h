
/*
   DO NOT EDIT THIS FILE!

   This file is automatically generated by tools/autogen.py from tools/public_api.h.
   Run this to regenerate:
       make autogen

*/

HPyAPI_STORAGE HPy _HPy_IMPL_NAME(Long_FromLong)(HPyContext ctx, long value)
{
    return _py2h(PyLong_FromLong(value));
}

HPyAPI_STORAGE long _HPy_IMPL_NAME(Long_AsLong)(HPyContext ctx, HPy h)
{
    return PyLong_AsLong(_h2py(h));
}

HPyAPI_STORAGE HPy _HPy_IMPL_NAME(Number_Add)(HPyContext ctx, HPy x, HPy y)
{
    return _py2h(PyNumber_Add(_h2py(x), _h2py(y)));
}

HPyAPI_STORAGE void _HPy_IMPL_NAME(Err_SetString)(HPyContext ctx, HPy type, const char *message)
{
    return PyErr_SetString(_h2py(type), message);
}

HPyAPI_STORAGE int _HPy_IMPL_NAME(Bytes_Check)(HPyContext ctx, HPy o)
{
    return PyBytes_Check(_h2py(o));
}

HPyAPI_STORAGE HPy_ssize_t _HPy_IMPL_NAME(Bytes_Size)(HPyContext ctx, HPy o)
{
    return PyBytes_Size(_h2py(o));
}

HPyAPI_STORAGE HPy_ssize_t _HPy_IMPL_NAME(Bytes_GET_SIZE)(HPyContext ctx, HPy o)
{
    return PyBytes_GET_SIZE(_h2py(o));
}

HPyAPI_STORAGE char *_HPy_IMPL_NAME(Bytes_AsString)(HPyContext ctx, HPy o)
{
    return PyBytes_AsString(_h2py(o));
}

HPyAPI_STORAGE char *_HPy_IMPL_NAME(Bytes_AS_STRING)(HPyContext ctx, HPy o)
{
    return PyBytes_AS_STRING(_h2py(o));
}

HPyAPI_STORAGE HPy _HPy_IMPL_NAME(Unicode_FromString)(HPyContext ctx, const char *utf8)
{
    return _py2h(PyUnicode_FromString(utf8));
}

HPyAPI_STORAGE int _HPy_IMPL_NAME(Unicode_Check)(HPyContext ctx, HPy o)
{
    return PyUnicode_Check(_h2py(o));
}

HPyAPI_STORAGE HPy _HPy_IMPL_NAME(Unicode_AsUTF8String)(HPyContext ctx, HPy o)
{
    return _py2h(PyUnicode_AsUTF8String(_h2py(o)));
}

HPyAPI_STORAGE HPy _HPy_IMPL_NAME(Unicode_FromWideChar)(HPyContext ctx, const wchar_t *w, HPy_ssize_t size)
{
    return _py2h(PyUnicode_FromWideChar(w, size));
}
