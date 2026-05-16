.. _signals:

================================
Signals
================================

The library fires custom Django signals at the end of CUD mutation execution. These are useful when you want to react to mutation-level events rather than raw model ``post_save``/``post_delete`` events.

Available signals
-----------------

The following signals are available from ``graphene_django_cud.signals``:

* ``post_create_mutation``
* ``post_update_mutation``
* ``post_delete_mutation``
* ``post_batch_create_mutation``
* ``post_batch_update_mutation``
* ``post_batch_delete_mutation``
* ``post_filter_update_mutation``
* ``post_filter_delete_mutation``

Example
-------

.. code:: python

    from graphene_django_cud.signals import post_create_mutation

    @post_create_mutation.connect
    def handle_post_create_mutation(sender, instance, **kwargs):
        print(f"A new instance was created by {sender}: {instance}")

Signal arguments
----------------

``post_create_mutation``
    ``sender``
        The mutation class.
    ``instance``
        The instance that was created.

``post_update_mutation``
    ``sender``
        The mutation class.
    ``instance``
        The instance that was updated.

``post_delete_mutation``
    ``sender``
        The mutation class.
    ``id``
        The id returned by the mutation. This may be a Relay global id when Relay is used, and can be customized by overriding ``get_return_id``.
    ``raw_id``
        The raw database id of the deleted instance.
    ``deleted_input_id``
        The id value supplied to the delete mutation.

``post_batch_create_mutation``
    ``sender``
        The mutation class.
    ``instances``
        The instances that were created.

``post_batch_update_mutation``
    ``sender``
        The mutation class.
    ``instances``
        The instances that were updated.

``post_batch_delete_mutation``
    ``sender``
        The mutation class.
    ``ids``
        The input ids supplied to the mutation.
    ``deletion_count``
        The number of instances that were deleted.
    ``deleted_ids``
        The ids returned by the mutation. These can be customized by overriding ``get_return_id``.

``post_filter_update_mutation``
    ``sender``
        The mutation class.
    ``instances``
        A queryset of the instances that were updated.

``post_filter_delete_mutation``
    ``sender``
        The mutation class.
    ``ids``
        The ids of the instances that were deleted.
