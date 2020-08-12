from rest_framework import serializers

from .models import CategoryModel, ShelvesModel, BookModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ('user',)
        fields = '__all__'
        model = CategoryModel


class ShelvesSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ('user',)
        fields = '__all__'
        model = ShelvesModel


class BookSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(BookSerializer, self).__init__(*args, **kwargs)
        context = self.context.get('request')
        if context:
            user = context.user
            self.fields.get('shelf').queryset = ShelvesModel.objects.filter(user=user)

    class Meta:
        read_only_fields = ('user',)
        fields = '__all__'
        model = BookModel
