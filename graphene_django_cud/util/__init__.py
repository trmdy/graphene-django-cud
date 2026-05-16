_STRING_EXPORTS = {"to_camel_case", "to_const", "to_snake_case"}
_MODEL_EXPORTS = {
    "apply_field_name_mappings",
    "convert_many_to_many_like_field",
    "create_dynamic_list_type",
    "create_dynamic_type",
    "disambiguate_id",
    "disambiguate_ids",
    "get_filter_fields_input_args",
    "get_fk_all_extras_field_names",
    "get_input_fields_for_model",
    "get_likely_operation_from_name",
    "get_m2m_all_extras_field_names",
    "get_model_field_or_none",
    "is_field_many_to_many",
    "is_field_many_to_one",
    "is_field_one_to_one",
    "overload_nested_fields",
    "resolve_foreign_key_extra_auto_field_names",
    "resolve_many_to_many_extra_auto_field_names",
    "resolve_many_to_one_extra_auto_field_names",
    "resolve_one_to_one_extra_auto_field_names",
    "validate_foreign_key_extras",
    "validate_many_to_many_extras",
}

__all__ = sorted(_STRING_EXPORTS | _MODEL_EXPORTS)


def __getattr__(name):
    if name in _STRING_EXPORTS:
        from . import string

        return getattr(string, name)

    if name in _MODEL_EXPORTS:
        from . import model

        return getattr(model, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
