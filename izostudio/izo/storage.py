import os
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CKEditor5Storage(FileSystemStorage):
    """Хранит загруженные в CKEditor 5 файлы в media/uploads/."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('location', os.path.join(settings.MEDIA_ROOT, 'uploads'))
        kwargs.setdefault('base_url', urljoin(settings.MEDIA_URL, 'uploads/'))
        super().__init__(*args, **kwargs)
