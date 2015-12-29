.. index:: 
   double: nano.blog; blog

blog
====
A very basic blog-app.

It has optional suppport for `django-taggit`.

.. automodule:: nano.blog

Models
------

.. autoclass:: nano.blog.models.Entry

Tools
-----

.. automodule:: nano.blog.tools
   :members:

.. index::
    double: nano.blog; settings

Changes to settings
-------------------

NANO_BLOG_USE_TAGS (optional)
    Set to True to use `django-taggit` if it is installed.

    **Default**: Not set

NANO_BLOG_SPECIAL_TAGS (optional)
    A list of tags that may be treated specially.

    **Default**: ``('pinned',)``
