import pytest
from django.test import TestCase
from django.core.urlresolvers import resolve, Resolver404


class URL解決テスト(TestCase):
    def test_helloのパスが404とならないこと(self):
        try:
            resolve('/mysite/hello')
        except Resolver404:
            pytest.fail('raise error')