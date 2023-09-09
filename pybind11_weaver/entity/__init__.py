from . import entity_base
from . import enum
from . import klass
from . import namespace
from . import funktion

from clang import cindex

_KIND = cindex.CursorKind

from pybind11_weaver import gen_unit


def create_entity(gu: gen_unit.GenUnit, cursor: cindex.Cursor):
    """Create an entity without parent.

    Note:
         newly created entity has no parent, user must call update_parent() after creation.

         update_parent() will update the parent of the entity and add the entity to the parent's children.

    """
    kind = cursor.kind

    if kind == _KIND.ENUM_DECL:
        return enum.EnumEntity(gu, cursor)
    if kind == _KIND.NAMESPACE:
        return namespace.NamespaceEntity(gu, cursor)
    if kind in [_KIND.CLASS_DECL, _KIND.STRUCT_DECL] and cursor.is_definition():
        return klass.ClassEntity(gu, cursor)
    if kind == _KIND.FUNCTION_DECL:
        return funktion.FunctionEntity(gu, cursor)

    return None
