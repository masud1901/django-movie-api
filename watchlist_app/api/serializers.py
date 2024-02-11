from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("watchlist",)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    # platform = serializers.CharField(source="platform.name", read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["platform"] = instance.platform.name
        return representation


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
