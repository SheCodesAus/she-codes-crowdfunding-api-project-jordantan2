from rest_framework import serializers
from .models import Product, Project, ProjectProduct, Category


class ProjectProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return ProjectProduct.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    image = serializers.URLField()
    # is_open = serializers.BooleanField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source="owner.id")
    category = serializers.SlugRelatedField(
        slug_field="slug", queryset=Category.objects.all()
    )

    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class ProjectDetailSerializer(ProjectSerializer):
    pledges = ProjectProductSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.image = validated_data.get("image", instance.image)
        # instance.is_open = validated_data.get("is_open", instance.is_open)
        instance.date_created = validated_data.get(
            "date_created", instance.date_created
        )
        instance.owner = validated_data.get("owner", instance.owner)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
