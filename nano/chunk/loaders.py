"""
Wrapper for loading templates from the filesystem.
"""

from django.apps import apps
from django.conf import settings
from django.template.base import TemplateDoesNotExist
from django.utils._os import safe_join

from django.template.loaders.base import Loader

class ChunkLoader(Loader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        chunk_model = apps.get_model('chunk', 'Chunk')
        chunk_model_name = chunk_model.__name__
        template_id = (self.chunk_model_name, template_name)
        try:
            chunk = self.chunk_model.objects.get(slug=template_name)
            return (chunk.content, "chunk:%s:%s" % template_id)
        except self.chunk_model.DoesNotExist:
            error_msg = "Couldn't find a %s-chunk named %s" % template_id
            raise TemplateDoesNotExist(error_msg)
