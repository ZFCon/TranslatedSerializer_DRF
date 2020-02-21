from rest_framework import serializers

from . import models


class TranslatedSerializer(serializers.ModelSerializer):
    def get_field_names(self, declared_fields, info):
        params = self.context['request'].query_params
        fields = super().get_field_names(declared_fields, info)
        lang = self.Meta.lang
        translated_fields = self.Meta.translated_fields


        if params.get('lang') == lang:
            fields = [i for i in fields if i not in translated_fields]
        else:
            fields = [i for i in fields if not i.endswith("_{}".format(lang))]

        return fields

class TestSerializer(TranslatedSerializer):
    class Meta:
        model = models.Test
        fields = "__all__"
        lang = "ar"
        translated_fields = ['name']
