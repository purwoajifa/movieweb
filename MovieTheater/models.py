from django.db import models

class cinema(models.Model):
	nama = models.CharField('Nama', max_length=27)
	alamat = models.CharField('Alamat', max_length=100)
	kontak = models.IntegerField()

	def __str__(self):
		return self.nama

	def __iter__(self):
		return iter([self.nama,
		self.alamat,
		self.kontak
		])

class movie(models.Model):
	judul = models.CharField('Judul', max_length=100)
	kategori = models.CharField('Kategori', max_length=100)
	tahun = models.IntegerField()

	def __str__(self):
		return self.judul

	def __iter__(self):
		return iter([self.judul,
		self.kategori,
		self.tahun
		])

class showing(models.Model):
	showing_time = models.TimeField()
	showing_date = models.DateField()
	movies = models.ForeignKey(movie, on_delete=models.CASCADE)

	def __str__(self):
		return self.movies.judul

class theater(models.Model):
	nama = models.CharField('Nama', max_length=27)
	kapasitas = models.IntegerField()
	cinemas = models.ForeignKey(cinema, on_delete=models.CASCADE)
	showings = models.ManyToManyField(showing)

	def __str__(self):
		return self.nama

class ticket(models.Model):
	nomor_kursi = models.CharField(max_length=10)
	harga = models.IntegerField()
	showings = models.ForeignKey(showing, on_delete=models.CASCADE)

	def __str__(self):
		return self.nomor_kursi