================================
DjangoCreateMutation
================================

Will create a new mutation which will create a *new* object of the
supplied model.

Mutation input arguments:

+------------+-----------+
| Argument   | Type      |
+============+===========+
| input      | Object!   |
+------------+-----------+

Meta fields:

.. list-table::
   :header-rows: 1
   :widths: 20 12 12 56

   * - Field
     - Type
     - Default
     - Description
   * - ``model``
     - Model
     - ``None``
     - The model. **Required**.
   * - ``only_fields``
     - Iterable
     - ``None``
     - If supplied, only these fields will be added as input variables for the model.
   * - ``exclude_fields``
     - Iterable
     - ``None``
     - If supplied, these fields will be excluded as input variables for the model.
   * - ``return_field_name``
     - String
     - ``None``
     - The name of the return field within the mutation. The default is the camelCased name of the model.
   * - ``permissions``
     - Tuple
     - ``None``
     - The permissions required to access the mutation.
   * - ``login_required``
     - Boolean
     - ``None``
     - If true, the calling user has to be authenticated.
   * - ``auto_context_fields``
     - Dict
     - ``None``
     - A mapping of context values into model fields. See below.
   * - ``optional_fields``
     - Tuple
     - ``()``
     - A list of fields which explicitly should have ``required=False``.
   * - ``required_fields``
     - Tuple
     - ``None``
     - A list of fields which explicitly should have ``required=True``.
   * - ``custom_fields``
     - Tuple
     - ``None``
     - A list of custom graphene fields which will be added to the model input type.
   * - ``type_name``
     - String
     - ``None``
     - If supplied, the input variable in the mutation will have its typename set to this string. This is useful when creating multiple mutations of the same type for a single model.
   * - ``many_to_many_extras``
     - Dict
     - ``{}``
     - A dict with extra information regarding many-to-many fields. See below.
   * - ``many_to_one_extras``
     - Dict
     - ``{}``
     - A dict with extra information regarding many-to-one relations. See below.
   * - ``foreign_key_extras``
     - Dict
     - ``{}``
     - A dict with extra information regarding foreign key extras.
   * - ``one_to_one_extras``
     - Dict
     - ``{}``
     - A dict with extra information regarding one-to-one extras.

.. code:: graphql

    mutation {
        createUser(input: {name: "John Doe", address: "Downing Street 10"}){
            user{
                id
                name
                address
            }
        }
    }
