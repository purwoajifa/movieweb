from django.shortcuts import render
from MovieTheater.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import status

@api_view(['GET'])
def get_all_cinema(request):
	cinemas = cinema.objects.all()
	serializer = cinemaSerializer(cinemas, many= True).data
	return Response({"data" : serializer}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def get_cinema(request, id):
	try:
		cinema1 = cinema.objects.get(id=id)
	except cinema.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serial = cinemaSerializer(cinema1).data
		return Response({"data" : serial}, status=status.HTTP_200_OK)
	elif request.method == 'PUT':
		serializer = cinemaSerializer(cinema1, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		cinema1.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_all_movie(request):
	movies = movie.objects.all()
	serializer = movieSerializer(movies, many= True).data
	return Response({"data" : serializer}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def get_movie(request, id):
	try:
		movie1 = movie.objects.get(id=id)
	except movie.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = movieSerializer(movie1).data
		return Response({"data" : serializer}, status=status.HTTP_200_OK)
	elif request.method == 'PUT':
		serializer = movieSerializer(movie1, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		movie1.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_all_showing(request):
	showings = showing.objects.all()
	serializer = showingSerializer(showings, many= True).data
	return Response({"data" : serializer}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def get_showing(request, id):
	try:
		showing1 = showing.objects.get(id=id)
	except showing.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = showingSerializer(showing1).data
		return Response({"data" : serializer}, status=status.HTTP_200_OK)
	elif request.method == 'PUT':
		serializer = showingSerializer(showing1, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		showing1.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_cinema(request):
	cinema = cinemaSerializer(data = request.data)
	if cinema.is_valid():
		cinema.save()
		return Response({"data" : "Berhasil Memasukkan Cinema"}, status=status.HTTP_201_CREATED)
	else:
		error_details = []
		for key in cinema.errors.keys():
			error_details.append({"field": key, "message": cinema.errors[key][0]})

		data = {
				"Error": {
					"status": 400,
					"message": "Data tidak valid",
					"error_details": error_details
					}
				}

		return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_movie(request):
	movie = movieSerializer(data = request.data)
	if movie.is_valid():
		movie.save()
		return Response({"data" : "Berhasil Memasukkan Movie"}, status=status.HTTP_201_CREATED)
	else:
		error_details = []
		for key in movie.errors.keys():
			error_details.append({"field": key, "message": movie.errors[key][0]})

		data = {
				"Error": {
					"status": 400,
					"message": "Data tidak valid",
					"error_details": error_details
					}
				}

		return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_showing(request):
	showing = showingSerializer(data = request.data)
	if showing.is_valid():
		showing.save()
		return Response({"data" : "Berhasil Memasukkan Showing"}, status=status.HTTP_201_CREATED)
	else:
		error_details = []
		for key in showing.errors.keys():
			error_details.append({"field": key, "message": showing.errors[key][0]})

		data = {
				"Error": {
					"status": 400,
					"message": "Data tidak valid",
					"error_details": error_details
					}
				}

		return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_theater(request):
	theaters = theater.objects.all()
	serializer = theaterSerializer(theaters, many= True).data
	return Response({"data" : serializer}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_ticket(request):
	tickets = ticket.objects.all()
	serializer = ticketSerializer(tickets, many= True).data
	return Response({"data" : serializer}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def get_theater(request, id):
	try:
		theater1 = theater.objects.get(id=id)
	except theater.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = theaterSerializer(theater1).data
		return Response({"data" : serializer}, status=status.HTTP_200_OK)
	elif request.method == 'PUT':
		serializer = theaterSerializer(theater1, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		theater1.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def get_ticket(request, id):
	try:
		ticket1 = ticket.objects.get(id=id)
	except ticket.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ticketSerializer(ticket1).data
		return Response({"data" : serializer}, status=status.HTTP_200_OK)
	elif request.method == 'PUT':
		serializer = ticketSerializer(ticket1, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"data" : serializer.data}, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		ticket1.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)