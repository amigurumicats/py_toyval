from typing import Any, Union, TypeVar


def validate(var: Any, type_: type) -> bool:
    if type_ is None:
        return isinstance(var, type(None))
    if type_ in {type(None), int, float, bool, str, bytes, list, dict, tuple}:
        # built-in
        return isinstance(var, type_)
    elif type_.__module__ == "typing":
        # typing
        if hasattr(type_, "_name") and type_._name == "Any":
            return True
        elif hasattr(type_, "__origin__") and hasattr(type_, "__args__"):
            if type_.__origin__ is list:
                if not isinstance(var, type_.__origin__): return False
                # List
                if isinstance(type_.__args__[0], TypeVar):
                    return validate(var, list)
                # List[Any]
                if type_.__args__[0] is Any:
                    return validate(var, list)
                # List[T]
                return all(validate(el, type_.__args__[0]) for el in var)
            elif type_.__origin__ is dict:
                if not isinstance(var, type_.__origin__): return False
                # Dict
                if isinstance(type_.__args__[0], TypeVar):
                    return validate(var, dict)
                # Dict[T, ?]
                if type_.__args__[0] is not Any:
                    if not all(validate(k, type_.__args__[0]) for k in var.keys()):
                        return False
                # Dict[?, T]
                if type_.__args__[1] is not Any:
                    if not all(validate(v, type_.__args__[1]) for v in var.values()):
                        return False
                return True
            elif type_.__origin__ is tuple:
                if not isinstance(var, type_.__origin__): return False
                if len(type_.__args__) == 0:
                    # Tuple
                    return validate(var, tuple)
                elif type_.__args__[-1] is Ellipsis:
                    # Tuple[int, ...]
                    return all(validate(el, type_.__args__[0]) for el in var)
                else:
                    if len(type_.__args__) != len(var):
                        return False
                    # Tuple[int, str]
                    return all(validate(el, type_.__args__[i]) for i, el in enumerate(var))
            elif type_.__origin__ is Union:
                # Union or Optional
                return any(validate(var, arg) for arg in type_.__args__)
            else:
                raise Exception("sorry")
        else:
            raise Exception("sorry")
    else:
        if issubclass(type_, tuple) and hasattr(type_, "__annotations__"):
            # NamedTuple
            return all(hasattr(var, k) and validate(getattr(var, k), v) for k, v in type_.__annotations__.items())
        elif issubclass(type_, dict) and hasattr(type_, "__annotations__"):
            # TypedDict
            if not isinstance(var, dict): return False
            return all(validate(var.get(k), v) for k, v in type_.__annotations__.items())
        elif hasattr(type_, "__dataclass_fields__") and hasattr(type_, "__annotations__"):
            # dataclass
            return all(hasattr(var, k) and validate(getattr(var, k), v) for k, v in type_.__annotations__.items())
        raise Exception("sorry")
