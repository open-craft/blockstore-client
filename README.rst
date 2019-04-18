Blockstore Client
=================

This package contains a python REST API client library for the Open edX Blockstore REST API. It also contains a command line tool that makes it easy to work with Blockstore from the command line.

This package supports Python 2 and 3.

Details
-------

The API client code in this repository is mostly auto-generated from Blockstore's OpenAPI specification file, using `openapi-generator <https://github.com/OpenAPITools/openapi-generator>`_. Do not edit the code in `blockstore_api`, as your changes will be lost (except for a few of the models, which can be edited). Instead, update the Blockstore API spec file, then run `make api-client` in this repository to update the auto-generated code.

Usage Example
-------------

Using the Tagstore API::

    >>> from blockstore_api import TagstoreApi, Taxonomy, Tag, Entity
    >>> tagstore = TagstoreApi()

Create a computer science taxonomy::

    >>> tax = tagstore.create_taxonomy(Taxonomy(name="Computer Science Taxonomy"))
    >>> tax.id
    42
    >>> language_tag = tagstore.add_taxonomy_tag(tax.id, Tag(name="Programming Languages"))
    >>> python_tag = tagstore.add_taxonomy_tag(tax.id, Tag(name="Python", parent=language_tag.name))
    >>> rust_tag = tagstore.add_taxonomy_tag(tax.id, Tag(name="Rust", parent=language_tag.name))

Check what tags an entity has::

    >>> entity_id = dict(external_id="Open edX", entity_type="software")
    >>> tagstore.get_entity(**entity_id).tags
    []

Apply a tag to the entity::

    >>> tagstore.add_tag_to_entity(**entity_id, **python_tag.id)
    >>> tagstore.get_entity(**entity_id).tags

License
-------

The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. Please see the LICENSE_ file for details.

.. _LICENSE: https://github.com/edx/{{cookiecutter.repo_name}}/blob/master/LICENSE

How To Contribute
-----------------

Contributions are welcome. Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details. Even though it was written with ``edx-platform`` in mind, these guidelines should be followed for Open edX code in general.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Get Help
--------

Ask questions and discuss this project on `Slack <https://openedx.slack.com/messages/general/>`_ or in the `edx-code Google Group <https://groups.google.com/forum/#!forum/edx-code>`_.
