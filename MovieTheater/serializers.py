from rest_framework import serializers
from .models import *

class cinemaSerializer(serializers.ModelSerializer):
	# nama = serializers.CharField(max_length=27)
	# alamat = serializers.CharField(max_length=100)
	# kontak = serializers.IntegerField()
	class Meta:
		model = cinema
		fields = ('nama', 'alamat', 'kontak')

	def create(self, validated_data):
		cinemas = cinema(**validated_data)
		cinemas.save()
		return cinemas

class movieSerializer(serializers.ModelSerializer):
	# judul = serializers.CharField(max_length=100)
	# kategori = serializers.CharField( max_length=100)
	# tahun = serializers.IntegerField()
	class Meta:
		model = movie
		fields = '__all__'

	def create(self, validated_data):
		movies = movie(**validated_data)
		movies.save()
		return movies

class showingSerializer(serializers.ModelSerializer):
	# showing_time = serializers.TimeField()
	# showing_date = serializers.DateField()
	# movies = serializers.ForeignKey(movie, on_delete=models.CASCADE)
	movies = movieSerializer(many=False)
	class Meta:
		model = showing
		fields = ('showing_time', 'showing_date', 'movies')
		# fields = '__all__'

	def create(self, validated_data):
		movie_data = validated_data.pop('movies')
		movie1 = movie.objects.get(**movie_data)
		showings = showing.objects.create(movies=movie1, **validated_data)
		return showings
		# showings = showing(**validated_data)
		# showings.save()
		# return showings

	def update(self, instance, validated_data):
		instance.showing_time = validated_data.get('showing_time', instance.showing_time)
		instance.showing_date = validated_data.get('showing_date', instance.showing_date)
		movie_data = validated_data.pop('movies')
		movie1 = movie.objects.get(**movie_data)
		instance.movies = movie1
		instance.save()
		return instance

class theaterSerializer(serializers.ModelSerializer):
	# nama = serializers.CharField(max_length=27)
	# kapasitas = serializers.IntegerField()
	# cinemas = serializers.ForeignKey(cinema, on_delete=models.CASCADE)
	# showings = serializers.ManyToManyField(showing)
	cinemas = cinemaSerializer(many=False, read_only=True)
	showings = showingSerializer(many=True)
	class Meta:
		model = theater
		fields = ('nama', 'kapasitas', 'cinemas', 'showings')

class ticketSerializer(serializers.ModelSerializer):
	# nomor_kursi = serializers.CharField(max_length=10)
	# harga = serializers.IntegerField()
	# showings = serializers.ForeignKey(showing, on_delete=models.CASCADE)
	showings = showingSerializer(many=False)
	class Meta:
		model = ticket
		fields = '__all__'